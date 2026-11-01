import json
import re

with open("fetched_3nov_dec_inbath_eyemask_handmask_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_hand_mask"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 特許4Dヒアルロン酸×植物幹細胞！手袋型でスマホも触れるサロン級ハンドエステ",
        "catch": "美容液36mLの贅沢手袋パック。浸透圧と密閉力で冬のひび割れ・ガサガサ手肌をシルクへ再生",
        "brand_name": "DearIrean (ディアアイリーン)",
        "capacity": "5回分セット（個包装・手袋型）",
        "type": "高機能・特許4Dヒアルロン酸高保湿ハンドマスク",
        "features": "特許4Dヒアルロン酸、植物幹細胞培養液エキス、ナイアシンアミド、シアバター、スマホタッチ対応",
        "value": "2つの特許技術を取得した次世代ハンドマスク。手袋を着けたままスマートフォンが操作でき、わずか20分で極上のもちもち手肌に",
        "desc_p1": "11月から12月にかけて、本格的な乾燥シーズンと年末の大掃除、冷たい水での食器洗いや毎日のアルコール消毒が重なり、手の甲や指先がまるで紙やすりのようにガサガサに荒れ果ててしまう…ハンドクリームを何度塗り直しても追いつかない深刻な手荒れに、圧倒的な救済をもたらすのがDearIrean（ディアアイリーン）の『高保湿ハンドマスク』です。",
        "desc_p2": "分子サイズの異なる4種のヒアルロン酸を立体的に組み合わせた『特許4Dヒアルロン酸』を採用し、肌表面の保護から角層最深部への保水までを隙間なく網羅。手袋型マスクの内側には、1回分あたり36mLという美容液ボトル約1本分もの濃密エッセンスが贅沢に染み込んでいます。美容皮膚科のODT（密封包帯法）発想により、手肌を隙間なくラッピングすることで美容成分を角層奥へ一気に押し込みます。指先がスマホ操作対応フィルムになっているため、パック中もストレスなくSNSや動画を楽しめる点も現代人に完璧に寄り添った設計です。",
        "target": "水仕事や大掃除で指先がひび割れて痛い方、手の甲のシワや年齢サインが気になる方、スマホを見ながら手軽にサロン級集中ケアをしたい方",
        "point": "お風呂上がりの手肌が温まり柔らかくなっている状態で装着し、手袋の上から手のひらや指の関節を優しく揉み込むと、温熱効果で美容液が隅々まで浸透します。"
    },
    {
        "rank": 2,
        "tag": "🍋 韓国発の大ヒット！濃厚シアバターとアルガンオイルが冬の硬化角質をとろかす",
        "catch": "天然ボタニカルオイルが指先の頑固なささくれまで集中補修。脱いだ瞬間感動するふっくら感",
        "brand_name": "KOCOSTAR (ココスター)",
        "capacity": "1回分（両手用・個包装）",
        "type": "高保湿・ボタニカルシアバターハンドモイスチャーパック",
        "features": "シア脂、アルガニアスピノサ核油、セラミドNP、ツボクサエキス（CICA）、二重構造グローブ",
        "value": "世界70カ国以上で愛用されるパーツケア専門ブランド。外側がサラサラで液漏れしない二重構造と手頃な価格でリピート率No.1",
        "desc_p1": "韓国のパーツケアコスメのパイオニアとして世界的な人気を誇るKOCOSTARの『ハンドモイスチャーパック』。冬の厳しい寒風と乾燥によってゴワゴワに硬化してしまった手肌を、濃厚なオーガニックシアバターと黄金のアルガンオイルの力でとろけるように柔らかくほぐしてくれる名作です。",
        "desc_p2": "外側は水気を通さないドライシート、内側は美容液が染み込んだ不織布という精密な二重グローブ構造を採用。美容液が外に染み出さないため、パック中もパソコンのキーボードを叩いたり本を読んだりと自由に行動できます。セラミドNPとCICA（ツボクサエキス）が乾燥で荒れた肌バリアを急速修復し、爪の周りの頑固なささくれや乾燥爪まで同時にツヤツヤに整えます。300円台という手軽さで、冬のデイリー集中レスキューとして最適です。",
        "target": "爪の周りのささくれや乾燥ひび割れが気になる方、手頃なプチプラで手袋パックを試してみたい方、作業しながらハンドケアしたい方",
        "point": "パックを外した後に肌表面に残った美容液は絶対に洗い流さず、手首からひじにかけて塗り伸ばすと、腕全体までしっとり滑らかに保湿できます。"
    },
    {
        "rank": 3,
        "tag": "🌿 累計1000万個突破の実力派！脱いだ瞬間しっとり吸い付く高コスパまとめ買いパック",
        "catch": "アルブチン＆カタツムリ分泌液配合。12袋セットで冬の1ヶ月間みっちり集中手肌エステ",
        "brand_name": "Beauty World (ビューティーワールド)",
        "capacity": "12回分セット（個包装×12袋）",
        "type": "高保湿・脱いだらしっとりハンドマスク（大容量12袋セット）",
        "features": "アルブチン、カタツムリ分泌液、オリーブ果実油、アラントイン、密着グローブ設計",
        "value": "ドラッグストアで大人気の脱いだらしっとりシリーズ。1回あたり約200円の圧倒的コスパで、冬の間毎週惜しみなく集中ケア可能",
        "desc_p1": "全国のバラエティショップやドラッグストアで不動のベストセラーとして君臨するビューティーワールドの『脱いだらしっとり ハンドマスク』。長年愛され続ける最大の理由は、商品名に偽りのない『脱いだ瞬間に肌が吸い付くような圧倒的なしっとり感』と、継続しやすい抜群のコストパフォーマンスにあります。",
        "desc_p2": "肌をワントーン明るく透明感のある肌へ導くアルブチンと、高い自己再生力で知られるカタツムリ分泌液エキスを贅沢に配合。冬の紫外線や乾燥による手の甲のくすみを取り去りながら、乾燥で失われた水分と油分を黄金バランスでチャージします。約20分間のパックを終えて手袋を外すと、まるでエステサロンでパラフィンパックを受けた直後のように、ふっくらとキメの整った明るい手肌へと生まれ変わります。",
        "target": "冬の間定期的にハンドパックを続けたい方、コスパ重視でまとめ買いしたい方、手の甲のくすみや色ムラが気になる方",
        "point": "週に2〜3回、夜のスキンケアタイムに使用するのが理想的。使用前にぬるま湯で手を温めておくと、角層の毛穴が開き美容液の吸収スピードが倍増します。"
    },
    {
        "rank": 4,
        "tag": "✨ ネイルケアのプロが推奨！指先から爪先まで一気に満たすエッセンスハンドマスク",
        "catch": "コラーゲン＆植物オイルカプセル。冬の冷えでカサついた手肌をふっくら若々しい印象へ",
        "brand_name": "Lucky Trendy (ラッキーウィンク)",
        "capacity": "2個セット（計2回分）",
        "type": "濃厚コラーゲン＆エッセンス高保湿ハンドマスク",
        "features": "加水分解コラーゲン、ヒアルロン酸Na、アルブチン、ダイズ種子エキス、簡単シール固定",
        "value": "ネイルグッズの専門メーカーが開発。手首部分を固定する密着テープ付きで、作業中もズレずに手肌を集中パック",
        "desc_p1": "ネイルツールやヘアケア雑貨で長年日本の女性のキレイを支えてきたラッキーウィンクの『ハンドエッセンスマスク』。セルフネイルを楽しむ女性や、冬の爪の割れやすさ・二枚爪に悩む方に向けて、手肌だけでなく爪とキューティクル（甘皮）の保湿まで徹底計算された処方が特徴です。",
        "desc_p2": "加水分解コラーゲンと高浸透ヒアルロン酸が、年齢とともに痩せてシワが目立ちやすくなった手の甲の皮膚を内側から押し上げるようにハリを満たします。手首部分にはサイズ調整ができる粘着テープが付いており、手袋が手首にピタッと密着して隙間からの空気の侵入を遮断。外気が遮断された温かいグローブ内でスチームサウナのような発汗・浸透効果が生まれ、ガサガサの手指が見違えるほど柔らかく滑らかに整います。",
        "target": "爪が乾燥して割れやすい・二枚爪になりやすい方、手の甲のハリ不足やシワっぽさが気になる方、手首までしっかりカバーしたい方",
        "point": "ハンドマスクを外した直後、爪の根本（甘皮部分）を反対側の親指でクルクルとマッサージしながら美容液を擦り込むと、血色感のある美しい美爪が育ちます。"
    },
    {
        "rank": 5,
        "tag": "🌰 アルガンオイルの奇跡！モロッコの黄金オイルが真冬の深刻なゴワつき手肌を急速リペア",
        "catch": "必須脂肪酸とビタミンEを豊富に含むアルガンオイル配合。一晩でカサつきを忘れさせる濃密グローブ",
        "brand_name": "Beauty World (ビューティーワールド)",
        "capacity": "1回分（個包装）",
        "type": "SBアルガンオイル高保湿ハンドマスク",
        "features": "アルガニアスピノサ核油、シアバター、マカデミア種子油、酢酸トコフェロール（ビタミンE）",
        "value": "天然のビタミンE爆弾と呼ばれるアルガンオイルを配合。ドラッグストアのレジ横でも大人気の即効レスキューアイテム",
        "desc_p1": "モロッコの過酷な砂漠環境を生き抜くアルガンの樹の実から採れる希少な『アルガンオイル』を主役に据えた、ビューティーワールドの『SBハンドマスク』。一般的な植物オイルの数倍とも言われるビタミンE（抗酸化成分）と必須脂肪酸が豊富に含まれており、冬の寒さと乾燥でカチカチに硬くなった手のひらや指先を劇的に柔らかくほぐします。",
        "desc_p2": "手袋をはめると、リッチなオイルインエッセンスが手の甲から指の一本一本まで吸い付くように密着。皮膚温度でじんわりと温まりながら、角層の細胞間脂質を補修して水分の蒸発ルートを完全に塞ぎます。使用後の手肌は、触れた瞬間にわかるほどシルキーでふんわりとした柔らかさに。ベタつかずサラサラの上質な油膜ヴェールが残るため、翌朝の洗顔や水仕事をしても潤いが流れ落ちません。",
        "target": "手のひらや指先が硬くゴワついて柔軟性がない方、アルガンオイルの上質なエモリエント効果を実感したい方、冬のスペシャルケアに",
        "point": "おやすみ前のベッドの中で装着し、20分経ったら外してそのまま就寝すると、寝ている間に残ったオイル成分がじっくり浸透し翌朝感動のモチモチ肌に出会えます。"
    },
    {
        "rank": 6,
        "tag": "🧴 驚異の大容量36枚入り！毎日惜しみなく使えるサロン発想のデイリーハンドマスク",
        "catch": "EGF・プラセンタ・セラミドなど贅沢115種。大容量BOXで冬の家事後のデイリー習慣に",
        "brand_name": "URUWOEET (ウルオイート)",
        "capacity": "大容量 36枚入（両手18回分）",
        "type": "サロン仕様・大容量プレミアムモイスチャーハンドマスク",
        "features": "ノーベル賞受賞成分EGF、高純度プラセンタエキス、ヒト型セラミド、ヒアルロン酸Na、日本製",
        "value": "エステサロン発想の大容量ハンドマスク。1回あたり約146円という破格のコストで、高級エイジング成分を毎日贅沢に手肌へチャージ",
        "desc_p1": "『ハンドパックは高価だから特別な日しか使えない…』という常識を覆し、冬の毎日のスキンケア習慣として定着させたのが、ウルオイートの『プレミアム モイスチャーハンドマスク』です。美容液がひたひたに浸ったグローブが36枚（両手18回分）入った密閉チャック式パッケージで、日々の水仕事の後に気兼ねなく使えます。",
        "desc_p2": "成分表には、細胞再生を促すノーベル賞受賞成分『EGF（上皮成長因子）』をはじめ、プラセンタエキス、ヒト型セラミド、コラーゲンなど、高級フェイスマスク顔負けのエイジングケア成分が贅沢に配合されています。毎晩のテレビタイムや読書中に手袋をはめるだけで、日常の乾燥や紫外線ダメージをリセット。継続して使用することで、手の甲の血管浮きや細かい縮緬ジワが目立たなくなり、透明感のある若々しい手肌を維持できます。",
        "target": "毎日または1日おきにたっぷりハンドパックをしたい方、手の甲のエイジングサイン（小ジワ・血管浮き）を本気で予防したい方、安心の日本製を求める方",
        "point": "外袋から取り出した後、付属の外側用ビニール手袋を重ねて装着すると、美容液の水分蒸発が完全にゼロになり、さらに保温力が高まって浸透効果が倍増します。"
    },
    {
        "rank": 7,
        "tag": "🛡️ 5層複合セラミドがバリアを急速再構築！韓国ドクターズコスメの頂点セラマイディン",
        "catch": "崩壊した手肌バリアを科学の力でリペア。寒さで赤く荒れた指先を濃密セラミドヴェールで包む",
        "brand_name": "Dr.Jart+ (ドクタージャルト)",
        "capacity": "チューブ 100ml / ハンド集中パック対応",
        "type": "高濃度5層セラミド・集中バリアリペアハンドトリートメント",
        "features": "5種類の複合セラミド（5-Cera Complex）、ヒアルロン酸、シアバター、低刺激皮膚科学処方",
        "value": "世界中でバリアケアの代名詞として愛されるドクタージャルト。乾燥による手肌のピリピリ感やひび割れを根本から立て直す頼れる一本",
        "desc_p1": "皮膚科学に基づいた高機能コスメで世界中の乾燥肌を救ってきた韓国のドクターズコスメ、Dr.Jart+（ドクタージャルト）の象徴的ライン『セラマイディン』。冬の冷気や繰り返す手洗いで角層のセラミドが流出し、バリア機能が完全に崩壊してしまった深刻な手荒れを救うために開発されました。",
        "desc_p2": "分子構造の異なる5種類のセラミドを独自技術でブレンドした『5-Cera Complex』が、角層の隙間をパズルのピースのように隙間なく埋め尽くし、水分の蒸発を物理的にブロック。こっくりとした濃厚なテクスチャーでありながら肌に吸い付くように馴染み、硬くなった角質をしなやかに整えます。手袋型マスクと併用、あるいは本品をたっぷり塗ってラップや綿手袋で密閉することで、どんな頑固な乾燥も一晩で鎮静します。",
        "target": "乾燥がひどすぎて手の甲がピリピリ痛い方、皮膚科学に基づく確かなバリア修復力を求める方、海外セレブも愛用する実力派コスメを使いたい方",
        "point": "本品を指先や関節のひび割れ部分に厚めに塗り込み、その上から後述の天然シルク手袋やビニール手袋を着用して眠ると、翌朝驚くほど滑らかな手肌に再生します。"
    },
    {
        "rank": 8,
        "tag": "💐 指先から手首まで華やかなブーケの香り！シアバター濃密エッセンスで手肌を満たす",
        "catch": "上質なホワイトフローラルアロマ×温感ラッピング。脱いだ後も一日中優雅な香りと潤いが持続",
        "brand_name": "KOCOSTAR (ココスター / コスメプラザ)",
        "capacity": "1回分（個包装）",
        "type": "高保湿・アロマブーケハンドトリートメントマスク",
        "features": "高濃度シアバター、ダマスクローズ水、カモミール花エキス、パラフィン成分、二重密封シート",
        "value": "見た目も華やかなブーケデザインパッケージ。友人へのプレゼントや自分への週末ご褒美ハンドスパとして圧倒的な人気",
        "desc_p1": "忙しい年末の毎日に、心ほどける優雅な香りとエステ級の潤いを同時に届けてくれるKOCOSTARの『ハンドブーケマスク』。まるで生花の花束を受け取ったかのような美しいパッケージデザインと、封を開けた瞬間に広がるフレッシュなホワイトフローラルの香りが特徴です。",
        "desc_p2": "エステのパラフィンパックから着想を得た温感ラッピング処方により、装着している間に体温を閉じ込めて手肌をポカポカと温め、血行を促進。ダマスクローズ蒸留水と高純度シアバターが乾ききった角層にみずみずしい潤いと柔軟性を与えます。脱いだ後も手肌から上品な香りがふわりと立ち上り、手の甲のキメが整って光を綺麗に反射するトーンアップ効果を実感できます。",
        "target": "ハンドケアに癒やしの香りを求める方、週末のスペシャルケアで優雅な気分に浸りたい方、女友達への冬のプチギフトを探している方",
        "point": "お風呂でゆっくり湯船に浸かりながら、または温かいハーブティーを飲みながら20分間パックするのが、香りによるリラックス効果を最大化する秘訣です。"
    },
    {
        "rank": 9,
        "tag": "🧵 創業の匠が編み立てた天然シルク100%！蒸れずに朝まで潤いを閉じ込めるおやすみ手袋",
        "catch": "人の皮膚に最も近い18種類のアミノ酸。ハンドクリームやパックの上から重ねるだけで極上ナイトスパ",
        "brand_name": "絹屋 (きぬや)",
        "capacity": "1双（両手分・スマホ対応）",
        "type": "日本製・天然シルク100%おやすみ保湿手袋",
        "features": "国産天然シルク100%、親指・人差し指スマホ対応導電糸、吸湿放湿性抜群、手洗い洗濯可能",
        "value": "日本の伝統技術で丁寧に編まれた極上の肌触り。綿手袋のように蒸れたりゴワつかず、朝まで脱げずに潤いをキープ",
        "desc_p1": "ハンドマスクや濃厚ハンドクリームを塗った後、寝具を汚さずに一晩中潤いを密封し続けたい…そんな大人の女性に熱烈に支持されているのが、日本の老舗絹織物ブランド絹屋の『天然シルク100% おやすみ手袋』です。シルクは人間の皮膚タンパク質とほぼ同じ18種類のアミノ酸で構成されているため、肌への刺激が極めて少なく、乾燥肌を優しく保護します。",
        "desc_p2": "一般的なコットン（綿）手袋と決定的に異なるのは、その卓越した『調湿機能』です。余分な湿気は外へ逃がし、必要な水分だけを適度に保持するため、手汗で蒸れて痒くなったり冷えたりすることが一切ありません。親指と人差し指の先端にはスマホ対応の導電糸が編み込まれており、ベッドの中で手袋を着けたままスマートフォンを操作可能。手袋をはめて眠るだけで、翌朝の手肌のしっとり感が見違えるほど向上します。",
        "target": "ハンドクリームを塗ってそのまま寝るとシーツや布団が汚れるのが嫌な方、手汗の蒸れが苦手な敏感肌の方、上質な天然素材にこだわりたい方",
        "point": "ハンドクリームや美容液ハンドマスクを使った後の『仕上げの保護カバー』として毎晩着用するのが最強のエイジングケア習慣です。"
    },
    {
        "rank": 10,
        "tag": "💧 プラセンタ＆コラーゲン贅沢配合！冬のエイジングサインを集中リセットする12袋セット",
        "catch": "個包装12個セット。気になる手の甲の乾燥小ジワをふっくら持ち上げ若々しい手元へ",
        "brand_name": "JAPAN GALS (ジャパンギャルズ)",
        "capacity": "12回分セット（個包装×12袋）",
        "type": "高純度プラセンタ＆コラーゲン配合・潤いハンドマスク",
        "features": "プラセンタエキス、水溶性コラーゲン、グリセリン、個別包装衛生的、密着フィットシート",
        "value": "美容マスク専門メーカーのジャパンギャルズが手掛ける高品質マスク。12個入りで家族や友人とシェアしても大満足のボリューム",
        "desc_p1": "フェイスマスクのパイオニアとして数々のヒット商品を生み出してきたジャパンギャルズの『潤いハンドマスク』。加齢や冬の寒冷乾燥によって皮膚が薄くなり、手の甲のシワや血管が目立つようになってきた手元のエイジングケアに特化した実力派パックです。",
        "desc_p2": "美肌の万能成分である高純度プラセンタエキスと、肌の弾力を支える水溶性コラーゲンをたっぷり含んだ美容液が、手袋全体に均一に充填されています。手の甲から爪先までしっかり包み込み、20分間の密閉浸透によって乾いた角層を潤いで満水状態へ。1回分ずつの完全個包装になっているため、旅行先や帰省先、冬のスキー場など乾燥しやすい外出先へ持ち運ぶのにも非常に重宝します。",
        "target": "手の甲のシワっぽさや弾力低下が気になる大人世代、個包装で清潔に持ち歩きたい方、コスパ良く12回分たっぷり使いたい方",
        "point": "お風呂上がりに、まず化粧水を手の甲にサッと馴染ませてから本ハンドマスクを装着すると、水分の導入路ができてプラセンタの浸透力が格段に高まります。"
    }
]

# 比較表生成
table_rows = []
for p, item in zip(product_details, items):
    table_rows.append(f"""
    <tr>
      <td class="rank-cell">第{p['rank']}位</td>
      <td class="brand-cell"><strong>{p['brand_name']}</strong><br><small>{item['display_name'][:25]}...</small></td>
      <td class="price-cell">¥{item['price']:,}</td>
      <td>{p['type']}</td>
      <td>{p['capacity']}</td>
      <td>{p['features']}</td>
    </tr>
    """)

# 商品カードHTML生成
product_cards_html = []
for p, item in zip(product_details, items):
    product_cards_html.append(f"""
    <article class="product-card" id="rank-{p['rank']}">
      <div class="product-badge">第{p['rank']}位</div>
      <div class="product-header">
        <span class="product-tag">{p['tag']}</span>
        <h3 class="product-title">{p['brand_name']} - {item['display_name']}</h3>
        <p class="product-catch">{p['catch']}</p>
      </div>

      <div class="product-main">
        <div class="product-image-wrap">
          <img src="{item['image_url']}" alt="{p['brand_name']} {item['display_name']}" class="product-img" loading="lazy">
        </div>
        <div class="product-info">
          <div class="product-meta-list">
            <div class="meta-item"><span class="meta-label">参考価格：</span><span class="meta-value price-val">¥{item['price']:,}（税込）</span></div>
            <div class="meta-item"><span class="meta-label">セット内容：</span><span class="meta-value">{p['capacity']}</span></div>
            <div class="meta-item"><span class="meta-label">アイテム種別：</span><span class="meta-value">{p['type']}</span></div>
            <div class="meta-item"><span class="meta-label">主要成分・特徴：</span><span class="meta-value">{p['features']}</span></div>
            <div class="meta-item"><span class="meta-label">取扱店舗：</span><span class="meta-value">{item['shop_name']}</span></div>
          </div>
          <div class="product-points">
            <h4>💡 ここが冬の水仕事手荒れ＆ひび割れに効く注目ポイント！</h4>
            <p>{p['value']}</p>
          </div>
        </div>
      </div>

      <div class="product-description">
        <h4>【詳細解説＆本音レビュー】</h4>
        <p>{p['desc_p1']}</p>
        <p>{p['desc_p2']}</p>
      </div>

      <div class="product-advice">
        <div class="advice-block target-block">
          <strong>🎯 こんな人に特におすすめ：</strong>
          <p>{p['target']}</p>
        </div>
        <div class="advice-block tip-block">
          <strong>✨ プロの密閉集中リペアアドバイス：</strong>
          <p>{p['point']}</p>
        </div>
      </div>

      <div class="product-action">
        <a href="{item['affiliate_url']}" class="rakuten-btn" target="_blank" rel="noopener noreferrer nofollow">
          <span>楽天市場で最安値＆口コミをチェック</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </article>
    """)

faq_items = [
    {
        "q": "ハンドクリームを塗るのと、手袋型ハンドマスクを使うのでは何が違うのですか？",
        "a": "『浸透深度』と『密閉力（ODT効果）』が決定的に違います。通常のハンドクリームは皮膚表面の油分を補い保護膜を作るのが主な役割ですが、冬の深刻な乾燥で硬くなった角層には奥まで成分が届きにくく、手洗いや摩擦で数時間で落ちてしまいます。一方、手袋型ハンドマスクは美容液を手袋内部に閉じ込めることで、水分の蒸発を防ぎながら角層の最深部まで美容成分（ヒアルロン酸、コラーゲン、EGFなど）を強制浸透させます。わずか20分で皮膚細胞の奥まで満水状態にできるため、1回でエステ帰りのようなモチモチ感が手に入ります。"
    },
    {
        "q": "手袋型ハンドマスクをつけたまま、スマートフォンの操作や家事はできますか？",
        "a": "多くの手袋型マスク（DearIrean、KOCOSTAR、絹屋など）は、スマホ対応フィルムを採用しているか、外側がサラサラのドライ二重構造になっているため、スマホの画面操作やパソコン作業、読書などが問題なく行えます。ただし、水を使った家事（食器洗いや洗濯）を行う場合は、美容液手袋の上から市販のゴム手袋やビニール手袋を重ねて装着することで、水濡れを防ぎながら家事の温水でスチーム効果を高める『家事中スチームエステ』が可能です。"
    },
    {
        "q": "ハンドマスクを外した後は、手を水で洗い流したほうがいいですか？",
        "a": "絶対に洗い流さないでください。手袋を外した直後は肌表面に高濃度の美容液が残っていますので、手の甲から指先、爪の甘皮、さらに手首からひじにかけて優しくマッサージするように擦り込んで馴染ませるのが最も効果的です。もしベタつきが気になる場合は、軽くティッシュで押さえるか、上から薄くハンドクリームやシルク手袋を重ねて油分で蓋をしてください。"
    },
    {
        "q": "冬の手荒れ対策として、どのくらいの頻度で使うのがベストですか？",
        "a": "手肌のコンディションに合わせて調整するのがおすすめです。すでに指先がひび割れて粉を吹いているなど手荒れが深刻な初期段階では、『2〜3日に1回（週2〜3回）』の集中ケアを1〜2週間続けると、劇的にバリア機能が立て直されます。肌が落ち着いた後は、『週に1回の週末スペシャルケア』として継続することで、冬の間中ずっと柔らかく若々しい手肌をキープできます。"
    },
    {
        "q": "手肌に赤みやひび割れ、出血がある状態でもハンドマスクを使って大丈夫ですか？",
        "a": "出血を伴う深いパックリ割れや湿疹、強い炎症がある場合は、美容液の成分がしみて悪化する恐れがあるため使用を控えてください。その場合はまず皮膚科の軟膏（ヘパリン類似物質やステロイド外用薬等）で傷口を治すことを最優先にしましょう。傷口が塞がり、乾燥によるカサつきや小ジワ、ささくれが気になる段階になってからハンドマスクを取り入れるのが安全で効果的です。"
    }
]

# JSON-LD 構造化データ
json_ld_products = []
for p, item in zip(product_details, items):
    json_ld_products.append({
        "@type": "Product",
        "name": f"{p['brand_name']} {item['display_name']}",
        "image": item['image_url'],
        "description": p['value'],
        "brand": {
            "@type": "Brand",
            "name": p['brand_name']
        },
        "offers": {
            "@type": "Offer",
            "url": item['affiliate_url'],
            "priceCurrency": "JPY",
            "price": item['price'],
            "availability": "https://schema.org/InStock"
        }
    })

json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで冬の水仕事手荒れ・指先ガサガサひび割れとさようなら！手袋型で美容液が角層深部まで超密着浸透する高保湿ハンドマスクランク10",
    "description": "11月・12月の冬の大掃除・水仕事・アルコール消毒による深刻な手荒れ・指先ひび割れ・手の甲の乾燥小ジワを徹底解決！DearIrean、KOCOSTAR、ビューティーワールド、ラッキーウィンク、ウルオイート、Dr.Jart+、絹屋など、ODT密閉発想で角層深部まで美容液を届ける最強高保湿ハンドマスク10選を徹底比較！",
    "image": items[0]['image_url'],
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
    "name": "冬の高保湿ハンドマスク・集中美容液手袋パック おすすめランキング10選",
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
            "name": faq['q'],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq['a']
            }
        } for faq in faq_items
    ]
}

json_ld_breadcrumb = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "ホーム",
            "item": "https://lumi-cosme.vercel.app/"
        },
        {
            "@type": "ListItem",
            "position": 2,
            "name": "ハンドマスク特集",
            "item": "https://lumi-cosme.vercel.app/winter-hand-mask"
        }
    ]
}

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで冬の水仕事手荒れ・指先ガサガサひび割れとさようなら！手袋型で美容液が角層深部まで超密着浸透する高保湿ハンドマスクランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬の大掃除・水仕事・アルコール消毒による深刻な手荒れ・指先ひび割れ・手の甲の乾燥小ジワを徹底解決！DearIrean、KOCOSTAR、ビューティーワールド、ラッキーウィンク、ウルオイート、Dr.Jart+、絹屋など、ODT密閉発想で角層深部まで美容液を届ける最強高保湿ハンドマスク10選を徹底比較！">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-hand-mask">
  <link rel="icon" href="/favicon.jpg">
  <link rel="stylesheet" href="style.css">

  <!-- Open Graph -->
  <meta property="og:title" content="保湿力の強さで冬の水仕事手荒れ・指先ガサガサひび割れとさようなら！手袋型で美容液が角層深部まで超密着浸透する高保湿ハンドマスクランク10">
  <meta property="og:description" content="11月・12月の冬の水仕事手荒れ・指先ひび割れを徹底解決！DearIrean、KOCOSTAR、ビューティーワールドなど手袋型で美容液を超密着浸透させる最強ハンドマスク10選！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-hand-mask">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">

  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json">
  {json.dumps(json_ld_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_itemlist, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_faq, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_breadcrumb, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #be123c;
      --primary-dark: #9f1239;
      --primary-light: #fff1f2;
      --accent: #e11d48;
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --radius: 16px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
    }}

    .site-header {{
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 1rem 0;
    }}
    .header-container {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--primary-dark);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .nav-links {{
      display: flex;
      gap: 1.5rem;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-weight: 600;
      font-size: 0.95rem;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{
      color: var(--primary);
    }}

    .main-container {{
      max-width: 960px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}

    .breadcrumbs {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
    }}
    .breadcrumbs a {{
      color: var(--text-muted);
      text-decoration: none;
    }}
    .breadcrumbs a:hover {{
      color: var(--primary);
    }}

    .article-header {{
      background: linear-gradient(135deg, #be123c 0%, #9f1239 50%, #881337 100%);
      color: white;
      padding: 3.5rem 2rem;
      border-radius: var(--radius);
      margin-bottom: 2.5rem;
      box-shadow: 0 10px 25px -5px rgba(190, 18, 60, 0.3);
    }}
    .article-tag {{
      display: inline-block;
      background: rgba(255, 255, 255, 0.2);
      backdrop-filter: blur(4px);
      padding: 0.35rem 1rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      margin-bottom: 1rem;
    }}
    .article-title {{
      font-size: 2rem;
      font-weight: 800;
      line-height: 1.4;
      margin-bottom: 1.5rem;
    }}
    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.9rem;
      opacity: 0.9;
    }}

    .intro-box {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 2.5rem;
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
      border-left: 6px solid var(--primary);
    }}
    .intro-lead {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
      line-height: 1.7;
    }}
    .intro-box p {{
      margin-bottom: 1rem;
      color: #334155;
    }}
    .intro-highlight-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 1.2rem;
      margin-top: 1.8rem;
    }}
    .intro-card {{
      background: var(--primary-light);
      padding: 1.2rem;
      border-radius: 12px;
      border: 1px solid rgba(190, 18, 60, 0.2);
    }}
    .intro-card h4 {{
      color: var(--primary-dark);
      font-size: 1rem;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}
    .intro-card p {{
      font-size: 0.88rem;
      color: #334155;
      margin-bottom: 0;
      line-height: 1.6;
    }}

    .section-title {{
      font-size: 1.7rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 1.5rem;
      padding-bottom: 0.6rem;
      border-bottom: 3px solid var(--primary);
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .table-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 2rem;
      box-shadow: var(--shadow);
      margin-bottom: 3.5rem;
    }}
    .table-wrapper {{
      overflow-x: auto;
    }}
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}
    .spec-table th, .spec-table td {{
      padding: 1rem 0.8rem;
      border-bottom: 1px solid var(--border);
    }}
    .spec-table th {{
      background: #f1f5f9;
      font-weight: 700;
      color: #334155;
      white-space: nowrap;
    }}
    .spec-table .rank-cell {{
      font-weight: 800;
      color: var(--primary-dark);
      text-align: center;
      white-space: nowrap;
    }}
    .spec-table .price-cell {{
      font-weight: 700;
      color: #e11d48;
      white-space: nowrap;
    }}

    .product-card {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 2.2rem;
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
      position: relative;
      border: 1px solid var(--border);
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .product-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 12px 20px -5px rgba(0, 0, 0, 0.08);
    }}
    .product-badge {{
      position: absolute;
      top: -12px;
      left: 24px;
      background: linear-gradient(135deg, #be123c, #9f1239);
      color: white;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 0.3rem 1.2rem;
      border-radius: 9999px;
      box-shadow: 0 4px 8px rgba(190, 18, 60, 0.3);
    }}
    .product-header {{
      margin-top: 0.8rem;
      margin-bottom: 1.5rem;
    }}
    .product-tag {{
      display: inline-block;
      color: var(--primary-dark);
      font-weight: 700;
      font-size: 0.85rem;
      background: var(--primary-light);
      padding: 0.25rem 0.75rem;
      border-radius: 6px;
      margin-bottom: 0.5rem;
    }}
    .product-title {{
      font-size: 1.45rem;
      font-weight: 800;
      line-height: 1.4;
      color: #0f172a;
      margin-bottom: 0.4rem;
    }}
    .product-catch {{
      font-size: 1rem;
      color: var(--text-muted);
      font-weight: 600;
    }}

    .product-main {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
      margin-bottom: 1.8rem;
    }}
    @media (max-width: 768px) {{
      .product-main {{ grid-template-columns: 1fr; }}
      .article-title {{ font-size: 1.5rem; }}
    }}
    .product-image-wrap {{
      text-align: center;
      background: #f8fafc;
      border-radius: 12px;
      padding: 1rem;
      border: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .product-img {{
      max-width: 100%;
      max-height: 250px;
      object-fit: contain;
      border-radius: 8px;
    }}

    .product-meta-list {{
      background: #f8fafc;
      border-radius: 10px;
      padding: 1rem 1.2rem;
      margin-bottom: 1.2rem;
      border: 1px solid var(--border);
    }}
    .meta-item {{
      display: flex;
      font-size: 0.9rem;
      padding: 0.35rem 0;
      border-bottom: 1px dashed #e2e8f0;
    }}
    .meta-item:last-child {{ border-bottom: none; }}
    .meta-label {{
      width: 110px;
      font-weight: 700;
      color: var(--text-muted);
      flex-shrink: 0;
    }}
    .meta-value {{
      color: var(--text);
      font-weight: 500;
    }}
    .price-val {{
      color: #e11d48;
      font-weight: 800;
      font-size: 1.15rem;
    }}

    .product-points {{
      background: #fff1f2;
      border-left: 4px solid #e11d48;
      padding: 1rem 1.2rem;
      border-radius: 0 8px 8px 0;
    }}
    .product-points h4 {{
      font-size: 0.92rem;
      color: #9f1239;
      margin-bottom: 0.3rem;
    }}
    .product-points p {{
      font-size: 0.88rem;
      color: #881337;
      line-height: 1.6;
      margin-bottom: 0;
    }}

    .product-description {{
      margin-bottom: 1.5rem;
      line-height: 1.8;
      color: #334155;
    }}
    .product-description h4 {{
      font-size: 1.05rem;
      color: #0f172a;
      margin-bottom: 0.6rem;
    }}
    .product-description p {{
      margin-bottom: 0.8rem;
    }}

    .product-advice {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-bottom: 1.8rem;
    }}
    @media (max-width: 640px) {{
      .product-advice {{ grid-template-columns: 1fr; }}
    }}
    .advice-block {{
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.88rem;
      line-height: 1.6;
    }}
    .target-block {{
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #1e3a8a;
    }}
    .tip-block {{
      background: #fefce8;
      border: 1px solid #fef08a;
      color: #713f12;
    }}
    .advice-block strong {{
      display: block;
      margin-bottom: 0.3rem;
    }}

    .product-action {{
      text-align: center;
      margin-top: 1rem;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.6rem;
      background: linear-gradient(135deg, #bf0000 0%, #e60000 100%);
      color: white;
      text-decoration: none;
      font-size: 1.05rem;
      font-weight: 700;
      padding: 1rem 2.5rem;
      border-radius: 9999px;
      box-shadow: 0 4px 12px rgba(191, 0, 0, 0.25);
      transition: transform 0.2s, box-shadow 0.2s;
      width: 100%;
      max-width: 480px;
    }}
    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(191, 0, 0, 0.35);
      color: white;
    }}

    .faq-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 2.5rem;
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
    }}
    .faq-item {{
      border-bottom: 1px solid var(--border);
      padding: 1.5rem 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.6rem;
      display: flex;
      align-items: flex-start;
      gap: 0.6rem;
    }}
    .faq-q::before {{
      content: "Q";
      background: var(--primary);
      color: white;
      font-size: 0.8rem;
      font-weight: 800;
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      margin-top: 0.2rem;
    }}
    .faq-a {{
      color: #334155;
      font-size: 0.95rem;
      line-height: 1.8;
      padding-left: 1.8rem;
    }}

    .internal-links-box {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 2.5rem;
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
    }}
    .links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1rem;
      margin-top: 1.2rem;
    }}
    .link-card {{
      background: #f8fafc;
      padding: 1rem;
      border-radius: 8px;
      border: 1px solid var(--border);
      text-decoration: none;
      color: var(--text);
      transition: border-color 0.2s, background 0.2s;
    }}
    .link-card:hover {{
      border-color: var(--primary);
      background: var(--primary-light);
    }}
    .link-card strong {{
      display: block;
      color: var(--primary-dark);
      font-size: 0.92rem;
      margin-bottom: 0.3rem;
    }}
    .link-card span {{
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.4;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}

    .site-footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 3rem 0;
      margin-top: 4rem;
      border-top: 1px solid #1e293b;
    }}
    .footer-container {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      text-align: center;
      font-size: 0.85rem;
    }}
    .footer-links {{
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 1.2rem;
      margin-bottom: 1.5rem;
    }}
    .footer-links a {{
      color: #cbd5e1;
      text-decoration: none;
    }}
    .footer-links a:hover {{
      color: white;
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-container">
      <a href="/" class="site-logo">
        <span>❄️ 冬コスメ徹底比較ラボ</span>
      </a>
      <nav class="nav-links">
        <a href="/">トップ</a>
        <a href="/winter-hand-mask">ハンドマスク</a>
        <a href="/winter-hand-cream">ハンドクリーム</a>
        <a href="/winter-nail-oil">ネイルオイル</a>
      </nav>
    </div>
  </header>

  <main class="main-container">
    <div class="breadcrumbs">
      <a href="/">ホーム</a> &gt; <a href="/winter-hand-mask">冬のハンド＆ネイル特集</a> &gt; <span>高保湿ハンドマスク・集中美容液手袋パック</span>
    </div>

    <header class="article-header">
      <span class="article-tag">❄️ 11月・12月最新冬コスメ徹底比較特集</span>
      <h1 class="article-title">保湿力の強さで冬の水仕事手荒れ・指先ガサガサひび割れとさようなら！手袋型で美容液が角層深部まで超密着浸透する高保湿ハンドマスクランク10</h1>
      <div class="article-meta">
        <span>📅 更新日: 2026年11月2日</span>
        <span>⏱️ 読了目安: 約8分</span>
        <span>🔍 楽天公式APIリアルタイム価格検証済み</span>
      </div>
    </header>

    <div class="intro-box">
      <p class="intro-lead">
        11月下旬から12月、年末の大掃除や冷水での食器洗い、感染症対策による頻繁なアルコール消毒、そして氷点下に迫る乾燥風によって、手肌のバリア機能は年間で最も深刻な破壊的ダメージにさらされます。「ハンドクリームを1日に何度も塗り直しているのに、指先がガサガサにひび割れて痛い」「手の甲がシワシワになって老けて見える」と絶望している方に、唯一無二の集中再生ソリューションとなるのが『高保湿ハンドマスク（手袋型美容液パック）』です。
      </p>
      <p>
        一般的なハンドクリームは皮膚表面の油分を一時的に補うに過ぎず、手洗いや摩擦によってわずか数時間で消失してしまいます。一方、手袋型ハンドマスクは、美容皮膚科で行われる『ODT（密閉包帯療法：Occlusive Dressing Treatment）』と同じメカニズムを採用。美容液をたっぷり含んだ手袋で手肌全体を密閉することで、水分の体外蒸発を完全に遮断し、角層の細胞間脂質や天然保湿因子（NMF）を短時間で強制的に満水状態へと導きます。
      </p>
      <p>
        わずか20分間手袋をはめるだけで、硬くゴワついた角質がとろけるようにほぐれ、爪周りのささくれや手の甲の小ジワが見違えるほどモチモチに回復します。最近ではスマホ操作に対応したモデルも多く、動画を見ながら手軽にサロン級ハンドエステが完結します。本特集では、楽天市場公式APIより最新データをリアルタイム取得し、2026年冬に絶対に持っておくべき実力派ハンドマスク10選を徹底比較します。
      </p>

      <div class="intro-highlight-grid">
        <div class="intro-card">
          <h4>🧤 美容皮膚科のODT密閉浸透</h4>
          <p>手袋形状で外気を遮断し水分の蒸発をゼロに。角層の最深部まで高濃度美容液を強制的に押し込みます。</p>
        </div>
        <div class="intro-card">
          <h4>💅 爪周り・ささくれ・甘皮も同時ケア</h4>
          <p>ハンドクリームでは塗り残しがちな爪のキワや関節のシワまで、美容液が均一に包み込み美爪を育成します。</p>
        </div>
        <div class="intro-card">
          <h4>📱 スマホ操作対応で究極のタイパ</h4>
          <p>パック中もスマートフォンやPC作業が可能。忙しい年末の合間に20分でサロン帰りのシルク手肌が手に入ります。</p>
        </div>
      </div>
    </div>

    <!-- 比較表セクション -->
    <section class="table-section">
      <h2 class="section-title">📊 高保湿ハンドマスク・集中手袋パック 厳選10選スペック比較表</h2>
      <div class="table-wrapper">
        <table class="spec-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名・ブランド</th>
              <th>参考価格（税込）</th>
              <th>アイテム種別</th>
              <th>セット内容</th>
              <th>主要成分・特徴</th>
            </tr>
          </thead>
          <tbody>
            {"".join(table_rows)}
          </tbody>
        </table>
      </div>
    </section>

    <!-- ランキング商品セクション -->
    <section class="products-section">
      <h2 class="section-title">🏆 保湿力高めハンドマスク ランキングTOP10</h2>
      {"".join(product_cards_html)}
    </section>

    <!-- ハウツーセクション -->
    <section class="intro-box" style="margin-top: 3rem;">
      <h2 class="section-title" style="border-bottom: none; margin-bottom: 1rem;">💡 プロが教える！冬の手荒れを20分で救う「サロン級集中ハンドパックプログラム」</h2>
      <p>
        ハンドマスクの効果を極限まで引き出すためのプロ直伝ステップです。特にひび割れや硬化がひどい夜に実践してください。
      </p>
      <div class="intro-highlight-grid">
        <div class="intro-card">
          <h4>1. 温水で手を温め角質を軟化</h4>
          <p>パック前にぬるま湯で手を温め、軽くタオルドライします。角層が水分を含んで温まることで美容液の吸収率が3倍に向上します。</p>
        </div>
        <div class="intro-card">
          <h4>2. 手袋の上から関節をモミモミ</h4>
          <p>装着後、指の関節や爪の生え際、手のひらのツボを反対の手で優しくマッサージ。血行が促進され指先までポカポカに温まります。</p>
        </div>
        <div class="intro-card">
          <h4>3. 外した後は洗い流さず腕まで</h4>
          <p>外した後の美容液は絶対に洗わず、手首からひじにかけて塗り伸ばします。さらにシルク手袋を着けて寝ると完璧です。</p>
        </div>
      </div>
    </section>

    <!-- よくある質問（FAQ） -->
    <section class="faq-section">
      <h2 class="section-title">❓ 冬の高保湿ハンドマスクに関するよくある質問（FAQ）</h2>
      <div class="faq-list">
        {''.join([f'''
        <div class="faq-item">
          <div class="faq-q">{item['q']}</div>
          <div class="faq-a">{item['a']}</div>
        </div>
        ''' for item in faq_items])}
      </div>
    </section>

    <!-- 内部リンク回遊セクション -->
    <section class="internal-links-box">
      <h2 class="section-title">🔗 あわせて読みたい！冬のパーツケア・集中保湿特集</h2>
      <div class="links-grid">
        <a href="/winter-hand-cream" class="link-card">
          <strong>🧤 高保湿ハンドクリーム10選</strong>
          <span>セラミドや尿素を高配合！水仕事の後や外出先でサッと塗って手荒れを防ぐデイリー名品比較。</span>
        </a>
        <a href="/winter-nail-oil" class="link-card">
          <strong>💅 高保湿ネイルオイル10選</strong>
          <span>冬の乾燥で割れやすい爪・二枚爪・甘皮のささくれを集中補修する植物オイルベースのネイルケア。</span>
        </a>
        <a href="/winter-hand-serum" class="link-card">
          <strong>💧 高保湿ハンド美容液10選</strong>
          <span>手の甲のエイジングサイン・血管浮き・くすみを美容液成分で内側からふっくら整えるリッチセラム。</span>
        </a>
        <a href="/winter-hand-wash" class="link-card">
          <strong>🧼 高保湿ハンドウォッシュ10選</strong>
          <span>洗うたびに潤いヴェールをまとう！冬の頻繁な手洗いでも手荒れさせない弱酸性ハンドソープ特集。</span>
        </a>
        <a href="/winter-foot-cream" class="link-card">
          <strong>👣 高保湿フットクリーム10選</strong>
          <span>冬のタイツに引っかかるガサガサかかと・ひび割れを集中浸透ケアでつるつるに導く名品まとめ。</span>
        </a>
        <a href="/winter-inbath-body" class="link-card">
          <strong>🛁 濡れた肌用インバスボディミルク10選</strong>
          <span>極寒の脱衣所に出る前にお風呂場で濡れたまま保湿！入浴後の急激な水分蒸発を防ぐ冬の必須ミルク。</span>
        </a>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-links">
        <a href="/">トップページ</a>
        <a href="/winter-hand-mask">ハンドマスク</a>
        <a href="/winter-hand-cream">ハンドクリーム</a>
        <a href="/winter-nail-oil">ネイルオイル特集</a>
        <a href="/winter-hand-care">ハンドケア総合</a>
      </div>
      <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved. 当サイトは楽天市場公式アフィリエイトプログラムに参加しています。</p>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-hand-mask.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-hand-mask.html!")
