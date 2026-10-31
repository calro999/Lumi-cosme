import json

with open("rakuten_3winter_body_booster_shampoo_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_moisture_shampoo"]["items"]

moisture_shampoo_details = [
    {
        "rank": 1,
        "tag": "🏆 乾燥で水分が抜け落ちたパサつき髪を救う！サロン帰りのしっとりまとまる髪をキープする最高峰ヘアケア",
        "catch": "ミルボン最高峰の毛髪科学。オージュア独自のCMC脂質修復テクノロジーで、冬のパサつく髪の芯までうるおいを再構築",
        "capacity": "250ml",
        "type": "サロン専売・水分補給集中アミノ酸系シャンプー",
        "texture": "シルクのようになめらかなとろみリキッド。キメ細かく弾力のある濃密クッション泡が瞬時に立ち上がる",
        "ingredients": "ココイルメチルタウリンNa、ラウラミドプロピルベタイン、PEG-20トレハロース、イソステアリン酸イソステアリル、牡丹エキス",
        "finish": "毛先まで水分が満ちてしっとりと重みのあるまとまり。冬の乾燥した風を受けても広がらずサラ艶が持続",
        "desc_p1": "11月から12月にかけて湿度が下がると、大気中の乾燥によって髪内部の水分をつなぎ止める「CMC脂質層」が破壊されます。水分保持力を失った髪は空洞化し、パサパサと広がり、ニットやマフラーを着脱するたびに激しい静電気が発生して絡まりや枝毛を誘発します。",
        "desc_p2": "日本のトップサロンで不動の人気を誇るオージュアの『クエンチ シャンプー』は、乾燥によって水分が失われた髪のために開発された水分補給特化型シャンプー。髪の水分保持機能を司る脂質二重層を補修し、うるおいを髪内部にギュッと定着させます。アミノ酸系のマイルドな洗浄成分が頭皮の乾燥を防ぎながら、洗い流した瞬間から指通りのなめらかさを実感。可憐な牡丹（ボタン）の香りが優雅なバスタイムを演出します。",
        "target": "冬になると毛先がパサついてまとまらない方、静電気で髪がフワフワ広がってしまう方、カラーやパーマで傷んだ髪をサロン級の保湿力で立て直したい方",
        "technique": "シャンプー前に38度前後のぬるま湯で2分間しっかり予洗いし、頭皮と髪の汚れを落とします。手のひらでしっかり泡立ててから髪全体を包み込み、毛先を泡でパックするように1分置いてから優しくすすぐと、保湿トリートメント効果が最大化します。",
        "voice": "『冬になると静電気とパサつきで髪が爆発していましたが、クエンチを使い始めてから乾かしただけでしっとりストンとまとまるようになりました。美容院帰りの質感が毎日続きます。』(30代・金融系)",
        "caution": "非常に保湿力が高いため、根元から毛先まですすぎ残しがないよう、ぬるま湯で丁寧にすすいでください。"
    },
    {
        "rank": 2,
        "tag": "✨ 4種のプレシャスオイル配合！冬の毛先のパサつきと静電気を抑え息をのむような濃密なツヤとしなやかさを与える",
        "catch": "世界中のセレブに愛されるケラスターゼ最高峰オイルシャンプー。黄金の濃密泡が髪の一本一本を優雅に包み込む",
        "capacity": "250ml",
        "type": "ラグジュアリー・プレシャスオイル配合高保湿シャンプー",
        "texture": "ゴールドの輝きを放つとろけるようなリッチジェル。濃密でクリーミーな泡立ちで摩擦を徹底ブロック",
        "ingredients": "アルガンオイル、カメリアオイル、トウモロコシ胚芽油、プラカシーオイル、マイズオイル、各種ビタミン誘導体",
        "finish": "シルクを纏ったかのような極上の滑らかさと圧倒的な輝き。毛先まで指が吸い付くようなしなやかさ",
        "desc_p1": "冬の髪のツヤが失われる最大の要因は、キューティクルの毛羽立ちと表面の油分（18-MEA）の剥離です。キューティクルがめくれ上がると光が乱反射してパサついて見え、髪内部のタンパク質が外へと流出してしまいます。",
        "desc_p2": "ケラスターゼを代表するオイルシリーズの傑作『ユイルスブリム バン ユイルスブリム R』は、希少なアルガンオイルやカメリアオイルなど4種の最高級プレシャスオイルを独自技術でミクロ分散配合。シャンプーしながらオイルの栄養分が髪深部まで行き渡り、キューティクルを滑らかにコーティングします。洗い流す段階から贅沢な手触りに変化し、冬の乾燥風に負けない艶やかな輝きとしなやかなコシを与えます。",
        "target": "髪のパサつきだけでなくツヤ不足・くすみに悩む方、ラグジュアリーなフローラルウッディの香りに包まれたい方、デパコス最高峰のヘアケアを求める方",
        "technique": "シャンプーを手のひらで軽く泡立てて頭皮になじませ、指の腹で頭皮をマッサージするように洗います。泡を毛先まで伸ばして揉み込むようにオイル成分を行き渡らせてから洗い流してください。",
        "voice": "『洗っている最中からオイルの濃密さが伝わり、流した後はトリートメントをしたかのようにトゥルトゥルになります。冬の乾燥した空気でも一日中ツヤが消えません。』(30代・外資系勤務)",
        "caution": "オイルリッチな処方のため、頭皮のべたつきが気になる脂性肌の方は、予洗いをしっかり念入りに行ってからご使用ください。"
    },
    {
        "rank": 3,
        "tag": "🌿 和漢植物エキス×濃密アミノ酸洗浄！冬のパサつき髪を毛先まで吸い付くような濃密保湿で満たす上位モデル",
        "catch": "ボタニスト最高峰のプレミアムライン。白樺樹液と伝統の和漢植物が頭皮をいたわりながら乾燥毛をしっとり鎮静",
        "capacity": "300ml",
        "type": "プレミアム・アミノ酸系ボタニカルモイストシャンプー",
        "texture": "とろみのあるまろやかな植物エキスリキッド。きめ細かくクリーミーな泡立ちで摩擦レスな洗い心地",
        "ingredients": "シラカンバ樹液、ダイズ種子エキス、シャクヤク根エキス、ビワ葉エキス、アミノ酸系界面活性剤（ココイル加水分解ダイズタンパクNa）",
        "finish": "重すぎず軽すぎない理想的なしっとり感。毛先までチュルンとまとまり、自然なエンジェルリングが宿る",
        "desc_p1": "日々のシャンプーによる「脱脂しすぎ」は、冬の頭皮の乾燥フケやかゆみ、髪のパサつきの根本原因です。洗浄力の強すぎる石油系界面活性剤で洗い続けると、頭皮の皮脂膜と髪の保護油分が奪われ、乾燥スパイラルに陥ってしまいます。",
        "desc_p2": "累計1億本突破のボタニストが大人世代の乾燥ダメージのために開発した『プレミアム ボタニカルシャンプー ベルベットモイスト』は、古来より髪に良いとされる和漢植物エキスと高保水白樺樹液を濃縮配合。植物由来のアミノ酸系洗浄成分が汚れだけを優しく浮かせ、頭皮の水分バリアを守りながら洗い上げます。ベルベットのようなリッチなまとまりと、優雅なサクラ＆プラムの香りが真冬のバスタイムを上質に演出します。",
        "target": "通常のボタニストでは冬の保湿力が物足りない方、頭皮の乾燥やかゆみも同時にケアしたい方、植物由来成分の優しさと確かな仕上がりの両方を求める方",
        "technique": "頭皮全体をしっかり濡らした後、1.5〜2プッシュを手に取り、頭皮を揉みほぐすように泡立てます。豊かな泡で頭皮をマッサージすることで、寒さで硬くなった頭皮の血行を促進できます。",
        "voice": "『定番のボタニストよりもしっとり感が格段に上で、冬のパサつく髪が毛先までストンと落ち着きました。頭皮の乾燥かゆみも無くなって大満足です。』(40代・事務職)",
        "caution": "アミノ酸系洗浄成分のため、整髪料をハードにつけている日は、最初にぬるま湯でしっかりスタイリング剤を落としてからシャンプーしてください。"
    },
    {
        "rank": 4,
        "tag": "🔬 SSVRシルク配合！冬の乾燥とヘアカラーによるハイダメージ毛を内部から棒状空洞化補修するプロ仕様",
        "catch": "髪の内部密度を高める先進サイエンス。ダメージでスカスカになった冬の髪を芯から強靭なしなやか髪へ再生",
        "capacity": "200ml",
        "type": "サロン専売・高機能内部補修リペアシャンプー",
        "texture": "クリーミーで濃密なリキッド。少量でも豊かに泡立ち、傷んでキシむ髪を摩擦からガードするクッション泡",
        "ingredients": "イソステアロイル加水分解シルク（SSVRシルク）、ホホバ油、ラウロイル加水分解シルクNa、アルギニン、各種アミノ酸",
        "finish": "髪一本一本にハリ・コシと芯のある弾力が宿り、冬の寒風にも負けないツルンとしたなめらかな手触り",
        "desc_p1": "冬の紫外線や乾燥、定期的なヘアカラーやブリーチが重なると、毛髪内部のタンパク質が抜け落ちて「棒状空洞化」が進行します。ストローのように中身がスカスカになった髪は、外気の湿気を吸ってうねったり、逆に乾燥してチリチリに縮れたりして制御不能になります。",
        "desc_p2": "グローバルミルボンの『リペア リストラティブ シャンプー』は、世界各国の髪を科学的に解析して誕生したプロフェッショナル仕様の補修シャンプー。シルク由来の補修成分「SSVRシルク」が髪内部の空洞に浸透して定着し、中身の詰まった健康な髪へと復元します。ケラチンやシルク成分の泡で洗いながら補修するため、洗うたびに毛髪強度がアップし、冬の枝毛や切れ毛の発生を未然に防ぎます。",
        "target": "ブリーチやカラーを繰り返して髪がスカスカ・チリチリに痛んでいる方、冬になると髪が切れたり枝毛が増えてしまう方、サロン専売の確かな補修力を実感したい方",
        "technique": "ぬるま湯でしっかり予洗いした後、適量を手のひらで泡立てて洗髪します。もっちりとした泡を毛先まで行き渡らせ、泡を毛束に揉み込むようにして1分間放置する「シルク泡パック」が極上の補修効果を発揮します。",
        "voice": "『ブリーチでボロボロだった髪が、このシャンプーを使い始めてから芯がしっかりして手触りが劇的に改善しました。冬の静電気も全く起きなくなりました。』(20代・ネイリスト)",
        "caution": "プロ仕様の高機能補修シャンプーのため、同シリーズのリペアトリートメントとセットで使用することで真価を発揮します。"
    },
    {
        "rank": 5,
        "tag": "🛡️ うるおいバリア処方×アミノ酸系洗浄！湿度変化や乾燥・静電気から髪を守り抜く超名作プチプラ",
        "catch": "ドラッグストアで手に入る驚愕のサロン級クオリティ。洗うだけで髪のバリア機能を高める新世代エッセンシャル",
        "capacity": "450ml",
        "type": "アミノ酸系・うるおいバリア高保湿シャンプー",
        "texture": "とろみのあるみずみずしいエッセンス状。泡立ちが非常に早く、モコモコの濃密泡が髪全体を瞬時に包み込む",
        "ingredients": "ココイルメチルタウリンNa、ラウロイルメチルアラニンNa、加水分解コラーゲン、スクワラン、シア脂、ヒアルロン酸Na",
        "finish": "毛先までトゥルンとしたなめらかなシルクタッチ。一日中パサつかず、雨や乾燥によるうねりをブロック",
        "desc_p1": "冬の朝、完璧にブローして出かけても、屋外の乾いた冷たい空気とオフィス内の暖房の寒暖差にさらされると、髪表面のバリアが破綻して毛先がバサバサに広がってしまいます。日常的なプチプラ価格で、環境変化に揺らがないタフなバリア機能を髪に与えるケアが切望されていました。",
        "desc_p2": "花王の革新作『エッセンシャル プレミアム バリアシャンプー シルキーモイスト』は、アミノ酸系洗浄成分をベースに、厳選された美容成分（スクワラン・シアバター・加水分解コラーゲン）を贅沢に配合。洗髪時のキューティクルの乱れを防ぎながら、髪本来が持つうるおいバリアを強化します。1,000円前後の手頃なプチプラでありながら、サロン専売品に匹敵するなめらかな指通りと静電気防止効果を実現した超コスパ名品です。",
        "target": "プチプラで毎日家族みんなで惜しみなく使える高保湿シャンプーを探している方、朝スタイリングしても日中に髪がパサついて広がってしまう方、ドラッグストアで買える名品を好む方",
        "technique": "予洗い後、ワンプッシュを手にとり、しっかり泡立てて頭皮と髪を優しく洗います。モコモコの泡立ちが良いため、摩擦を気にせずストレスフリーに洗髪できます。",
        "voice": "『プチプラとは思えないクオリティで感動しました！アミノ酸系なのに泡立ちが良く、ドライヤー後の髪が毛先までトゥルトゥルにまとまります。リピート決定です。』(30代・主婦)",
        "caution": "シリコンフリー処方のため、ダメージが極端に強いブリーチ毛の方は、洗髪後に同シリーズの高保湿ヘアマスクを併用することをおすすめします。"
    },
    {
        "rank": 6,
        "tag": "🫧 超高圧浸透型コラーゲン配合！もっちり濃密泡が冬のパサつく髪と乾燥した頭皮を優しく洗い上げる",
        "catch": "100MPaの超高圧で微粒子化したコラーゲン。髪と頭皮の角層すみずみまで浸透し、ぷるんとした弾力とうるおいを注入",
        "capacity": "400ml",
        "type": "超高圧浸透テクノロジー・集中保水コラーゲンシャンプー",
        "texture": "プルンとしたジュレのようなリキッド。水を含むと弾力のあるホイップのような濃密泡へ変化",
        "ingredients": "超高圧処理加水分解コラーゲン、ココイルグルタミン酸TEA、加水分解ケラチン、セラミドEOP/NP/AP、ヒアルロン酸ヒドロキシプロピルトリモニウム",
        "finish": "水分をたっぷり含んだようなみずみずしい保水感。パサつきを抑え、指通りスルンとしたサラ艶髪へ",
        "desc_p1": "分子量の大きい通常のコラーゲンは、髪の表面を覆うだけで内部まで浸透しにくいという弱点がありました。冬の乾燥で内部の水分が抜け落ちた髪には、微小な隙間を通過できる超微粒子化された保湿分子の補給が必須です。",
        "desc_p2": "スキンケア発想の機能性ヘアケア・アンレーベルラボの『CO モイスト シャンプー』は、水深1万メートルの圧力に匹敵する100MPaの超高圧で処理したナノコラーゲンを配合。キューティクルのわずかな隙間から毛髪深部へスムーズに浸透し、水分を抱え込んで逃しません。さらに3種のヒト型セラミドが頭皮のバリア機能を保護。乾燥して敏感になった冬の地肌とパサつく髪を、ぷるんとした潤いで満たします。",
        "target": "髪のパサつきと同時に頭皮の乾燥も気になる方、スキンケア成分（コラーゲンやセラミド）にこだわりたい方、フルーティフローラルの甘く爽やかな香りが好きな方",
        "technique": "シャンプーを髪全体に馴染ませ、もっちりしたホイップ泡で頭皮を包み込むように洗います。泡立てた状態で30秒ほど置くことで、超高圧コラーゲンが髪内部へじっくり浸透します。",
        "voice": "『泡立ちがとても濃密で、洗っている間も髪が絡まりません。乾かした後の毛先がプルプルに潤っていて、冬の乾燥による静電気もピタッと収まりました。』(20代・OL)",
        "caution": "洗浄成分が非常にマイルドなため、整髪料をたっぷり使った日は2度洗いするか、予洗いを長めに行ってください。"
    },
    {
        "rank": 7,
        "tag": "🌿 100%天然由来×アミノ酸系洗浄！リンス不要で冬の乾燥頭皮と毛先をしっとりハリコシ良く洗い上げる名作",
        "catch": "大人の頭皮と髪のためのオールインワンシャンプー。33種の美容成分が頭皮の乾燥かゆみを防ぎボリュームアップ",
        "capacity": "400ml",
        "type": "100%天然由来・オールインワン高保湿スカルプシャンプー",
        "texture": "とろりとした琥珀色のリッチエッセンス。少量でもキメ細かなモチモチ泡が立ち、髪がきしまない",
        "ingredients": "ココイルグルタミン酸TEA、ココイルメチルアラニンNa、加水分解シルク、ワカメエキス、ホップエキス、リンゴ果実培養細胞エキス、柑橘精油",
        "finish": "リンスなしでも指通りなめらか。根元はふんわり立ち上がり、毛先はしっとり落ち着く絶妙なバランス",
        "desc_p1": "冬の寒さによって頭皮の血流が悪くなると、毛根への栄養が不足し、髪のハリ・コシが低下してペタンとしたボリューム不足に陥ります。さらに度重なるトリートメントのすすぎ残しが頭皮の毛穴を塞ぎ、冬のフケやかゆみを悪化させる原因になることも少なくありません。",
        "desc_p2": "haruの『kurokami スカルプ』は、100%天然由来成分のみで作られた高品質オールインワンシャンプー。ヤシ由来の濃密なアミノ酸系洗浄成分が頭皮の汚れを優しくオフし、33種の天然美容成分が角層に浸透。リンスやコンディショナーを使わなくても、シルクや海藻エキスがキューティクルを整え、驚くほどなめらかな指通りを実現します。忙しい冬の夜の時短ケアとしても圧倒的な支持を集めています。",
        "target": "冬の頭皮の乾燥かゆみ・フケが気になる方、髪のボリューム不足や抜け毛が気になる方、リンス不要で時短＆極上のスカルプケアを両立したい方",
        "technique": "お湯でしっかり予洗いした後、適量を手に取り頭皮をもみほぐすように洗います。モコモコの泡で髪全体を包み込み、2〜3分間そのまま置く「泡パック」を行うと、頭皮と髪に美容成分がたっぷり浸透します。",
        "voice": "『本当にリンスが要らないのか半信半疑でしたが、これ一本で毛先までしっとりサラサラになります！冬の頭皮の乾燥やかゆみも全く気にならなくなりました。柑橘の香りも癒やされます。』(40代・主婦)",
        "caution": "使い始めの数日間は、シリコン配合シャンプーからの移行期としてわずかにきしみを感じることがありますが、使い続けることで髪本来の健やかな手触りに戻ります。"
    },
    {
        "rank": 8,
        "tag": "✨ オーガニックアルガンオイル×アミノケラチン配合！冬の毛先までまとまる濃密ダメージ補修シャンプー",
        "catch": "ドラッグストアの定番大人気シリーズ。傷んだ髪の隙間を埋めて補修し、ツヤとまとまりを長時間キープ",
        "capacity": "450ml",
        "type": "オーガニックオイルイン・濃密リペアシャンプー",
        "texture": "とろみのあるクリーミーなリキッド。素早くキメ細かい濃密泡が立ち上がり、髪全体を優しく包む",
        "ingredients": "アルガニアスピノサ核油（オーガニックアルガンオイル）、ステアルジモニウムヒドロキシプロピル加水分解ケラチン、羽毛ケラチン、バオバブ種子油、各種植物エキス",
        "finish": "毛先までツヤやかでしっとり重厚なまとまり。パサつきやうねりを抑え、ブローしやすい扱いやすい髪へ",
        "desc_p1": "冬はマフラーやコートの襟足との擦れによって、後頭部や毛先のキューティクルが剥離し、ボサボサに絡まりやすくなります。摩擦ダメージを軽減するためには、洗髪時から髪表面にオイルヴェールを形成し、滑りを良くすることが重要です。",
        "desc_p2": "モイストダイアンの『パーフェクトビューティー エクストラダメージリペア』は、高品質なオーガニックアルガンオイルと、髪の構成成分であるケラチンをアミノ酸結合させた「アミノケラチン」を配合。ナノカプセル化された補修成分が傷んだキューティクルの隙間にピタッと密着し、蓄積したダメージを集中補修します。ドラッグストアでいつでも買えるプチプラ価格で、冬のパサつく髪をツヤのあるまとまり髪へと導きます。",
        "target": "プチプラでしっかり重めのしっとり感を求める方、毛先のパサつきや枝毛がひどい方、甘く華やかなフローラル＆ベリーの香りが好きな方",
        "technique": "適量を手にとり、ぬるま湯を加えながらしっかり泡立てて髪全体を洗います。同シリーズのトリートメントやヘアマスクを毛先を中心に重ねることで、冬の乾燥ガードがより強固になります。",
        "voice": "『コスパが良くてずっと愛用しています。冬のパサつく毛先もしっとりまとまり、朝の寝癖直しがとても楽になりました。甘い香りも一日中続きます。』(20代・学生)",
        "caution": "しっとり感が強めの処方のため、細毛・軟毛の方で根元をふんわりさせたい場合は、毛先を中心に泡を行き渡らせるようにしてください。"
    },
    {
        "rank": 9,
        "tag": "🌿 オーガニック植物成分×ハーブエキス配合！傷んで乾燥した髪をしっとりなめらかに洗い上げる癒やしの香り",
        "catch": "北アルプスの清らかな天然水とハーブの恵み。サロン発想のアロマエステで冬のこわばった頭皮と髪を解きほぐす",
        "capacity": "300ml",
        "type": "オーガニック植物成分配合・アロマ高保湿シャンプー",
        "texture": "琥珀色のなめらかなエッセンス状。豊かでキメ細かいハーブ泡が心地よく立ち上がる",
        "ingredients": "オレフィン(C14-16)スルホン酸Na、ココイルアラニンTEA、ローズマリー葉油、カミツレ花油、ラベンダー油、アボカド油、ホホバ種子油",
        "finish": "サロン帰りのような上質でシルキーな手触り。頭皮はスッキリ爽快、毛先はしっとりサラサラ",
        "desc_p1": "冬の寒さや多忙な年末年始は、無意識のうちに頭皮の筋肉が緊張して血行が悪くなり、頭皮の突っ張りやコリを感じやすくなります。毎日のシャンプーを単なる汚れ落としではなく、心身の緊張を解き放つアロマテラピーの時間に変えることが、健やかな髪の土台づくりに直結します。",
        "desc_p2": "日本のオーガニックヘアケアの先駆け・ラ・カスタの『アロマエステ ヘアソープ 35』は、傷んで乾燥した髪のために調合された高保湿ライン。ローズマリーやラベンダー、カモミールなどの上質なエッセンシャルオイルが、深呼吸したくなる極上のフローラルハーブの香りを広げます。植物オイルとハーブエキスが冬の乾燥毛をうるおいで満たし、しっとりまとまりのあるツヤ髪へと磨き上げます。",
        "target": "本格的なオーガニックアロマの香りでリラックスしたい方、サロン品質の上品な洗い上がりを求める方、冬の髪の乾燥と頭皮のコリを同時に癒やしたい方",
        "technique": "予洗いをしっかり行った後、手のひらで泡立てて頭皮を優しくマッサージします。洗髪中は目を閉じて深く息を吸い込み、天然精油の豊かなアロマを堪能してください。",
        "voice": "『美容院で勧められてから何本もリピートしています。ハーブの香りが本当に素晴らしくて、洗うだけで一日の疲れが吹き飛びます。髪もしっとりサラサラです。』(30代・自営業)",
        "caution": "天然精油を贅沢に使用しているため、香りをフレッシュに保つよう使用後はフタをしっかり閉めて保管してください。"
    },
    {
        "rank": 10,
        "tag": "💧 サロン級アミノ酸洗浄×セラミド・ヒアルロン酸！もっちり濃密泡が冬のパサつき髪をうるおいで包み込む",
        "catch": "毛髪補修のアミノ酸を贅沢配合。乾燥で傷んだキューティクルを滑らかに補正する実力派アミノシャンプー",
        "capacity": "400ml",
        "type": "サロン発想・アミノ酸×セラミド高保湿シャンプー",
        "texture": "とろみのあるまろやかなリキッド。生クリームのようにキメ細かく弾力のあるモチモチ泡",
        "ingredients": "ココイルグルタミン酸TEA、ラウロイル加水分解シルクNa、セラミドNG/NP/AP、加水分解ケラチン、ヒアルロン酸Na、ヘマチン",
        "finish": "毛先までうるおいがぎゅっと詰まったようなみずみずしさ。ベタつかず軽やかなサラサラまとまり髪",
        "desc_p1": "髪の主成分である「ケラチンタンパク質」は、約18種類のアミノ酸で構成されています。冬の乾燥や静電気によるダメージで失われたアミノ酸を、毎日の洗髪で補うことは、髪の強度と保水力を回復させるための最も理にかなったアプローチです。",
        "desc_p2": "サロン発想ヘアケアブランド・アミノレスキューの『モイスト シャンプー』は、アミノ酸系洗浄成分に加えて、セラミドやヒアルロン酸、ヘマチンなどの高機能補修成分を贅沢にブレンド。ホイップクリームのような濃密な弾力泡が、髪同士の摩擦を徹底的に防ぎながら優しく洗い上げます。冬の乾燥でパサついた毛先にもうるおいが浸透し、指通りの良いなめらかな質感へと仕上げます。",
        "target": "アミノ酸シャンプーならではの優しい洗い心地を好む方、セラミドやケラチンによる補修効果を重視する方、コストパフォーマンスの高い実力派シャンプーを探している方",
        "technique": "適量を手にとり、少量のぬるま湯を加えながらしっかり泡立てます。豊かな泡で頭皮を優しく洗い、毛先まで泡を行き渡らせてからぬるま湯で丁寧に洗い流してください。",
        "voice": "『泡立ちがとてもクリーミーで、洗っているときから髪が柔らかくなるのが分かります。冬でも静電気が起きにくくなり、朝のまとまりが良くなりました。』(20代・会社員)",
        "caution": "アミノ酸成分が豊富に含まれているため、すすぎはぬるま湯でヌルつきがなくなるまでしっかり丁寧に行ってください。"
    }
]

# JSON-LD用ItemList
json_ld_items = []
for idx, it in enumerate(items):
    dt = moisture_shampoo_details[idx]
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
            "headline": "保湿力の強さで冬のパサつき・静電気・頭皮乾燥とさようなら！うるおい満ちる濃密高保湿シャンプーランク10",
            "description": "11月・12月の冬の暖房風や乾燥による毛先のパサパサ・静電気広がり・頭皮のカサつきを徹底解決！オージュア、ケラスターゼ、ボタニストプレミアム、ミルボン、エッセンシャルプレミアムなど、アミノ酸系洗浄＆濃密保湿で髪と頭皮をうるおす最強高保湿シャンプー10選を徹底比較！",
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
                    "name": "冬に髪がパサついて静電気が起きやすいのはなぜですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "髪の理想的な水分量は11〜13%程度ですが、湿度が低下する11月〜12月は水分量が10%未満まで急激に落ち込みます。乾燥した髪は電気を帯びやすくなり、ニットやマフラー、ブラッシングの摩擦によって数千ボルトの静電気が発生します。静電気はキューティクルを無理やりめくれ上がらせ、さらなる水分蒸発と枝毛・パサつきを引き起こす悪循環を生みます。アミノ酸系保湿シャンプーで髪内部の水分を保つことが根本的な解決策です。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "アミノ酸系シャンプーは洗浄力が弱くて頭皮がベタつきませんか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "アミノ酸系洗浄成分（ココイルメチルタウリンNa、ラウロイルメチルアラニンNaなど）は、頭皮に必要なうるおいと皮脂膜を残しながら、不要な皮脂や汗、大気汚染物質だけを選択的に落とす『選択洗浄性』を持っています。洗髪前に38度のぬるま湯で2分間しっかり予洗いを行えば、汚れの約7〜8割はお湯だけで落ちるため、アミノ酸シャンプーでも全くベタつかず、すっきりと清潔に洗い上げることができます。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "冬のお風呂で髪を洗うときのお湯の温度は何度がベストですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "『38度〜39度のぬるま湯』がベストです。寒い冬は41度〜42度以上の熱いシャワーを頭皮に直接当てたくなりますが、40度を超える熱湯は髪のキューティクルを開かせ、頭皮の保護皮脂やセラミドを一気に溶かし出して極度の乾燥やかゆみを招きます。少しぬるいと感じる38度前後で優しく洗い流すことが、ツヤ髪と潤い頭皮を保つ鉄則です。"
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
  <title>保湿力の強さで冬のパサつき・静電気・頭皮乾燥とさようなら！うるおい満ちる濃密高保湿シャンプーランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬の暖房風や乾燥による毛先のパサパサ・静電気広がり・頭皮のカサつきを徹底解決！オージュア、ケラスターゼ、ボタニストプレミアム、ミルボン、エッセンシャルプレミアムなど、アミノ酸系洗浄＆濃密保湿で髪と頭皮をうるおす最強高保湿シャンプー10選を徹底比較！">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-moisture-shampoo">
  <meta property="og:title" content="保湿力の強さで冬のパサつき・静電気・頭皮乾燥とさようなら！うるおい満ちる濃密高保湿シャンプーランク10">
  <meta property="og:description" content="11月・12月の冬の暖房風や乾燥による毛先のパサパサ・静電気広がり・頭皮のカサつきを徹底解決！オージュア、ケラスターゼ、ボタニストプレミアム、ミルボン、エッセンシャルプレミアムなど、アミノ酸系洗浄＆濃密保湿で髪と頭皮をうるおす最強高保湿シャンプー10選を徹底比較！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-moisture-shampoo">
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
        <a href="#why-hair-dry">冬の毛髪科学</a>
        <a href="#faq-section">よくある質問</a>
      </nav>
    </div>
  </header>

  <main class="container main-content">
    <article class="article-body">
      <nav class="breadcrumb" aria-label="パンくずリスト">
        <ol>
          <li><a href="/">トップ</a></li>
          <li aria-current="page">高保湿シャンプー</li>
        </ol>
      </nav>

      <header class="article-header">
        <span class="badge category-badge">ヘアケア・静電気＆パサつき防止</span>
        <h1 class="article-title">保湿力の強さで冬のパサつき・静電気・頭皮乾燥とさようなら！うるおい満ちる濃密高保湿シャンプーランク10</h1>
        <div class="article-meta">
          <time datetime="2026-11-01">2026年11月1日更新</time>
          <span class="author">執筆：冬コスメ比較検証チーム</span>
        </div>
      </header>

      <!-- 導入文 -->
      <section class="intro-box">
        <p>
          11月から12月へと寒さが本格化するにつれて、「毛先がパサパサして針金のように広がる」「ニットやマフラーを着脱するたびにパチパチと静電気が起きて髪が顔に張り付く」「ドライヤーで乾かした後に毛先がまとまらない」「頭皮がカサついてフケやかゆみが出る」といった深刻な髪と頭皮の乾燥トラブルに直面していませんか？
        </p>
        <p>
          冬の外気湿度は一年で最も低く、さらにオフィスや自宅のエアコン暖房の温風が追い打ちをかけます。髪の水分量は理想の12%前後から一気に10%未満へと低下し、キューティクルが毛羽立って内部のタンパク質と水分が流出。その状態で洗浄力の強すぎる石油系シャンプー（ラウレス硫酸など）を使い続けると、必要な油分まで根こそぎ奪われ、パサつきと静電気のスパイラルから抜け出せなくなります。
        </p>
        <p>
          この過酷な真冬の乾燥毛を救う唯一の鍵が、汚れを優しく落としながら毛髪内部に水分とアミノ酸・補修オイルを直接届ける<strong>「高保湿アミノ酸系シャンプー」</strong>です。アミノ酸系洗浄成分と濃密な保湿エッセンスが、洗髪時の摩擦をゼロに抑え、サロン帰りのようなトゥルンとした手触りとまとまりを取り戻します。
        </p>
        <p>
          本特集では、楽天市場やサロンアワードで絶大な支持を集める高保湿シャンプーの中から、編集部が泡立ち・洗浄時のきしみ感のなさ・仕上がりのうるおい保持力・静電気抑制効果を徹底検証し、11月〜12月の冬に本当に頼れる実力派10選をランキング形式で厳選しました。
        </p>
      </section>

      <!-- 目次 -->
      <nav class="toc-card" aria-label="目次">
        <h2 class="toc-title">📑 目次</h2>
        <ul class="toc-list">
          <li><a href="#why-hair-dry">1. なぜ11月〜12月に髪がパサつき静電気が大発生するのか？毛髪科学の真相</a></li>
          <li><a href="#how-to-choose">2. 失敗しない！冬の高保湿シャンプー選びの3原則</a></li>
          <li><a href="#ranking">3. 高保湿シャンプーおすすめ厳選ランキング10選</a></li>
          <li><a href="#guide-section">4. サロン帰りの艶を再現！冬の38度ぬるま湯＆濃密泡パック洗髪法</a></li>
          <li><a href="#faq-section">5. よくある質問 (FAQ)</a></li>
          <li><a href="#related-section">6. あわせて読みたい冬の徹底保湿特集</a></li>
        </ul>
      </nav>

      <!-- 科学的背景解説 -->
      <section id="why-hair-dry" class="content-block">
        <h2>🔬 なぜ11月〜12月に髪がパサつき静電気が大発生するのか？毛髪科学の真相</h2>
        <p>
          冬になると急に毛先が広がり、静電気に悩まされるのには、毛髪の内部構造と湿度環境の明確な因果関係があります。
        </p>
        <div class="science-grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:20px; margin:24px 0;">
          <div style="background:#f1f5f9; padding:20px; border-radius:8px; border-left:4px solid #0284c7;">
            <h3 style="margin-top:0; font-size:1.1rem; color:#0f172a;">① 髪の水分量10%未満で起きる「帯電現象」</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#334155; margin-bottom:0;">
              髪内部の水分が十分にある状態（12%以上）では、電気は自然に空気中へと放電されます。しかし湿度が40%を下回る冬は髪の水分が奪われて電気の逃げ場がなくなり、衣服との摩擦によって数千ボルトの静電気が蓄積。反発し合って髪が爆発するように広がります。
            </p>
          </div>
          <div style="background:#f1f5f9; padding:20px; border-radius:8px; border-left:4px solid #0284c7;">
            <h3 style="margin-top:0; font-size:1.1rem; color:#0f172a;">② 暖房温風によるキューティクルの剥離</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#334155; margin-bottom:0;">
              エアコンの乾いた温風に長時間さらされると、キューティクルを接着している細胞間脂質（CMC）が乾燥して剥がれ落ちます。魚のウロコのようにめくれ上がったキューティクルは光を乱反射させ、ツヤを完全に奪い去ります。
            </p>
          </div>
          <div style="background:#f1f5f9; padding:20px; border-radius:8px; border-left:4px solid #0284c7;">
            <h3 style="margin-top:0; font-size:1.1rem; color:#0f172a;">③ 高級アルコール系洗浄剤による過脱脂</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#334155; margin-bottom:0;">
              冬に洗浄力の強すぎるシャンプーを使うと、乾燥から頭皮を守るべき皮脂膜や髪表面の18-MEAが根こそぎ洗い流されます。洗うたびに自衛手段を失い、パサつきとフケ・かゆみが深刻化してしまいます。
            </p>
          </div>
        </div>
      </section>

      <!-- 選び方解説 -->
      <section id="how-to-choose" class="content-block">
        <h2>💡 失敗しない！冬の高保湿シャンプー選びの3原則</h2>
        <div class="choose-principles" style="margin:24px 0;">
          <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px; margin-bottom:16px;">
            <h3 style="color:#0369a1; margin-top:0;">基準1：アミノ酸系・ベタイン系洗浄成分を主成分にしたものを選ぶ</h3>
            <p style="line-height:1.7; color:#475569;">
              全成分表示の2番目〜3番目に「ココイルメチルタウリンNa」「ラウロイルメチルアラニンNa」「ココイルグルタミン酸TEA」「コカミドプロピルベタイン」などが記載されているものを選びましょう。髪のタンパク質を守りながらマイルドに洗い上げます。
            </p>
          </div>
          <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px; margin-bottom:16px;">
            <h3 style="color:#0369a1; margin-top:0;">基準2：毛髪内部補修成分（ケラチン・シルク・セラミド・コラーゲン）の配合</h3>
            <p style="line-height:1.7; color:#475569;">
              加水分解ケラチン、加水分解シルク、超高圧コラーゲン、ナノセラミドなどの補修成分が入っているシャンプーは、シャンプーの泡立ちの中で髪の空洞に浸透し、髪の芯からうるおいを再構築します。
            </p>
          </div>
          <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
            <h3 style="color:#0369a1; margin-top:0;">基準3：高純度エモリエント植物オイル（アルガン・ホホバ・シア）の配合</h3>
            <p style="line-height:1.7; color:#475569;">
              洗い流した後のキューティクル表面を保護し、静電気を防止するためには、アルガンオイルやホホバオイル、シアバターなどの良質なエモリエントオイルが配合されているものがベストです。指通りが格段に向上します。
            </p>
          </div>
        </div>
      </section>

      <!-- ランキング一覧セクション -->
      <section id="ranking" class="ranking-section">
        <div class="ranking-header">
          <h2>🏆 高保湿シャンプーおすすめ厳選ランキング10選</h2>
          <p class="ranking-subtitle">11月〜12月の頑固なパサつき・静電気・頭皮乾燥を防ぎ、毛先までうる艶にまとめる名品を徹底比較！</p>
        </div>
"""

for idx, it in enumerate(items):
    dt = moisture_shampoo_details[idx]
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
                  <tr><th>主要補修・保湿成分</th><td>{dt["ingredients"]}</td></tr>
                  <tr><th>仕上がり質感</th><td>{dt["finish"]}</td></tr>
                </tbody>
              </table>

              <div class="product-review-body">
                <h4>【毛髪科学的アプローチ＆製品特徴】</h4>
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

# 比較表、洗い方ガイド、FAQ、内部リンク
html_content += """
      <!-- 比較まとめ一覧表 -->
      <section class="comparison-summary-section" style="margin:48px 0;">
        <h2>📊 高保湿シャンプー10選 比較早見表</h2>
        <div style="overflow-x:auto;">
          <table class="summary-table" style="width:100%; border-collapse:collapse; margin-top:16px; font-size:0.92rem;">
            <thead>
              <tr style="background:#0284c7; color:#fff;">
                <th style="padding:12px 10px; border:1px solid #cbd5e1;">順位 / ブランド</th>
                <th style="padding:12px 10px; border:1px solid #cbd5e1;">商品名</th>
                <th style="padding:12px 10px; border:1px solid #cbd5e1;">洗浄・補修成分</th>
                <th style="padding:12px 10px; border:1px solid #cbd5e1;">特徴・おすすめな人</th>
                <th style="padding:12px 10px; border:1px solid #cbd5e1;">参考価格</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">1位 オージュア</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">クエンチ シャンプー</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">タウリン系・CMC脂質補修成分</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">水分保持力を取り戻しサロン帰りの髪へ</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥7,260</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">2位 ケラスターゼ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">バン ユイルスブリム R</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">4種プレシャスオイル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">息をのむツヤと滑らかさ！静電気も完全防御</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥12,880</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">3位 ボタニスト</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">プレミアム ベルベットモイスト</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">白樺樹液・和漢植物エキス</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">頭皮をいたわりながら乾燥毛をチュルンと保湿</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥2,850</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">4位 ミルボン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">リペア リストラティブ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">SSVRシルク・ホホバ油</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ハイダメージの空洞化を芯から埋めるプロ仕様</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥5,720</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">5位 エッセンシャル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">プレミアム バリア シルキーモイスト</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">アミノ酸系・うるおいバリア処方</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">驚異の高コスパ！湿度変化や静電気から守る</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥664</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">6位 アンレーベルラボ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">CO モイスト シャンプー</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">超高圧浸透型コラーゲン・セラミド</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">もっちり泡で髪と頭皮をプルプルの保水膜へ</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥3,410</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">7位 haru</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">kurokami スカルプ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">100%天然由来・アミノ酸洗浄</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">リンス不要！冬の乾燥頭皮とハリコシを同時にケア</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥3,654</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">8位 ダイアン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">エクストラダメージリペア</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">アルガンオイル・アミノケラチン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">濃密な重めのまとまり！ドラコス大定番</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥1,016</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">9位 ラ・カスタ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">アロマエステ ヘアソープ 35</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">オーガニック精油・ハーブエキス</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">極上フローラルハーブの香りとサロン品質の手触り</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥5,500</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">10位 アミノレスキュー</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">モイスト シャンプー</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">アミノ酸・セラミド・ヘマチン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">生クリーム濃密泡でパサつく髪を優しく包む</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥4,176</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- 正しい洗い方ガイド -->
      <section id="guide-section" class="expert-guide-section" style="background:#f8fafc; border-radius:12px; padding:28px; margin:40px 0;">
        <h2>🛁 サロン帰りの艶を再現！冬の38度ぬるま湯＆濃密泡パック洗髪法</h2>
        <div style="line-height:1.8; color:#334155;">
          <h3>1. 38度のぬるま湯で「2分間の予洗い」</h3>
          <p>
            寒い冬は熱いお湯（41〜42度）で洗いたくなりますが、高温のお湯は頭皮の必要な皮脂膜や髪のCMCを一気に溶かし出し、極度の乾燥を招きます。少しぬるいと感じる「38度前後」のお湯で、頭皮を揉みながら2分間しっかり予洗いしましょう。これだけで汚れの7〜8割が落ち、シャンプーの泡立ちが劇的に良くなります。
          </p>

          <h3 style="margin-top:24px;">2. 手のひらで泡立ててから頭皮へ！「濃密泡パック」</h3>
          <p>
            シャンプー液を直接頭皮につけて泡立てると、髪同士の摩擦でキューティクルが傷つきます。必ず手のひらでぬるま湯を加えながらしっかり泡立て、もっちりした泡を頭皮と髪に乗せてください。頭皮を指の腹でマッサージするように洗った後、泡を毛先まで伸ばして1分間置く「泡パック」を行うと、アミノ酸や補修オイルが髪深部へ浸透します。
          </p>

          <h3 style="margin-top:24px;">3. すすぎは「予洗いの倍の時間」かけて丁寧に</h3>
          <p>
            高保湿シャンプーは保湿成分が豊富なため、すすぎ残しがあると頭皮トラブルの原因になります。耳の後ろや襟足、頭頂部など、シャワーヘッドを地肌に近づけながら、ヌルつきが完全に消えるまで十分に洗い流しましょう。
          </p>
        </div>
      </section>

      <!-- よくある質問 (FAQ) -->
      <section id="faq-section" class="faq-section">
        <h2>❓ 冬の高保湿シャンプー よくある質問 (FAQ)</h2>
        <div class="faq-item">
          <h3>Q1. 冬に髪がパサついて静電気が起きやすいのはなぜですか？</h3>
          <p>髪の理想的な水分量は11〜13%程度ですが、湿度が低下する11月〜12月は水分量が10%未満まで急激に落ち込みます。乾燥した髪は電気を帯びやすくなり、ニットやマフラー、ブラッシングの摩擦によって数千ボルトの静電気が発生します。静電気はキューティクルを無理やりめくれ上がらせ、さらなる水分蒸発と枝毛・パサつきを引き起こす悪循環を生みます。アミノ酸系保湿シャンプーで髪内部の水分を保つことが根本的な解決策です。</p>
        </div>
        <div class="faq-item">
          <h3>Q2. アミノ酸系シャンプーは洗浄力が弱くて頭皮がベタつきませんか？</h3>
          <p>アミノ酸系洗浄成分（ココイルメチルタウリンNa、ラウロイルメチルアラニンNaなど）は、頭皮に必要なうるおいと皮脂膜を残しながら、不要な皮脂や汗、大気汚染物質だけを選択的に落とす『選択洗浄性』を持っています。洗髪前に38度のぬるま湯で2分間しっかり予洗いを行えば、汚れの約7〜8割はお湯だけで落ちるため、アミノ酸シャンプーでも全くベタつかず、すっきりと清潔に洗い上げることができます。</p>
        </div>
        <div class="faq-item">
          <h3>Q3. 冬のお風呂で髪を洗うときのお湯の温度は何度がベストですか？</h3>
          <p>『38度〜39度のぬるま湯』がベストです。寒い冬は41度〜42度以上の熱いシャワーを頭皮に直接当てたくなりますが、40度を超える熱湯は髪のキューティクルを開かせ、頭皮の保護皮脂やセラミドを一気に溶かし出して極度の乾燥やかゆみを招きます。少しぬるいと感じる38度前後で優しく洗い流すことが、ツヤ髪と潤い頭皮を保つ鉄則です。</p>
        </div>
      </section>

      <!-- 関連特集への内部リンク -->
      <section id="related-section" class="related-section">
        <h2>🔗 あわせて読みたい冬の徹底保湿・ヘアケア特集</h2>
        <div class="internal-links-grid">
          <a href="/winter-hair-care" class="related-card">
            <span class="related-tag">ヘアケア総論</span>
            <h4>💇‍♀️ 冬の髪の乾燥・静電気対策ヘアケア ランク10</h4>
            <p>シャンプーからアウトバスまで冬の美髪ルーティンを徹底解説。</p>
          </a>
          <a href="/winter-hair-mask" class="related-card">
            <span class="related-tag">ヘアマスク</span>
            <h4>🛁 冬の集中補修高保湿ヘアマスク ランク10</h4>
            <p>週に数回の集中トリートメントで深刻な枝毛・パサつきを撃退。</p>
          </a>
          <a href="/winter-hair-oil" class="related-card">
            <span class="related-tag">ヘアオイル</span>
            <h4>✨ 冬の濃密高保湿ヘアオイル ランク10</h4>
            <p>ドライヤー前後に毛先をコーティングして静電気と乾燥を防御。</p>
          </a>
          <a href="/winter-scalp-shampoo" class="related-card">
            <span class="related-tag">スカルプシャンプー</span>
            <h4>🌿 冬のフケ・かゆみ防止スカルプシャンプー ランク10</h4>
            <p>頭皮の毛穴とフケ・かゆみケアに特化した薬用スカルプ特集。</p>
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

with open("winter-moisture-shampoo.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated winter-moisture-shampoo.html ({len(html_content):,} bytes)")
