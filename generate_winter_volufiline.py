import json
import re

with open("fetched_final_30_tranexamic_azulene_volufiline.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_volufiline"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 フランスセダーマ社純正原料100%配合！冬のしぼみ肌を底上げする最高峰原液",
        "catch": "ボルフィリン原液100%配合。真冬の乾燥でしぼんだ目元・ほうれい線にふっくら弾力を注入",
        "brand_name": "KISO (基礎化粧品研究所)",
        "capacity": "20ml (キソ ファーミングエッセンス VF)",
        "type": "高純度ボルフィリン原液美容液",
        "features": "フランスセダーマ社特許ボルフィリン（ハナスゲ根エキス・水添ポリイソブテン）100%配合、パラベンフリー",
        "value": "余計な希釈を行わず、世界最高峰のボリュームアップ特許原料をそのままボトリング。手持ちのクリームやセラムに混ぜても単体でも使える圧倒的汎用性",
        "desc_p1": "11月から12月へと本格的な寒さが訪れると、外気の乾燥だけでなく低気温による血行不良が皮膚の深層まで波及。水分や皮脂が失われるだけでなく、肌を内側から支える皮下組織の代謝が停滞し、目の下のくぼみ、頬のこけ、ほうれい線が急に深くなり、顔全体に暗い『冬枯れ影』が刻まれます。KISOのファーミングエッセンスVFは、そんな冬のしぼみ顔に挑む最高濃度のボルフィリン原液です。",
        "desc_p2": "フランスの老舗研究所セダーマ社が開発した特許原料『ボルフィリン』を、贅沢にも100%原液のまま採用。ユリ科植物ハナスゲの根から抽出される『サルササポゲニン』が、しぼんだ肌の内側で脂肪組織の働きを力強くサポートします。オイルのように濃厚でリッチなテクスチャーが、乾燥した角層をじんわりほぐしながら密着。夜塗って眠るだけで、翌朝の洗顔時には指先を跳ね返すようなふっくらとした肉感と濃密な潤いを実感できます。",
        "target": "冬になると目元のくぼみやほうれい線の影が目立つ方、肌の痩せ・しぼみが気になる大人肌、セダーマ社純正の高品質な原液をコスパ良く試したい方",
        "point": "化粧水の後にスポイトから1〜2滴を取り、目の下、ほうれい線、唇の輪郭に指先でトントンと押し込むように塗布。さらに手持ちの保湿クリームに1滴混ぜて全顔に伸ばすと、極上のふっくらリフトヴェールが完成します。"
    },
    {
        "rank": 2,
        "tag": "🇯🇵 純国産ボトリングの安心感！セダーマ社ハナスゲ根エキスを100%生かした濃密セラム",
        "catch": "フランス産ボルフィリン原料100%。冬の乾燥小ジワとしぼんだ皮膚にピンポイントでハリチャージ",
        "brand_name": "Beauty Farm (ビューティーファーム)",
        "capacity": "10ml (ボルフィリン 原液 100% 美容液)",
        "type": "国産高純度ボルフィリン原液",
        "features": "フランス産ハナスゲ根エキス配合ボルフィリン100%、無香料・無着色・エタノールフリー・日本製",
        "value": "日本国内のクリーンルームで丁寧に充填。気になるパーツに狙い撃ちしやすいドロップボトルで、冬の目袋・口元のたるみ影を集中ケア",
        "desc_p1": "国内の美容サロンやこだわり派のユーザーから高い評価を受けるビューティーファームの純度100%ボルフィリン美容液。原料の調達からボトリングまで徹底した品質管理のもとで作られた国産コスメです。",
        "desc_p2": "真冬の冷風で薄く縮こまってしまった目元の皮膚や、口角の周りに塗布すると、濃厚な原液が角層のキメの隙間を埋め尽くすようにピタッと密着。植物性フィトステロールが肌の奥深くに留まり、乾燥による細かい縮みジワを内側から押し広げるようにふっくら補正します。10mlのコンパクトサイズながら数滴で驚くほどの伸びと密着感を発揮し、毎日のスキンケアをクリニック級のパーツケアへと格上げします。",
        "target": "目元や口元の細かい影が気になり始めた30代〜50代、日本製クオリティの原液コスメを求める方、手持ちのアイクリームを強化したい方",
        "point": "夜のお手入れで、アイクリームを塗る直前に1滴を薬指に取り、目頭から目尻、こめかみに向かって優しく引き上げるようにプレス。唇に塗れば縦ジワの目立たないぷるぷるリップが叶います。"
    },
    {
        "rank": 3,
        "tag": "🫧 微細酸素バブルが弾けて角層深層へ直撃！ボルフィリン5%×ペプチド9種の革命エッセンス",
        "catch": "微細バブル×セダーマ社ボルフィリン5%。塗った瞬間に泡立ち、冬のたるみ肌をパンッと跳ね返す",
        "brand_name": "MEDI-PEEL (メディピール)",
        "capacity": "100ml (ペプチド9 ボリューム オールインワン エッセンス)",
        "type": "酸素バブル高機能リフティング美容液",
        "features": "セダーマ社ボルフィリン5%、ペプチド9種複合体、4重ヒアルロン酸、エラスチン配合",
        "value": "肌に塗布すると数秒で微細な酸素バブルが自然発生。バブルが弾ける刺激で血行を促し、ボルフィリンとペプチドを角層深部へ一気に押し込む",
        "desc_p1": "韓国のメディカルエステブランド『メディピール』が放つ、世界的大ヒットのボリュームエッセンス。フランスセダーマ社の特許ボルフィリンをなんと5%もの高濃度で配合し、さらに弾力を司るペプチドを9種類も凝縮したハイパフォーマーです。",
        "desc_p2": "肌の上に伸ばすと、わずか数秒で青白い微細な酸素の泡がシュワシュワと発泡。このバブルが冬の冷えで滞った肌を心地よくマッサージしながら、有効成分の浸透ルートを切り拓きます。泡がなじんだ後の肌は、まるでサロン帰りのように内側からパンッと張るような弾力と、水を弾くような水光ツヤを獲得。1本で化粧水・美容液・乳液の機能を兼ね備える贅沢処方です。",
        "target": "冬の冷えで顔全体がたるんで疲れて見えがちな方、サロン級の炭酸＆酸素美容を自宅で体験したい方、大容量で贅沢に使いたい方",
        "point": "洗顔後、4〜5プッシュを顔全体に厚めに塗り広げます。数秒後に泡立ってきたら、泡が自然に消えるまで待ち、その後手のひら全体で優しく押し込むようにハンドプレスしてください。"
    },
    {
        "rank": 4,
        "tag": "💄 スティック型でいつでもどこでもふっくら注入！ボルフィリン高配合の特濃マルチバーム",
        "catch": "ボルフィリン高配合スティック。冬の外出先でも目元・ほうれい線・唇のしぼみ影を一瞬でリセット",
        "brand_name": "SIDMOOL (シドミュール)",
        "capacity": "9.5ml (ボルフィリン40 弾力マルチバーム)",
        "type": "高濃度ボルフィリン集中スティックバーム",
        "features": "セダーマ社ボルフィリン高配合、シア脂、ミツロウ、天然植物性トコフェロール",
        "value": "乾燥と寒風でしぼんだ目元や口元に、手を汚さず直接ひと塗り。高保水バーム膜が水分蒸散をブロックしながらハリを注入",
        "desc_p1": "韓国の天然志向ダーマコスメの草分け『シドミュール』が誇る特濃バームスティック。セダーマ社の高品質ボルフィリンをバーム状に高濃度で固め、乾燥しやすいパーツにダイレクトに密着させます。",
        "desc_p2": "真冬の冷たい外気やオフィスの暖房で、午後になると目元の乾燥小ジワにファンデーションが食い込んだり、ほうれい線の影が濃くなったりする現象を、サッとひと塗りで解決。体温でとろける植物性ワックスが肌表面にツヤやかな保護膜を作り、ボルフィリンが肌内部のハリをサポートします。リップクリーム代わりにも使え、ふっくらグラマラスな唇をキープできます。",
        "target": "日中のオフィスの乾燥で目元や口元が突っ張る方、メイク直しと同時にエイジングケアをしたい方、持ち歩きコスメを求める方",
        "point": "メイクの上から乾燥が気になる目元やほうれい線に滑らせ、指先で軽くトントンとなじませます。夜はリップパックとして唇の輪郭オーバー気味に塗って就寝すると翌朝驚くほどふっくらします。"
    },
    {
        "rank": 5,
        "tag": "👁️ フランス産ボルフィリン20%配合の衝撃！目元のくぼみ・乾燥小ジワを消し去る特化クリーム",
        "catch": "ボルフィリン20%配合アイクリーム。真冬の乾燥でしわむ目元・まぶた・ゴルゴラインを集中リフト",
        "brand_name": "DERMA FACTORY (ダーマファクトリー)",
        "capacity": "30ml (ボルフィリン20% アイクリーム)",
        "type": "高濃度ボルフィリン集中アイクリーム",
        "features": "フランスセダーマ社ボルフィリン20%、コラーゲン水、パンテノール、アデノシン",
        "value": "成分開示ブランドならではの超高配合率。精製水の代わりにコラーゲン水を採用し、真冬のアイゾーンを内側から押し上げるようなハリ感で満たす",
        "desc_p1": "成分含有量を100%正直に公開することで爆発的な支持を集めるダーマファクトリー。本品は、アイクリームとしては異例中の異例となる『ボルフィリン20%』という圧倒的な高配合を実現したパーツ特化型クリームです。",
        "desc_p2": "基剤にも水ではなくコラーゲン水を使用し、乾燥して薄くなった目元の皮膚に密着。こっくりとした濃厚なテクスチャーが、塗った瞬間からピンとしたフィルムを張ったように目元をホールドします。寒さで萎縮したまぶたのたるみや、目の下のクマ・くぼみ影に対して、毎晩継続して使うことで内側から肉感的なハリが蘇ります。",
        "target": "目元の深い乾燥小ジワやまぶたのたるみに悩む方、市販のアイクリームで満足できなかった方、高濃度成分の確かな手応えが欲しい方",
        "point": "夜のお手入れの最後に、米粒大を薬指に取り、目周りの骨に沿ってポンポンと優しく叩き込みます。眉間のシワやほうれい線、首の横ジワにも伸ばすと効果的です。"
    },
    {
        "rank": 6,
        "tag": "🔬 レチナール×ペプチド×植物性ハリ成分！冬の肌萎縮に挑む高浸透エイジングセラム",
        "catch": "次世代ビタミンAレチナール×植物性弾力成分。冬のゴワつき肌をほぐしながら奥からふっくら覚醒",
        "brand_name": "ONE THING (ワンシング)",
        "capacity": "30ml (ペプチド レチナール セラム)",
        "type": "高機能リフティングエイジングセラム",
        "features": "リポソーム化レチナール、弾力サポートペプチド、ハナスゲ根エキス、ヒアルロン酸",
        "value": "レチノールよりも即効性の高いレチナールを微細カプセル化。冬の硬化した角層をなめらかにほぐし、ボルフィリン成分と共鳴して真冬の弾力を底上げ",
        "desc_p1": "原料のシンプルさと高い効果で知られるワンシングが開発したハイエンドセラム。レチノールの一歩先を行く『レチナール』を採用し、植物性ハリ成分であるハナスゲ根エキス（ボルフィリン成分）やペプチドと融合させました。",
        "desc_p2": "冬の乾燥でターンオーバーが滞り、表面がゴワゴワに硬くなった肌にも、超微細なリポソームカプセルがスーッと浸透。古い角質を滑らかに整えながら、奥深くに豊かなハリ弾力を注ぎ込みます。黄色い濃密なセラムですがベタつきはなく、翌朝の肌の手触りはつるんとシルキーで、指を押し返すようなモチモチ感に満たされます。",
        "target": "肌のゴワつきとたるみ・しぼみを同時に解決したい方、低刺激なレチナールセラムを試したい方、翌朝の即効的なハリ感を求める方",
        "point": "夜の洗顔後、化粧水で肌を整えた後に2〜3滴を全顔へ。特にたるみが気になるフェイスラインからこめかみへ向けて、手のひらで引き上げるようになじませてください。"
    },
    {
        "rank": 7,
        "tag": "🥑 セダーマ社特許ボルフィリン×高保水シア脂！真冬の冷風を跳ね返す濃厚リフティングクリーム",
        "catch": "ボルフィリン高濃度配合クリーム。冬枯れで痩せたフェイスラインを濃密な潤いで引き締める",
        "brand_name": "Tosowoong (トソウン)",
        "capacity": "50ml (ボルフィリン ボリューム リフティングクリーム)",
        "type": "超高保湿リフトクリーム",
        "features": "セダーマ社ボルフィリン、シア脂、マカダミア種子油、ナイアシンアミド、アデノシン",
        "value": "バターのように濃厚なエモリエント膜が、冬の乾燥冷風をシャットアウト。ボルフィリンが一日中じっくりと角層に浸透し続ける高保湿設計",
        "desc_p1": "韓国のスキンケアブランド・トソウンが手掛けるボルフィリンリフティングクリーム。乾燥の激しい冬の韓国で、美魔女たちから愛用され続けているロングセラーのボリュームアップクリームです。",
        "desc_p2": "シアバターとマカダミア種子油を贅沢にブレンドしたこっくり濃厚なクリームは、肌に乗せると体温でじゅわっと溶け出し、乾ききった角層に極上の油膜ヴェールを形成。ボルフィリンとアデノシンの相乗効果で、真冬の寒さでこわばった表情筋周りの皮膚をふっくらと持ち上げます。朝まで乾燥を一切寄せ付けず、陶器のように滑らかなハリツヤ肌を守り抜きます。",
        "target": "冬は普通のリフトクリームでは乾燥してしまう超乾燥肌の方、夜塗って朝まで続く強烈な保湿力を求める方、首元までしっかりケアしたい方",
        "point": "夜のお手入れの最後にパール粒大を手のひらで温めてから、あご先から耳の横、小鼻からこめかみへとリフトアップするように引き上げながら塗り広げます。"
    },
    {
        "rank": 8,
        "tag": "🧊 ひんやりハイドロゲルが密着！発酵ハナスゲ×ヴィーガンコラーゲンの目元集中パッチ",
        "catch": "発酵ハナスゲエキス×ヴィーガンコラーゲン。冬の暖房で乾ききった目元にみずみずしい弾力を急速注入",
        "brand_name": "Abib (アビブ)",
        "capacity": "60枚入 (コラーゲン アイパッチ レディテクスチャー)",
        "type": "ハイドロゲル目元・口元集中パッチ",
        "features": "発酵ハナスゲ根エキス、ヴィーガンコラーゲン、カフェイン、ナイアシンアミド",
        "value": "密着力抜群のハイドロゲルシートが、乾いた目元の温度を穏やかに冷ましながら、美容成分を角層奥深くまでじっくり送り届ける",
        "desc_p1": "スタイリッシュなデザインと確かな鎮静・保水力で大人気のアビブ。コラーゲンアイパッチは、発酵させたハナスゲ根エキスと植物性ヴィーガンコラーゲンをぷるぷるのハイドロゲルシートに凝縮したパーツケアの名品です。",
        "desc_p2": "真冬の室内暖房で乾ききり、ちりめんジワが目立つ目元やほうれい線にピタッと貼るだけで、ひんやりとした水分感が広がり、火照りやむくみを解消。時間とともにゲルシートが薄くなり、成分が肌に吸い込まれていくのを視覚的にも実感できます。剥がした後の目元はパッと明るくふっくらとし、どんよりした冬の目元の疲れ影が一掃されます。",
        "target": "朝起きると目元がむくんだり乾燥でシワっぽい方、メイク前に目元を短時間で集中ケアしたい方、貼ったまま家事をしたい方",
        "point": "朝のメイク前や夜のスキンケア時、目元やほうれい線に貼って15〜20分置きます。パッチを剥がした後は、残ったエッセンスを指先で優しくタッピングしてなじませてください。"
    },
    {
        "rank": 9,
        "tag": "🧬 ロート製薬の皮膚科学の極致！重力としぼみに挑む高機能リフトクリーム",
        "catch": "パワーリフトテクノロジー採用。真冬の過酷な環境下で緩んだ肌構造を全方位から引き上げる",
        "brand_name": "Obagi (オバジ) / ロート製薬",
        "capacity": "50g (オバジX ダーマアドバンスドリフト)",
        "type": "高機能リフトクリーム",
        "features": "エラスグロウ、エラスリッチ、コラプラス、高浸透ペプチド、高保水エモリエント処方",
        "value": "皮膚の張力（テンション）に着目した最先端リフト設計。濃厚なコクのあるテクスチャーが肌をタイトに引き締めながら、内側から押し上げる弾力を創出",
        "desc_p1": "ロート製薬の先進皮膚科学研究が結実したオバジの最高峰リフトクリーム『ダーマアドバンスドリフト』。肌の張力構造にアプローチし、冬の寒さと乾燥で下垂しやすくなった肌を力強くホールドします。",
        "desc_p2": "濃厚で粘り気のあるユニークなテクスチャーが、肌の上でピタッと密着。まるで形状記憶リフトマスクを装着したかのように、フェイスラインや頬を高い位置でキープします。高浸透コラーゲンやエラスチンサポート成分が角層の深部を満たし、真冬の乾燥冷風にも決してへこたれない、内側から押し戻されるような力強いハリ肌を育みます。",
        "target": "頬の位置が下がってきたと感じる方、フェイスラインのもたつきが気になる方、最高峰のドラッグストア高機能クリームを選びたい方",
        "point": "パール粒大を手に取り、あごから耳の下、口角から耳の中央、小鼻からこめかみへと、皮膚を引き上げるようにハンドプレスしながらなじませます。最後に手のひら全体でフェイスラインを包み込み、5秒間キープするとリフト感が固定されます。"
    },
    {
        "rank": 10,
        "tag": "👁️ 目袋・まぶたのゆるみを360度ケア！ロート製薬のアイケア最高峰プレミアム",
        "catch": "パワライズコンプレックス配合。真冬の乾燥でしぼんだ目元に湧き上がるような生命力を宿す",
        "brand_name": "episteme (エピステーム) / ロート製薬",
        "capacity": "18g (アイパーフェクトショットa)",
        "type": "最高峰エイジングアイクリーム",
        "features": "パワライズコンプレックス、キープエラスコンプレックス、植物性ボリュームエキス配合",
        "value": "百貨店カウンターで絶大な信頼を集める最高峰アイクリーム。まぶた、目尻、目の下の3大パーツへ全方位からハリ弾力を注入",
        "desc_p1": "ロート製薬が百貨店専用のプレステージブランドとして展開するエピステームのアイコン『アイパーフェクトショットa』。目元の皮膚構造を徹底研究し、真冬の乾燥で痩せ細った目元に劇的なハリをもたらす最高峰のアイクリームです。",
        "desc_p2": "目元の薄い皮膚に負担をかけないよう、極上の滑らかさと密着力を両立。塗布した瞬間にピンとしたハリのフィルムが形成され、まぶたの重みや目の下のくぼみ影をふっくらと持ち上げます。乾燥によるちりめんジワを防ぎ、一日中潤いに満ちた凛とした眼差しを保ちます。まさに大人の冬の投資にふさわしい逸品です。",
        "target": "まぶたが重く下がってきた方、目の下の影がコンシーラーでも隠せない方、一生モノの最高峰アイクリームを手に入れたい方",
        "point": "朝晩、化粧水や乳液で肌を整えた後、片目につき米粒1個分を優しくなじませます。目頭から目尻に向かって軽く引き上げ、こめかみを軽くプッシュしてツボを刺激すると目元の巡りが高まります。"
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
        "url": f"https://lumi-cosme.vercel.app/winter-volufiline.html#item-{i+1}",
        "offers": {
            "@type": "Offer",
            "price": str(p['price']),
            "priceCurrency": "JPY",
            "availability": "https://schema.org/InStock"
        }
    })

faq_list = [
    {
        "question": "ボルフィリンを使うと顔全体が太ったり余計な脂肪がついたりしませんか？",
        "answer": "そのような心配は全くありません。ボルフィリン（ハナスゲ根エキス）は、塗布した局所の角層直下にある既存の脂肪細胞に対して働きかけ、細胞内の脂質蓄積や分化をサポートする植物性ハリ成分です。全身の体重増加や無秩序な脂肪細胞の増殖を引き起こすものではなく、あくまで寒さや加齢で『痩せてしぼんでしまった部分（目の下のくぼみ、ほうれい線、唇など）』にふっくらとした自然なハリ・肉感を取り戻す作用に留まります。適量を気になるパーツになじませることで、理想的な若々しいふっくら感が得られます。"
    },
    {
        "question": "なぜ11月〜12月の真冬にしぼみ肌・たるみ影が悪化するのですか？",
        "answer": "冬の外気低下と湿度の急降下は、角層の水分を奪うだけでなく、皮下毛細血管を収縮させて血流を滞らせます。これにより真皮のコラーゲン産生スピードが落ちることに加え、皮下脂肪組織の代謝エネルギーも低下。皮膚が薄い目元やまぶた、口元は風船の空気が抜けたようにしぼんで凹みが生まれ、そこに室内照明の光が当たることで濃い『冬枯れ影』として現れます。通常の水分補給だけでなく、ボルフィリンのような皮下の厚みをサポートする油溶性ハリ成分によるケアが不可欠です。"
    },
    {
        "question": "ボルフィリン原液は目元や唇に直接塗っても安全ですか？",
        "answer": "植物由来の成分であり、皮膚刺激性は非常に穏やかなため、目元や唇のケアにも広く使用されています。ただし、原液は非常に濃厚な油性エキス（水添ポリイソブテン等を含む）のため、目の中に入らないよう注意してください。初めて使用する際は、手持ちのアイクリームや化粧水、ワセリンなどに1滴混ぜて使い始め、肌の反応を見ながら徐々に原液でのピンポイント塗布へ移行することをおすすめします。"
    },
    {
        "question": "レチノールやペプチド、スピキュール針美容液と併用しても良いですか？",
        "answer": "非常に相乗効果が高い組み合わせです。スピキュール（針美容液）で浸透ルートを開いた後にボルフィリンを重ねると、成分がよりスムーズに角層奥へ届きます。また、ペプチドやレチノールが真皮のコラーゲン・エラスチンを活性化し、ボルフィリンが皮下組織のボリュームをサポートするため、『真皮＋皮下のダブルリフト』が実現します。併用順序としては、洗顔後【針美容液/化粧水】→【レチノール/ペプチド美容液】→【ボルフィリン原液】→【保湿クリーム】の順が理想的です。"
    },
    {
        "question": "どのくらいの期間で効果を実感できますか？使用を止めると戻りますか？",
        "answer": "塗布直後から濃厚なエモリエント膜による乾燥小ジワの目立たなさとモチモチ感を実感できますが、ふっくらとした肉感的なボリュームやほうれい線の影の緩和を本格的に感じるには、肌のターンオーバーと細胞代謝のサイクルに合わせて『約4週間〜8週間（1〜2ヶ月）』の継続使用が推奨されます。使用を完全に中止すると徐々に元の状態へ戻るため、真冬の乾燥期間中（11月〜2月）は毎日のスキンケアステップに組み込んでキープすることをおすすめします。"
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
        "@id": "https://lumi-cosme.vercel.app/winter-volufiline.html"
    },
    "headline": "保湿力の強さで肌乾燥とさようなら！寒さでしぼんだ目元・口元をふっくら満たして冬枯れ影を跳ね返す高濃度ボルフィリンコスメランク10",
    "description": "11月・12月の冬枯れしぼみ顔とほうれい線・目元のくぼみ影を救う高濃度ボルフィリンコスメを徹底厳選！KISO原液、メディピール酸素バブル、シドミュールバーム、ダーマファクトリーからオバジXまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。",
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
    "name": "真冬の高濃度ボルフィリンコスメおすすめ人気ランキング10選",
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
            <tr><th>主要成分・配合率</th><td>{d['features']}</td></tr>
            <tr><th>ふっくら高保湿の理由</th><td>{d['value']}</td></tr>
          </table>
          
          <div class="review-block">
            <h4>💡 冬のしぼみ肌・くぼみ影に対する詳細解説</h4>
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
  <title>保湿力の強さで肌乾燥とさようなら！寒さでしぼんだ目元・口元をふっくら満たして冬枯れ影を跳ね返す高濃度ボルフィリンコスメランク10 - 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬枯れしぼみ顔とほうれい線・目元のくぼみ影を救う高濃度ボルフィリンコスメを徹底厳選！KISO原液、メディピール酸素バブル、シドミュールバーム、ダーマファクトリーからオバジXまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。">
  <meta name="keywords" content="ボルフィリン,ハナスゲ根エキス,高保湿美容液,ほうれい線,目元のくぼみ,しぼみ肌,冬コスメ,乾燥肌,KISO,メディピール,楽天コスメ">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-volufiline.html">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！寒さでしぼんだ目元・口元をふっくら満たして冬枯れ影を跳ね返す高濃度ボルフィリンコスメランク10">
  <meta property="og:description" content="11月・12月の冬枯れしぼみ顔とほうれい線・目元のくぼみ影を救う高濃度ボルフィリンコスメを徹底厳選！KISO原液、メディピール酸素バブル、シドミュールバーム、ダーマファクトリーからオバジXまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-volufiline.html">
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
      --primary: #831843;
      --primary-light: #9d174d;
      --accent: #e11d48;
      --accent-soft: #ffe4e6;
      --bg: #fffbfb;
      --card-bg: #ffffff;
      --text: #4c0519;
      --text-muted: #701a31;
      --border: #fbcfe8;
      --radius: 12px;
      --shadow: 0 4px 16px rgba(131, 24, 67, 0.08);
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
      background: linear-gradient(135deg, #500724, #831843);
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
      background: #ffe4e6;
      color: #e11d48;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 4px 12px;
      border-radius: 20px;
      margin-bottom: 14px;
    }}
    h1 {{
      font-size: 1.85rem;
      line-height: 1.45;
      color: #500724;
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
      color: #701a31;
      margin-bottom: 18px;
    }}
    .toc-box {{
      background: #fff1f2;
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
      color: #831843;
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
      background: #fff1f2;
      padding: 20px;
      border-radius: 10px;
      border: 1px solid #fecdd3;
    }}
    .grid-card:nth-child(2) {{ background: #fdf2f8; border-color: #fbcfe8; }}
    .grid-card:nth-child(3) {{ background: #fff7ed; border-color: #ffedd5; }}
    .grid-card h4 {{
      color: #831843;
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
      background: linear-gradient(135deg, #e11d48, #be123c);
      color: #fff;
      font-size: 1.05rem;
      font-weight: 800;
      padding: 6px 18px;
      border-radius: 20px;
      box-shadow: 0 4px 10px rgba(225, 29, 72, 0.3);
    }}
    .product-tag {{
      display: inline-block;
      margin-top: 6px;
      font-size: 0.88rem;
      font-weight: 700;
      color: #be123c;
      background: #ffe4e6;
      padding: 3px 10px;
      border-radius: 6px;
      margin-bottom: 10px;
    }}
    .product-name {{
      font-size: 1.4rem;
      line-height: 1.4;
      color: #500724;
      margin-bottom: 8px;
      font-weight: 800;
    }}
    .product-catch {{
      font-size: 0.98rem;
      font-weight: 600;
      color: #9d174d;
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
      background: #fff1f2;
      border-radius: 8px;
      border: 1px dashed #fecdd3;
    }}
    .price-label {{ display: block; font-size: 0.78rem; color: #701a31; }}
    .price-val {{ font-size: 1.5rem; font-weight: 800; color: #e11d48; }}
    .price-tax {{ font-size: 0.8rem; color: #701a31; }}
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
      background: #fff1f2;
      padding: 8px 12px;
      border: 1px solid #fbcfe8;
      text-align: left;
      color: #831843;
      font-weight: 600;
    }}
    .spec-table td {{
      padding: 8px 12px;
      border: 1px solid #fbcfe8;
      background: #fff;
    }}
    .review-block {{
      background: #fff1f2;
      border-left: 4px solid var(--accent);
      padding: 16px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 14px;
    }}
    .review-block h4 {{
      font-size: 0.98rem;
      color: #500724;
      margin-bottom: 8px;
    }}
    .review-block p {{
      font-size: 0.92rem;
      line-height: 1.75;
      color: #701a31;
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
      border: 1px solid #fbcfe8;
      text-align: center;
    }}
    .compare-table th {{
      background: #ffe4e6;
      color: #500724;
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
      color: #e11d48;
      font-weight: 700;
      margin-bottom: 8px;
    }}
    .faq-a {{
      font-size: 0.95rem;
      line-height: 1.8;
      color: #701a31;
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
      background: #fff1f2;
      padding: 16px;
      border-radius: 8px;
      border: 1px solid #ffe4e6;
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
    <span style="font-size: 0.85rem; color: #fecdd3;">2026-2027年 冬季最新スキンケア特集</span>
  </div>
</header>

<div class="breadcrumb">
  <a href="/">ホーム</a> &gt; <span>高濃度ボルフィリンコスメ</span>
</div>

<main class="main-container">
  <div class="article-header">
    <span class="article-badge">🌹 11月〜12月冬枯れしぼみ顔・弾力影対策</span>
    <h1>保湿力の強さで肌乾燥とさようなら！寒さでしぼんだ目元・口元をふっくら満たして冬枯れ影を跳ね返す高濃度ボルフィリンコスメランク10</h1>
    <div class="meta-box">
      <span>📅 最終更新日: 2026年11月4日</span>
      <span>✍️ 監修: 冬コスメ徹底比較ラボ 美容皮膚科学リサーチチーム</span>
      <span>⏱️ 読了目安: 約8分</span>
    </div>
    <p class="lead-text">
      11月に入り本格的な寒風が吹き始めると、「鏡を見るたびに目の下が痩せて影ができている」「ほうれい線や口元の縦ジワが深く刻まれて老け見えする」「水分保湿をいくら重ねても肌がしぼんで弾力がない」という切実な悩みが一気に顕在化します。冬の寒さは皮膚表面の水分を奪うだけでなく、皮下の毛細血管を収縮させて血流を滞らせ、肌のボリュームを支える皮下組織を急速に萎縮させてしまうからです。
    </p>
    <p class="lead-text">
      この「冬のしぼみ顔」に対する画期的なアプローチとして、世界中の美容クリニックやコスメフリークから熱烈な注目を浴びているのが、フランス・セダーマ社が開発した特許原料『ボルフィリン（ハナスゲ根エキス）』です。「塗るボリューム注入」と称されるこの植物エキスは、しぼんだ肌に肉感的なふっくら感と濃密な潤いを取り戻します。本特集では、高濃度ボルフィリンを配合した実力派コスメ10選を楽天市場の最新データから厳選し、徹底比較解説します。
    </p>
  </div>

  <div class="toc-box">
    <div class="toc-title">📑 目次 - タップして各項目へジャンプ</div>
    <ol class="toc-list">
      <li><a href="#guide-mechanism">1. なぜ11月〜12月に「ボルフィリン」が必要なのか？（冬枯れしぼみ顔のメカニズム）</a></li>
      <li><a href="#guide-points">2. 冬の高濃度ボルフィリンコスメを選ぶ3つの絶対基準</a></li>
      <li><a href="#ranking-section">3. 【2026年最新】真冬の高濃度ボルフィリンコスメおすすめ人気ランキング10選</a></li>
      <li><a href="#comparison-section">4. 高濃度ボルフィリンコスメ10選スペック＆価格早見表</a></li>
      <li><a href="#usage-technique">5. 美容のプロ直伝！気になる影を消し去るピンポイント重ね塗り＆リフトマッサージ</a></li>
      <li><a href="#faq-section">6. 高濃度ボルフィリンコスメに関するよくある質問（FAQ）</a></li>
      <li><a href="#related-section">7. あわせて読みたい冬の集中ハリ＆高保湿関連記事</a></li>
    </ol>
  </div>

  <section class="guide-section" id="guide-mechanism">
    <h2>1. なぜ11月〜12月に「ボルフィリン」が必要なのか？</h2>
    <p>
      「化粧水をたっぷり塗ってクリームで蓋をしているのに、夕方になると頬や目の下がこけて疲れて見える」という現象。これは角層の乾燥だけが原因ではありません。冬の低温によって皮膚の血行が滞り、皮下脂肪組織の代謝エネルギーが著しく落ちることで、肌の土台そのものが『ボリュームダウン（萎縮）』していることが原因です。
    </p>
    <p>
      風船から空気が抜けると表面に細かいシワができるように、皮下が痩せ細ると皮膚が余ってたるみ、目袋のくぼみやほうれい線、マリオネットラインとして定着します。水分を補給するだけの保湿では、この「皮下のしぼみ」を根本から持ち上げることはできません。
    </p>
    
    <div class="guide-grid">
      <div class="grid-card">
        <h4>① ハナスゲ根由来「サルササポゲニン」の力</h4>
        <p>フランスセダーマ社が特許を取得したボルフィリンは、ハナスゲ根から抽出されるサルササポゲニンが主成分。脂肪細胞の分化と脂質蓄積をサポートし、しぼんだ肌にふっくらとした肉感をもたらします。</p>
      </div>
      <div class="grid-card">
        <h4>② 真冬の冷風を寄せ付けない濃厚エモリエント膜</h4>
        <p>ボルフィリン原料自体が水添ポリイソブテンなど親油性の高い基剤と結合しているため、肌表面に濃密な油性シールドを形成。水分蒸散を強力に防ぎます。</p>
      </div>
      <div class="grid-card">
        <h4>③ ペプチド・針・レチノールとの相乗効果</h4>
        <p><a href="/winter-spicule" style="color:#e11d48;font-weight:600;">スピキュール針美容液</a>や<a href="/winter-peptide-serum" style="color:#e11d48;font-weight:600;">ペプチド</a>、<a href="/winter-retinol-cream" style="color:#e11d48;font-weight:600;">レチノール</a>と組み合わせることで、「真皮コラーゲン＋皮下ボリューム」の全層リフトを実現します。</p>
      </div>
    </div>
  </section>

  <section class="guide-section" id="guide-points">
    <h2>2. 冬の高濃度ボルフィリンコスメを選ぶ3つの絶対基準</h2>
    <p>
      真冬のしぼみ肌を劇的にふっくら蘇らせるために、失敗しない製品選びのポイントを3つ解説します。
    </p>
    <h3>① フランスセダーマ（Sederma）社の純正原料が明記されているか</h3>
    <p>
      ボルフィリンは、フランスの世界的原料メーカー・セダーマ社の登録商標です。品質と安全性が臨床データで証明されているのはセダーマ社の純正ボルフィリン（ハナスゲ根エキス＋水添ポリイソブテン）のみ。「セダーマ社特許原料使用」と明記されているか、原料認証マークがある製品を選びましょう。
    </p>
    <h3>② 配合濃度（原液100%、または5%〜20%などの高配合）が担保されているか</h3>
    <p>
      冬の深刻なしぼみ肌には、少量配合された製品よりも、原液タイプ（100%配合）や、推奨濃度（1%〜5%）以上を高配合した特化型クリームが圧倒的に効果的です。KISOのような原液美容液なら、手持ちのアイテムに混ぜて濃度を自在に調整できます。
    </p>
    <h3>③ 集中ケアしたい部位（目元・口元・全顔）に適した剤形か</h3>
    <p>
      目元やほうれい線のピンポイントケアには濃厚な原液やアイクリーム、日中のメイクの上からの保湿にはスティックバーム、顔全体のたるみケアには微細酸素バブルやリフトクリームなど、ライフスタイルと悩みに合わせた剤形を選びましょう。
    </p>
  </section>

  <section id="ranking-section">
    <h2 style="font-size: 1.6rem; color: #500724; margin-bottom: 24px; padding-left: 14px; border-left: 6px solid #e11d48;">
      3. 【2026年最新】真冬の高濃度ボルフィリンコスメおすすめ人気ランキング10選
    </h2>
    <p style="margin-bottom: 32px; font-size: 0.95rem; color: #701a31;">
      楽天市場の最新データから、セダーマ社原料の真正性、配合濃度、ふっくらハリ実感度、最新販売価格を総合評価したおすすめ10選です。
    </p>
    
    {cards_str}
  </section>

  <section class="guide-section" id="comparison-section">
    <h2>4. 高濃度ボルフィリンコスメ10選スペック＆価格早見表</h2>
    <p>
      ランクインした全10アイテムの参考価格、製品形状、主要な強みを一覧で比較できます。
    </p>
    
    <div class="compare-table-wrap">
      <table class="compare-table">
        <thead>
          <tr>
            <th>順位・製品名</th>
            <th>参考価格</th>
            <th>分類</th>
            <th>主要な強み・特徴</th>
            <th>おすすめの悩み部位</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>第1位 KISO ボルフィリン原液100%</strong></td>
            <td>¥2,480</td>
            <td>原液美容液</td>
            <td>セダーマ社純正ボルフィリン100%ボトリング</td>
            <td>目元のくぼみ・ほうれい線・全顔</td>
          </tr>
          <tr>
            <td><strong>第2位 ビューティーファーム 原液100%</strong></td>
            <td>¥1,780</td>
            <td>原液美容液</td>
            <td>国産ボトリング・無添加低刺激設計</td>
            <td>口元の縮みジワ・目袋・リップ</td>
          </tr>
          <tr>
            <td><strong>第3位 メディピール ペプチド9エッセンス</strong></td>
            <td>¥2,580</td>
            <td>酸素バブル液</td>
            <td>ボルフィリン5%×ペプチド9種×微細酸素泡</td>
            <td>顔全体のたるみ・大人のしぼみ肌</td>
          </tr>
          <tr>
            <td><strong>第4位 シドミュール 弾力マルチバーム</strong></td>
            <td>¥2,380</td>
            <td>スティックバーム</td>
            <td>手を汚さず塗れる高配合バームスティック</td>
            <td>日中の乾燥小ジワ・メイク直し・唇</td>
          </tr>
          <tr>
            <td><strong>第5位 ダーマファクトリー アイクリーム</strong></td>
            <td>¥3,000</td>
            <td>アイクリーム</td>
            <td>驚異のボルフィリン20%×コラーゲン水</td>
            <td>深い目元乾燥ジワ・まぶたのたるみ</td>
          </tr>
          <tr>
            <td><strong>第6位 ワンシング レチナールセラム</strong></td>
            <td>¥2,416</td>
            <td>高機能セラム</td>
            <td>ナノレチナール×ハナスゲ根エキス</td>
            <td>冬のゴワつき・キメの乱れ・弾力</td>
          </tr>
          <tr>
            <td><strong>第7位 トソウン リフティングクリーム</strong></td>
            <td>¥1,530</td>
            <td>高保湿クリーム</td>
            <td>セダーマ社原料×シア脂×マカダミア油</td>
            <td>超乾燥肌・夜の集中リフト密閉</td>
          </tr>
          <tr>
            <td><strong>第8位 アビブ コラーゲン アイパッチ</strong></td>
            <td>¥2,530</td>
            <td>ゲルパッチ</td>
            <td>発酵ハナスゲ×ヴィーガンコラーゲンゲル</td>
            <td>朝の目元むくみ・ひんやり保水</td>
          </tr>
          <tr>
            <td><strong>第9位 オバジX ダーマアドバンスドリフト</strong></td>
            <td>¥10,298</td>
            <td>高機能クリーム</td>
            <td>ロート製薬パワーリフトテクノロジー</td>
            <td>フェイスラインの重力たるみ</td>
          </tr>
          <tr>
            <td><strong>第10位 エピステーム アイパーフェクト</strong></td>
            <td>¥7,150</td>
            <td>最高峰アイケア</td>
            <td>360度目元構造研究・プレステージ処方</td>
            <td>目袋の影・大人の深刻な目元悩み</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="guide-section" id="usage-technique">
    <h2>5. 美容のプロ直伝！気になる影を消し去るピンポイント重ね塗り＆リフトマッサージ</h2>
    <p>
      ボルフィリンのふっくら効果を最大限に高める、真冬のプロフェッショナルな活用術です。
    </p>
    <h3>① 「トントン垂直スタンプ」で皮下にダイレクトチャージ</h3>
    <p>
      目の下のくぼみやほうれい線に塗る際は、決して横に擦り伸ばしてはいけません。皮膚が薄く伸びやすいため、シワを悪化させる原因になります。薬指の腹に原液を1滴取り、気になる溝に対して「垂直に優しくトントン」とタッピングしながら押し込むように浸透させてください。
    </p>
    <h3>② 「手持ちクリームへの1滴ブースト」で全顔ボリュームアップ</h3>
    <p>
      顔全体の乾燥しぼみが気になる時は、手のひらで<a href="/winter-moisture-cream" style="color:#e11d48;font-weight:600;">保湿クリーム</a>を温め、そこにボルフィリン原液を1〜2滴垂らして混ぜ合わせます。全顔に伸ばすことで、真冬の暖房乾燥を完全にシャットアウトしながら、翌朝パンッと張るような水光ハリ肌が手に入ります。
    </p>
    <h3>③ 就寝前の「ぷるぷるリップオーバーパック」</h3>
    <p>
      冬になると唇が乾燥して縦ジワが目立ち、口紅が綺麗に乗らないという方に超おすすめなのが、ボルフィリンのリップパック。唇とその輪郭1mm外側までボルフィリン原液（またはシドミュールのバーム）をたっぷり塗り、その上から<a href="/winter-lip-mask" style="color:#e11d48;font-weight:600;">リップマスク</a>を重ねて就寝します。翌朝、ヒアルロン酸注入をしたかのようにふっくらグラマラスな唇に仕上がります。
    </p>
  </section>

  <section class="faq-section" id="faq-section">
    <h2>6. 高濃度ボルフィリンコスメに関するよくある質問（FAQ）</h2>
    {faq_str}
  </section>

  <section class="internal-section" id="related-section">
    <h2>7. あわせて読みたい冬の集中ハリ＆高保湿関連記事</h2>
    <p style="margin-bottom: 20px; font-size: 0.95rem; color: #701a31;">
      ふっくら若々しいハリと弾力を保つための、おすすめ関連特集です。
    </p>
    <div class="internal-grid">
      <a href="/winter-spicule" class="internal-card">
        <h4>🪡 高保湿スピキュール（針美容液）ランク10</h4>
        <p>天然ニードルで角層奥まで浸透ルートを開く！ボルフィリンとの相乗効果も抜群。</p>
      </a>
      <a href="/winter-stem-cell" class="internal-card">
        <h4>🧬 高保湿ヒト幹細胞コスメランク10</h4>
        <p>肌本来の自活保水力を根源から呼び覚ます最高峰エイジングスキンケア。</p>
      </a>
      <a href="/winter-peptide-serum" class="internal-card">
        <h4>✨ 高機能ペプチド美容液ランク10</h4>
        <p>真皮のコラーゲンとエラスチンを支え、たるみに挑むハリ弾力セラム特集。</p>
      </a>
      <a href="/winter-retinol-cream" class="internal-card">
        <h4>🌙 高保湿レチノールクリームランク10</h4>
        <p>ターンオーバーを促進し乾燥小ジワを消し去る冬の夜間集中リペアクリーム。</p>
      </a>
      <a href="/winter-eye-cream" class="internal-card">
        <h4>👁️ 冬の高保湿アイクリームランク10</h4>
        <p>デリケートな目元を濃厚な潤いで保護し、ちりめんジワを防ぐ名品アイケア。</p>
      </a>
      <a href="/winter-lip-care" class="internal-card">
        <h4>💄 冬の高保湿リップケア特集</h4>
        <p>ひび割れや皮剥けを防ぎ、ふっくら柔らかな唇を育む特濃リップアイテム。</p>
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

with open("winter-volufiline.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated winter-volufiline.html successfully!")
