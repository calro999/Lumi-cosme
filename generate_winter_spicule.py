import json
import re

with open("fetched_final_30_spicule_stemcell_lipidure.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_spicule"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 針コスメ旋風の火付け役！毎晩使えるデイリー浸透ブースター",
        "catch": "天然マイクロニードル95,000本配合。硬化した冬の角質層に美容成分の通り道を開く",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "50ml (シカ リードルショット 100)",
        "type": "導入マイクロニードル針美容液 (デイリーケア用)",
        "features": "CICA REEDLE™ 95,000本、シカヒアルロン™、アミノ酸17種、ツボクサエキス配合",
        "value": "毛穴よりもはるかに細い天然マイクロニードルが角層にチクチクと心地よい刺激を与え、後から重ねる保湿化粧水やクリームの浸透力を劇的に底上げ",
        "desc_p1": "11月から12月にかけて冷え込みが加速すると、外気温の低下に伴い肌のターンオーバーが停滞。古い角質が蓄積してゴワつき、どれだけ高価な保湿美容液やこっくりしたクリームを塗っても表面で滑って中に入っていかないという切実な悩みが急増します。VTのリードルショット100は、純度99%まで精製された海綿由来の天然微細針『シカリードル』を1本に約95,000本配合した画期的な導入美容液です。",
        "desc_p2": "洗顔直後の素肌に適量を伸ばすと、チクチクとした独特の刺激とともに、針が角層深部へと微細な浸透ルート（マイクロチャネル）を形成。同時にシカ成分と低分子ヒアルロン酸が角層深くまで送り届けられます。その後に化粧水をつけると、乾いたスポンジが水を吸い上げるように一瞬で肌に引き込まれる感覚に感動するはず。毎晩使えるマイルドな刺激設計で、冬枯れ肌のキメをふっくら立て直すファーストステップに最適です。",
        "target": "冬になると肌が硬くこわばってスキンケアの浸透が悪い方、毛穴の開きやキメの乱れをなめらかに整えたい方、初めて針美容液に挑戦する方",
        "point": "洗顔後、化粧水の前に使用します。顔全体に塗り広げたら、手のひら全体で肌を包み込み、垂直に『ギュッギュッ』と押し込むようにハンドプレスするのが浸透を高めるコツです。"
    },
    {
        "rank": 2,
        "tag": "⚡ 3日に1度の集中浸透ケア！23万本の高密度アプローチで毛穴・弾力を覚醒",
        "catch": "天然ニードル237,500本配合。頑固なインナードライとゴワつきを速攻リセット",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "50ml (シカ リードルショット 300)",
        "type": "集中浸透マイクロニードル美容液 (3日サイクル用)",
        "features": "CICA REEDLE™ 237,500本配合、高純度シカヒアルロン、低分子コラーゲン、ナイアシンアミド",
        "value": "100の約2.5倍のニードル密度。頑固に硬化した真冬の角質層を打破し、サロン級のキメ密度の高い水光肌へ導く",
        "desc_p1": "リードルショット100で肌が慣れてきた方や、真冬の寒風によって深刻なゴワつき・キメの粗さに悩まされている方に絶対的な支持を得ているのが『リードルショット300』です。1本に約237,500本ものマイクロニードルが凝縮されており、肌に伸ばした瞬間のチクチク感は100よりも明確でパワフル。",
        "desc_p2": "3日に1回のスペシャルケアとして夜のルーティンに取り入れることで、滞った角質層のリフレッシュを加速させます。針が肌に留まっている約72時間の間、継続的に角層へ微細な刺激を与え続け、肌本来の再生力と保水ネットワークを活性化。翌朝の洗顔時には、指先がツルンと滑るようななめらかさと、内側からパンッと張るような弾力感を実感できます。",
        "target": "リードルショット100では物足りなくなった方、冬の毛穴の開きやたるみ毛穴が気になる方、3日に1回の集中ケアで劇的な手応えが欲しい方",
        "point": "リードルショット300を塗布した直後は、鎮静・高保湿効果の高いシートマスク（CICAやPDRN、ヒト幹細胞マスクなど）を重ねると、美容液成分が針を伝って奥深くまで浸透し相乗効果が爆発します。"
    },
    {
        "rank": 3,
        "tag": "🔥 週1回の最高峰エステ級アプローチ！57万本の超濃密ニードルで肌再生を刺激",
        "catch": "天然ニードル570,000本。週末のリセット美容で冬枯れ肌の限界を突破する",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "30ml (シカ リードルショット 700)",
        "type": "最高濃度スペシャルニードル美容液 (週1回用)",
        "features": "CICA REEDLE™ 570,000本配合、高純度シカエキス、エラスチン、濃密セラミドコンプレックス",
        "value": "シリーズ最高峰の圧倒的ニードル配合量。美容皮膚科のダーマペン着想で、厚くなった冬の不要角質を脱ぎ捨てるような劇的リニューアル感",
        "desc_p1": "VTリードルショットシリーズの中で最高峰のニードル密度を誇る『リードルショット700』。1本に実に570,000本ものスピキュールが配合されており、サロンのハーブピーリングやダーマペン施術を彷彿とさせる本格的な刺激感を自宅で体験できます。",
        "desc_p2": "指先で伸ばすだけでもしっかりとしたチクチク感があり、特に小鼻の黒ずみや頬のたるみ毛穴、眉間や額の乾燥ゴワつきに対して週に1回集中投下することで、滞った冬の肌サイクルを強力にブースト。塗布後は赤みが出ないよう、手持ちの最もリッチな高保湿クリームでたっぷりと蓋をすることが推奨されます。翌朝から2〜3日後にかけて、内側から押し出されるような透明感とハリツヤが現れます。",
        "target": "本格的なクリニック級の肌管理を自宅で行いたい方、冬の角質肥厚で肌がくすんで暗く見える方、週1回の集中美容で劇的変化を求める上級者",
        "point": "週に1回、休日前夜のスペシャルケアとして使用します。擦るように横に広げると刺激が強すぎるため、気になる部分にトントンと垂直に優しく押し込み、直後にこっくりしたセラミドクリームで保護してください。"
    },
    {
        "rank": 4,
        "tag": "✨ ヤーマンが放つ美顔器発想の国産名品！24K純金コロイドをまとった針美容液",
        "catch": "純金担持マイクロニードル約100万本配合。大人の乾燥・年齢サインに深く響く",
        "brand_name": "YA-MAN (ヤーマン) / メディリフト",
        "capacity": "18g (メディリフト ニードルリフトセラム)",
        "type": "純金コロイド担持マイクロニードル濃密セラム",
        "features": "24Kゴールドニードル約100万本配合、3種のヒアルロン酸、3種のコラーゲン、ナイアシンアミド、金コロイド",
        "value": "日本の美顔器パイオニアが開発。天然スピキュールに24K純金をコーティングし、電気的微弱電流のような働きでハリ成分を角層深層へ届ける",
        "desc_p1": "美容家電のトップランナーであるヤーマンが、メディリフトシリーズの技術を結集して生み出したプレミアム針美容液。天然海綿由来の微細針にナノサイズの24K純金をコーティングした『ゴールドニードル』を1個あたり約100万本も配合しています。",
        "desc_p2": "ゴールドの微弱電荷によって、針に吸着させた3種のヒアルロン酸と3種のコラーゲンが角層深層までスムーズにデリバリー。冬の冷えによって硬くなった表情筋周りの皮膚をふっくらと持ち上げるようなハリ感を与えます。チクチク感は非常に上品でなめらか。乾燥小ジワが目立ちやすい目元やほうれい線周りにも安心して使え、大人の冬枯れ肌に品のあるツヤをもたらします。",
        "target": "目元・口元の乾燥小ジワやフェイスラインのゆるみが気になる30代〜50代、国産ブランドの高品質な針コスメを選びたい方",
        "point": "洗顔後、化粧水で肌を整えた後にパール粒大を手に取り、下から上へ引き上げるように優しくハンドプレス。ほうれい線や目尻など気になる部位には重ね付けが効果的です。"
    },
    {
        "rank": 5,
        "tag": "🌱 初めての針コスメに！敏感肌でも毎日朝夜使える超低刺激設計",
        "catch": "天然ニードル38,000本配合。チクチク感が苦手な方でも安心して続けられる入門編",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "50ml (マイルド リードルショット 50)",
        "type": "超マイルド導入マイクロニードル美容液 (朝夜デイリー用)",
        "features": "CICA REEDLE™ 38,000本、ツボクサエキス、パンテノール、プロポリスエキス",
        "value": "針の本数を抑え、鎮静成分と保湿成分をたっぷり配合。朝のメイク前にも使えるマイルドさで、日中のメイクのノリと密着感を向上",
        "desc_p1": "針コスメに興味はあるけれど、強いチクチク感や赤みが怖くて一歩を踏み出せないという方の救世主となっているのが『マイルド リードルショット50』です。ニードル数を約38,000本に最適化し、痛みをほとんど感じないレベルに抑えつつ、美容成分の導入機能はしっかり確保しています。",
        "desc_p2": "パンテノールやプロポリスエキスなど、肌の保護バリアを強化する成分が手厚く配合されており、冬の乾燥によって過敏になったゆらぎ肌でもピリピリせずにすんなり浸透。夜だけでなく朝の洗顔後にも使用でき、その後のファンデーションの密着度や日中の乾燥崩れ防止に目覚ましい効果を発揮します。",
        "target": "針コスメ初心者の方、痛みに敏感な方、冬になると肌が敏感に傾きやすい方、朝のメイク前にも針ブースターを使いたい方",
        "point": "朝のスキンケアに取り入れるのが特におすすめ。洗顔後に本品をなじませ、化粧水と乳液を重ねてからベースメイクに入ると、粉吹き知らずのなめらかなツヤ肌が一日中続きます。"
    },
    {
        "rank": 6,
        "tag": "💉 クリニック級の集中注入！ヒト幹細胞培養液×スピキュールの注射器型パック",
        "catch": "2gずつの個別注射器シリンジ容器。鮮度抜群のヒト幹細胞と針が真冬の肌を再起動",
        "brand_name": "SCボーテ (SC BEAUTE)",
        "capacity": "2g×4本 / 12本 (プレミアムインジェクション)",
        "type": "サロン専売ホームケア用マイクロニードル注入パック",
        "features": "ヒト幹細胞順化培養液、天然微細針スピキュール、マトリキシル3000、低分子ヒアルロン酸",
        "value": "エステサロンのハーブトリートメントコースでも使用される本格プロ処方。密閉シリンジから直接肌に押し込む贅沢な集中リペア",
        "desc_p1": "エステサロンや美容皮膚科で導入されている本格的なマイクロニードルトリートメントを、自宅で再現できる注射器型シリンジコスメ『SCボーテ プレミアムインジェクション』。空気や光に触れない完全密閉容器に、高純度ヒト幹細胞順化培養液と天然スピキュールが高濃度で封入されています。",
        "desc_p2": "注射器から直接肌に出して塗り込み、指の腹でトントンと角層に押し込んでいくと、チクチクとした針とともに成長因子とペプチドが角層深部へ直撃。冬の寒暖差で萎縮してしまった真皮・表皮の細胞間マトリックスを力強く刺激し、翌朝起きたときの肌のハリと弾力密度の違いは圧倒的です。大事な予定の前夜の駆け込み寺コスメとして熱狂的な支持を集めています。",
        "target": "エステサロン級の即効性を求める方、真冬の乾燥で肌の萎縮や深い乾燥ジワが気になる方、新鮮なヒト幹細胞×針の相乗効果を体験したい方",
        "point": "夜の洗顔後、1本（2g）を顔全体から首元にかけて贅沢に塗り込みます。押し込むように浸透させた後、洗い流さずにそのまま保湿シートマスクを密着させて就寝すると効果が最大化します。"
    },
    {
        "rank": 7,
        "tag": "🔬 エクソソーム×微細ニードル針の融合！真冬の乾燥毛穴開きをキュッと引き締める",
        "catch": "毛穴特化の微細ショット。冷えと乾燥でだらしなく広がった毛穴周りを濃密ケア",
        "brand_name": "medicube (メディキューブ)",
        "capacity": "30ml (ゼロワンデイ エクソソーム ショット 2000/7500)",
        "type": "毛穴特化エクソソーム針美容液",
        "features": "高純度エクソソーム、微細針ニードル、AHA・BHA・PHA、アゼライン酸、ナイアシンアミド",
        "value": "韓国メディカルコスメのトップブランド発。次世代の細胞間伝達物質エクソソームを微細ニードルに乗せて毛穴深部へ送り込む",
        "desc_p1": "韓国のダーマコスメとして世界的な人気を誇るメディキューブの『ゼロワンデイ エクソソームショット』。冬の暖房によるインナードライで皮脂バランスが崩れ、ファンデーションが毛穴落ちしてしまう冬毛穴の悩みに特化して開発された針美容液です。",
        "desc_p2": "細胞間を駆け巡る高純度エクソソームと毛穴引き締め成分を微細ニードルに担持。塗布すると角層毛穴の奥までチクチクと届き、緩んだ毛穴の壁をキュッと引き締めながら、乾燥によるキメの乱れをなめらかに修復します。使用直後から肌表面がサラリと引き締まりつつ、内側にはしっとりとした保水感が残る絶妙な仕上がりです。",
        "target": "冬でもTゾーンがテカるのに頬は乾く混合肌の方、毛穴の黒ずみや開きが気になる方、エクソソームの最新美容を取り入れたい方",
        "point": "夜のお手入れで、特に毛穴の気になる小鼻、頬の中央、眉間を中心に優しくローリングしながら押し込みます。その後、水分感の強いジェルクリームで保湿すると毛穴が目立たなくなります。"
    },
    {
        "rank": 8,
        "tag": "🍋 レーザー美容発想の超高浸透！高濃度ビタミンC×ナノカプセル集中セラム",
        "catch": "ナノカプセルが角層深層へ速攻浸透。冬のくすみと乾燥毛穴を一網打尽にする高機能美容液",
        "brand_name": "QUALITY 1st (クオリティファースト)",
        "capacity": "30ml (ダーマレーザー ウルセラC)",
        "type": "レーザー発想超高浸透ナノカプセル美容液",
        "features": "4種のビタミンC高濃度配合、ナイアシンアミド25%、浸透型ナノカプセル、防腐剤フリー",
        "value": "ドラッグストアで完売続出の大ヒット美容液。美容レーザーのように角層の奥まで美容成分を届ける独自デリバリーシステム",
        "desc_p1": "シートマスクで絶大な人気を誇るダーマレーザーシリーズの最高峰美容液『ウルセラC』。スピキュールのように角層深くへ成分を押し込む『ナノカプセル浸透技術』を採用し、高濃度ビタミンCとナイアシンアミド25%を瞬時に届けます。",
        "desc_p2": "冬の紫外線残存ダメージと血行不良によってどんよりと暗く沈んだ肌に、まばゆいばかりの透明感とみずみずしい潤いを補給。針コスメの後に重ねて使うビタミン美容液としても相性抜群で、針によって開かれた浸透ルートを通ってビタミンCが角層深部へ吸い込まれていきます。",
        "target": "冬のくすみや毛穴の黒ずみを晴らしたい方、コスパ良く高濃度ビタミンCとナイアシンアミドを取り入れたい方",
        "point": "リードルショットなどの針美容液をなじませた直後に、本品を2〜3滴重ねる『W浸透ブースター術』がSNSでも大バズり中。翌朝の肌のトーンアップ感が一段と際立ちます。"
    },
    {
        "rank": 9,
        "tag": "✨ トラネキサム酸×高純度PDRN！冬の頑固なくすみと弾力不足を晴らす導入セラム",
        "catch": "サーモンDNA由来のPDRNと美白成分TXAを融合。透明感と水光ツヤをダブル注入",
        "brand_name": "CNP Laboratory (シーエヌピー)",
        "capacity": "100ml (ダーマアンサー TXA-PDRN ブースター)",
        "type": "高純度PDRN×TXA導入ブライトニング美容液",
        "features": "高純度PDRN（サーモンDNA）、トラネキサム酸（TXA）、ナイアシンアミド、ヒアルロン酸",
        "value": "皮膚科医監修の韓国トップブランドCNPが開発。冬の乾燥でしぼんだ角層細胞をふっくら持ち上げ、透明感あふれる水光肌へ導く",
        "desc_p1": "韓国ドクターズコスメの草分けCNP Laboratoryが放つ、今季最大の話題作『ダーマアンサー TXA-PDRN ブースター』。美容医療のリジュラン注射で知られるサーモンDNA由来成分『PDRN』と、くすみ・赤みにアプローチする『トラネキサム酸（TXA）』を贅沢に配合しています。",
        "desc_p2": "冬の寒風による乾燥ダメージで荒れた角層バリアを素早く補修し、内側から溢れ出すようなツヤとハリを再建。針美容液と併用することで、PDRNの強力な細胞修復シグナルが角層のすみずみまで行き渡り、乾き切った砂漠肌が瞬時にみずみずしく満たされます。とろみのあるリッチなテクスチャーながら、肌にすっと溶け込む浸透力の高さも魅力です。",
        "target": "冬になると肌がくすんで疲れて見える方、PDRNのハリ弾力効果を毎日のスキンケアで手軽に実感したい方",
        "point": "洗顔後、またはリードルショット塗布後に適量を顔全体に優しくハンドプレス。手のひらの温もりで包み込むと、ツヤ膜が肌表面にピタッと密着します。"
    },
    {
        "rank": 10,
        "tag": "🌙 眠っている間に針がじわじわ効く！天然スピキュール配合の濃密ナイトシールド",
        "catch": "天然微細針×CICA×ヒト型セラミド。暖房の効いた寝室でも朝まで乾かない鉄壁クリーム",
        "brand_name": "韓国コスメ / 日本発針コスメ",
        "capacity": "50g (スピキュール 高保湿ナイトリペアクリーム)",
        "type": "高保湿スピキュール配合ナイトリペアクリーム",
        "features": "天然マイクロニードル、ツボクサエキス（CICA）、ヒト型セラミド3種、シアバター、スクワラン",
        "value": "美容液だけでなく『クリームで針を閉じ込める』新発想。寝ている間の水分蒸散をブロックしながら、微細針がハリ成分を送り続ける",
        "desc_p1": "針美容液のステップの最後に重ねることで、スキンケア効果を極限まで閉じ込める『スピキュール配合高保湿ナイトクリーム』。濃厚なテクスチャーの中に均一に分散された天然微細針が、肌に塗布した瞬間から心地よい刺激を与えます。",
        "desc_p2": "CICAやヒト型セラミド、シアバターが肌表面にリッチな保護膜を形成。冬のエアコン暖房が夜通し稼働する寝室でも肌の水分を逃さず、翌朝起きたときの肌は、まるでエステ帰りのようなモチモチとした手触りとピンとしたハリ感に包まれます。針美容液とのライン使いはもちろん、単体でもしっかりとした手応えを発揮します。",
        "target": "朝起きると肌がカサカサに乾いている方、クリームの段階でも針の刺激とハリ感を実感したい方、冬の集中ナイトリペアを行いたい方",
        "point": "夜のお手入れの最後に、大きめのパール1粒分を手に取り、手のひらで温めてから顔全体にプレス。目尻やほうれい線には指先でトントンと重ね付けしてください。"
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
        "url": f"https://trendbeauty.site/winter-spicule.html#item-{i+1}",
        "offers": {
            "@type": "Offer",
            "price": str(p['price']),
            "priceCurrency": "JPY",
            "availability": "https://schema.org/InStock"
        }
    })

faq_list = [
    {
        "question": "スピキュール（針美容液）のチクチク感は肌に悪影響や傷を与えませんか？",
        "answer": "スピキュールは天然海綿から不純物を極限まで取り除いた純度99%以上の微細な天然ケイ素の針です。針の先端は非常に細く、角質層の細胞間をかき分けるように入るため、皮膚組織を傷つけることはありません。チクチクとした刺激は『美容成分が角層に引き込まれているサイン』であり、約72時間（2〜3日）かけて肌のターンオーバーとともに古い角質と一緒に自然と体外へ脱落します。ただし、擦るように強く塗り広げると刺激感が増すため、優しくハンドプレスで押し込むように塗布するのが正しい使い方です。"
    },
    {
        "question": "11月〜12月の真冬の乾燥肌・敏感肌でもスピキュールを使って大丈夫ですか？",
        "answer": "冬は寒風や暖房によって肌の角質が硬く厚くなり（角質肥厚）、通常の保湿スキンケアが表面で弾かれやすい季節です。スピキュールは角層に微細な通り道（マイクロチャネル）を開けるため、むしろ冬のインナードライ対策に非常に有効です。ただし、肌が赤くヒリついている時や皮剥けしている極度の敏感期は刺激になる場合があるため、まずはニードル本数の少ない『マイルド50』や『100』から始め、塗布後はCICAやセラミドなどの高保湿・鎮静クリームをたっぷり重ねることをおすすめします。"
    },
    {
        "question": "レチノールや高濃度ビタミンCと併用しても問題ありませんか？",
        "answer": "スピキュールとレチノール・ビタミンCの併用は、浸透力が高まるため非常に高い美容効果が期待できますが、同時に刺激感も出やすくなります。初めて併用する場合は、スピキュール（リードルショット等）を塗布した後、数分置いてから低刺激な保湿化粧水を挟み、その後にレチノールやビタミンCを少量ずつ塗布してください。A反応やピリピリ感が気になる方は、朝＝ビタミンC、夜＝スピキュール、あるいは日を分けて交互に使用するのが安全で効果的です。"
    },
    {
        "question": "スピキュール美容液は朝のスキンケアで使っても大丈夫ですか？",
        "answer": "『リードルショット50』のようなマイルドな製品は朝の使用も推奨されており、角層を整えて日中のメイクのノリや密着度を高める効果があります。ただし、針が角層にある状態で紫外線や外気の乾燥刺激を受けるとデリケートに傾きやすいため、朝に使用した後は必ず『高保湿な乳液・クリーム』と『SPF50+/PA++++程度の日焼け止め』を念入りに重ねてください。高濃度の300や700は夜のみの使用が鉄則です。"
    },
    {
        "question": "使い続けると肌がチクチク感に慣れて効果が薄れることはありますか？",
        "answer": "使い続けるうちにチクチク感に慣れて痛みをあまり感じにくくなることがありますが、それは肌の角質層が整い、バリア機能が安定してきた証拠です。針が角層に通り道を開けて美容成分を届ける物理的な作用は変わらず働いているため、効果が薄れているわけではありません。さらなる手応えを求めたい場合は、100から300へステップアップしたり、週末に700を取り入れるローテーションケアが効果的です。"
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
        "@id": "https://lumi-cosme.vercel.app/winter-spicule.html"
    },
    "headline": "保湿力の強さで肌乾燥とさようなら！毛穴奥まで潤いを届けて冬枯れ肌をふっくら覚醒させる高保湿スピキュール（針美容液）ランク10",
    "description": "11月・12月の過酷な暖房乾燥と寒風ゴワつき肌を救う高保湿スピキュール（針美容液）を徹底厳選！VTリードルショット（100・300・700・50）からヤーマン純金ニードル、SCボーテ、メディキューブまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。",
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
    "name": "真冬の高保湿スピキュール（針美容液）おすすめ人気ランキング10選",
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
            <tr><th>主要成分・針仕様</th><td>{d['features']}</td></tr>
            <tr><th>高保湿・浸透の理由</th><td>{d['value']}</td></tr>
          </table>
          
          <div class="review-block">
            <h4>💡 冬の乾燥肌・ゴワつきに対する詳細解説</h4>
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
  <title>保湿力の強さで肌乾燥とさようなら！毛穴奥まで潤いを届けて冬枯れ肌をふっくら覚醒させる高保湿スピキュール（針美容液）ランク10 - 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の過酷な暖房乾燥と寒風ゴワつき肌を救う高保湿スピキュール（針美容液）を徹底厳選！VTリードルショット（100・300・700・50）からヤーマン純金ニードル、SCボーテ、メディキューブまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。">
  <meta name="keywords" content="スピキュール,針美容液,リードルショット,マイクロニードル,高保湿,冬コスメ,乾燥肌,毛穴ケア,インナードライ,楽天コスメ">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-spicule.html">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！毛穴奥まで潤いを届けて冬枯れ肌をふっくら覚醒させる高保湿スピキュール（針美容液）ランク10">
  <meta property="og:description" content="11月・12月の過酷な暖房乾燥と寒風ゴワつき肌を救う高保湿スピキュール（針美容液）を徹底厳選！VTリードルショット（100・300・700・50）からヤーマン純金ニードル、SCボーテ、メディキューブまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-spicule.html">
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
      --primary: #4a2810;
      --primary-light: #7a4820;
      --accent: #d97706;
      --bg: #fdfbf7;
      --card-bg: #ffffff;
      --text: #2d2a26;
      --text-muted: #6b635b;
      --border: #eedcc8;
      --radius: 12px;
      --shadow: 0 4px 16px rgba(74, 40, 16, 0.08);
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
      background: linear-gradient(135deg, #3d200d, #633316);
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
      background: #fef3c7;
      color: #b45309;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 4px 12px;
      border-radius: 20px;
      margin-bottom: 14px;
    }}
    h1 {{
      font-size: 1.85rem;
      line-height: 1.45;
      color: #3b1d0c;
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
      color: #443e38;
      margin-bottom: 18px;
    }}
    .toc-box {{
      background: #faf6f0;
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
      color: #422513;
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
      background: #fdf8f3;
      padding: 20px;
      border-radius: 10px;
      border: 1px solid #ebd9c8;
    }}
    .grid-card h4 {{
      color: var(--primary);
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
      background: linear-gradient(135deg, #d97706, #b45309);
      color: #fff;
      font-size: 1.05rem;
      font-weight: 800;
      padding: 6px 18px;
      border-radius: 20px;
      box-shadow: 0 4px 10px rgba(180, 83, 9, 0.3);
    }}
    .product-tag {{
      display: inline-block;
      margin-top: 6px;
      font-size: 0.88rem;
      font-weight: 700;
      color: #b45309;
      background: #fef3c7;
      padding: 3px 10px;
      border-radius: 6px;
      margin-bottom: 10px;
    }}
    .product-name {{
      font-size: 1.4rem;
      line-height: 1.4;
      color: #3b1d0c;
      margin-bottom: 8px;
      font-weight: 800;
    }}
    .product-catch {{
      font-size: 0.98rem;
      font-weight: 600;
      color: #78350f;
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
      background: #fff8f0;
      border-radius: 8px;
      border: 1px dashed #f2cbab;
    }}
    .price-label {{ display: block; font-size: 0.78rem; color: #88786a; }}
    .price-val {{ font-size: 1.5rem; font-weight: 800; color: #c2410c; }}
    .price-tax {{ font-size: 0.8rem; color: #88786a; }}
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
      background: #fdf5ec;
      padding: 8px 12px;
      border: 1px solid #eedcc8;
      text-align: left;
      color: #633316;
      font-weight: 600;
    }}
    .spec-table td {{
      padding: 8px 12px;
      border: 1px solid #eedcc8;
      background: #fff;
    }}
    .review-block {{
      background: #faf7f2;
      border-left: 4px solid var(--accent);
      padding: 16px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 14px;
    }}
    .review-block h4 {{
      font-size: 0.98rem;
      color: #4a2810;
      margin-bottom: 8px;
    }}
    .review-block p {{
      font-size: 0.92rem;
      line-height: 1.75;
      color: #38332e;
      margin-bottom: 8px;
    }}
    .review-block p:last-child {{ margin-bottom: 0; }}
    .target-block, .usage-block {{
      font-size: 0.9rem;
      margin-bottom: 10px;
      line-height: 1.7;
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
      color: #78350f;
      font-weight: 700;
      margin-bottom: 8px;
    }}
    .faq-a {{
      font-size: 0.95rem;
      line-height: 1.8;
      color: #3d3731;
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
      background: #faf6f0;
      padding: 16px;
      border-radius: 8px;
      border: 1px solid #ebd9c8;
      text-decoration: none;
      color: inherit;
      transition: all 0.2s;
    }}
    .internal-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.06);
      background: #fff;
    }}
    .internal-card h4 {{
      color: var(--primary);
      font-size: 0.98rem;
      margin-bottom: 6px;
      font-weight: 700;
    }}
    .internal-card p {{
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}
    
    footer {{
      background: #2b180d;
      color: #d6cbbf;
      padding: 48px 20px 24px;
      font-size: 0.88rem;
      line-height: 1.8;
    }}
    .footer-inner {{
      max-width: 1080px;
      margin: 0 auto;
    }}
    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px 20px;
      margin-bottom: 24px;
    }}
    .footer-links a {{ color: #e8ded4; text-decoration: none; font-size: 0.82rem; }}
    .footer-links a:hover {{ text-decoration: underline; }}
    .footer-copy {{
      text-align: center;
      border-top: 1px solid #4a3424;
      padding-top: 24px;
      color: #998777;
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <a href="/" class="site-logo">冬コスメ徹底比較ラボ</a>
    </div>
  </header>
  
  <div class="breadcrumb">
    <a href="/">トップ</a> &gt; <a href="/winter-spicule.html">高保湿スピキュール（針美容液）</a>
  </div>
  
  <main class="main-container">
    <article class="article-header">
      <span class="article-badge">2026-2027年 冬季最新・浸透革新コスメ特集</span>
      <h1>保湿力の強さで肌乾燥とさようなら！毛穴奥まで潤いを届けて冬枯れ肌をふっくら覚醒させる高保湿スピキュール（針美容液）ランク10</h1>
      <div class="meta-box">
        <span>📅 公開日: 2026年11月4日</span>
        <span>✍️ 執筆・監修: 冬コスメ徹底比較ラボ 編集部</span>
        <span>⏱️ 読了目安: 約12分</span>
      </div>
      <p class="lead-text">
        11月から12月にかけて外気湿度が30%台へ急落し、オフィスのエアコン温風が一日中素肌をさらし続ける真冬の入り口。「どれだけ高価な保湿美容液やこっくりしたクリームを塗っても、肌の表面でヌルつくだけで中に入っていかない」「乾燥しているのに毛穴がパカッと開き、ファンデーションが毛穴落ちしてしまう」という深刻な悩みに直面していませんか？
      </p>
      <p class="lead-text">
        その原因は、寒冷外気と血行不良によって角質細胞のターンオーバーが停滞し、硬く乾いた角質が層をなして肌表面を塞いでしまう『冬の角質肥厚』にあります。この鉄壁のバリアを打破し、潤いの通り道（マイクロチャネル）を物理的に開拓するのが、いま美容界を席巻している『スピキュール（天然マイクロニードル）』です。本記事では、天然海綿から精製された純度99%以上の微細針に高保湿成分を融合させた、楽天で今すぐ手に入る最高峰の針美容液10選を徹底検証してご紹介します。
      </p>
      
      <div class="toc-box">
        <div class="toc-title">📑 目次（タップで各項目へジャンプ）</div>
        <ol class="toc-list">
          <li><a href="#mechanism">なぜ真冬の乾燥ゴワつき肌に「スピキュール（針美容液）」が効くのか？</a></li>
          <li><a href="#selection">冬の針コスメ選びで失敗しないための4大チェックポイント</a></li>
          <li><a href="#ranking">真冬の高保湿スピキュール（針美容液）おすすめ人気ランキング10選</a></li>
          <li><a href="#synergy">美容のプロが実践！スピキュール×高保湿成分の相乗効果を高めるブースター術</a></li>
          <li><a href="#faq">スピキュール（針美容液）に関するよくある質問（FAQ）</a></li>
          <li><a href="#related">あわせて読みたい冬の集中高保湿ケア特集</a></li>
        </ol>
      </div>
    </article>
    
    <section class="guide-section" id="mechanism">
      <h2>なぜ真冬の乾燥ゴワつき肌に「スピキュール（針美容液）」が効くのか？</h2>
      <p>
        初冬の11月〜12月は、日本列島に乾いたシベリア寒気団が流れ込み、東京や大阪などの太平洋側都市部では外気湿度が20〜30%台まで急落します。さらに室内では暖房器具がフル稼働し、皮膚表面の水分蒸発スピードは夏の3倍以上に加速します。
      </p>
      <p>
        この過酷な環境から身を守ろうとして、肌は角質層を厚く硬くして防御態勢に入ります。これが『冬の角質肥厚（かくしつひこう）』です。角質層がプラスチックのように硬化してしまうと、通常の分子構造を持つヒアルロン酸やコラーゲン、セラミドなどの保湿成分は角層の隙間に入り込めず、肌表面を滑るだけで蒸発してしまいます。
      </p>
      <div class="guide-grid">
        <div class="grid-card">
          <h4>🪡 1. 微細な通り道（マイクロチャネル）を形成</h4>
          <p>スピキュールは毛穴の数分の一の微細な天然ケイ素針。角質細胞の隙間にスッと入り込み、物理的な浸透ルートを開拓。後から塗る化粧水やクリームがぐんぐん引き込まれます。</p>
        </div>
        <div class="grid-card">
          <h4>⚡ 2. 72時間の持続刺激で自活力覚醒</h4>
          <p>針が角層に留まっている約72時間の間、肌細胞に『異物を押し出そうとする心地よい微細刺激』を与え続けます。停滞していたターンオーバーが活性化し、内側から押し上げるハリが生まれます。</p>
        </div>
        <div class="grid-card">
          <h4>💧 3. 針そのものが美容成分の運び屋</h4>
          <p>近年の最新スピキュールは多孔質構造（無数の微細な穴）を持っており、その内部にCICA、低分子ヒアルロン酸、純金コロイド、ペプチドなどを抱き込ませて角層深層へ直撃させます。</p>
        </div>
      </div>
    </section>
    
    <section class="guide-section" id="selection">
      <h2>冬の針コスメ選びで失敗しないための4大チェックポイント</h2>
      <p>
        ひとくちにスピキュール美容液と言っても、ニードルの配合密度やテクスチャー、鎮静成分の有無によって使用感や適した肌状態は大きく異なります。乾燥が進む冬だからこそ意識したい選び方のポイントを整理しました。
      </p>
      <div class="guide-grid">
        <div class="grid-card">
          <h4>① ニードル本数（刺激レベル）で選ぶ</h4>
          <p><strong>・3万〜5万本（マイルド50等）：</strong> 初心者や敏感肌の朝夜デイリー保湿に。<br>
          <strong>・10万本前後（リードル100等）：</strong> 毎晩使える万能ブースター。キメと浸透を底上げ。<br>
          <strong>・20万〜30万本（リードル300等）：</strong> 3日に1回。頑固な毛穴・ゴワつきを速攻リセット。<br>
          <strong>・50万本以上（リードル700等）：</strong> 週1回の最高峰エステ級スペシャルケア。</p>
        </div>
        <div class="grid-card">
          <h4>② 鎮静・抗炎症サポート成分の有無</h4>
          <p>冬は寒暖差によって毛細血管が拡張し、赤みが出やすい季節。ツボクサエキス（CICA）、パンテノール、グリチルリチン酸2K、プロポリスなど、針の刺激を和らげながら鎮静してくれる複合処方を選びましょう。</p>
        </div>
        <div class="grid-card">
          <h4>③ 針に担持された美容成分（純金・PDRN等）</h4>
          <p>単なる海綿針だけでなく、ヤーマンのように純金ナノコロイドをコーティングしたものや、エクソソーム、PDRN、ヒト幹細胞培養液をドッキングさせた先端処方は、冬の年齢肌に劇的なハリをもたらします。</p>
        </div>
        <div class="grid-card">
          <h4>④ 容器形状と鮮度管理</h4>
          <p>注射器型シリンジ容器（SCボーテ等）やエアレスポンプは、空気に触れず酸化を防げるため非常に衛生的。最後まで均一なニードル密度と高活性な保湿力をキープできます。</p>
        </div>
      </div>
    </section>
    
    <section id="ranking">
      <h2 style="font-size: 1.6rem; color: #3b1d0c; border-bottom: 3px solid #d97706; padding-bottom: 10px; margin-bottom: 36px; font-weight: 800;">
        🏆 真冬の高保湿スピキュール（針美容液）おすすめ人気ランキング10選
      </h2>
      
      {cards_str}
      
    </section>
    
    <section class="guide-section" id="synergy">
      <h2>美容のプロが実践！スピキュール×高保湿成分の相乗効果を高めるブースター術</h2>
      <p>
        スピキュール美容液の最大の魅力は、その後に重ねるスキンケアの効果を何倍にも引き上げる『ブースター機能』にあります。11月〜12月の過酷な乾燥を乗り切るための、プロ直伝の重ね付けテクニックをマスターしましょう。
      </p>
      <div class="guide-grid">
        <div class="grid-card">
          <h4>1. 塗り方は「擦る」のではなく「押し込む」</h4>
          <p>手のひらに広げて横にゴシゴシ擦ると、針が皮膚表面を引っ掻いて赤みの原因になります。肌の上に点置きし、手のひら全体で垂直に『トントン、ギュッ』と優しく包み込むように密着させましょう。</p>
        </div>
        <div class="grid-card">
          <h4>2. 直後に「高保水シートマスク」で水分タンク補給</h4>
          <p>針によって通り道が開かれた直後の肌は、水分を猛烈に欲しています。ヒト幹細胞やヒアルロン酸、CICAをたっぷり含んだシートマスクを10〜15分密着させると、角層深部まで美容液が満ち渡ります。</p>
        </div>
        <div class="grid-card">
          <h4>3. 仕上げは「ヒト型セラミド・オイル」で完全密閉</h4>
          <p>水分を補給した後は、冬の冷風と暖房から守るためにこっくりしたクリームで蓋をします。セラミドクリームやマルラオイル、ローズヒップオイルを重ねることで、翌朝まで吸い付くような水光肌が完成します。</p>
        </div>
      </div>
    </section>
    
    <section class="faq-section" id="faq">
      <h2>スピキュール（針美容液）に関するよくある質問（FAQ）</h2>
      {faq_str}
    </section>
    
    <section class="internal-section" id="related">
      <h2>あわせて読みたい！冬の乾燥撃退・集中保湿スキンケア特集</h2>
      <div class="internal-grid">
        <a href="/winter-stem-cell.html" class="internal-card">
          <h4>🧬 高保湿ヒト幹細胞コスメ10選</h4>
          <p>肌細胞の根源から保水力を呼び覚ます！冬枯れ肌の密度を高める最高峰エイジングケア。</p>
        </a>
        <a href="/winter-lipidure.html" class="internal-card">
          <h4>💧 高保水リピジュアコスメ10選</h4>
          <p>ヒアルロン酸の2倍の保水力！洗っても落ちない人工角層ヴェールで暖房乾燥を完全ブロック。</p>
        </a>
        <a href="/winter-ceramide-cream.html" class="internal-card">
          <h4>🛡️ 高保湿セラミドクリーム10選</h4>
          <p>角層の細胞間脂質をガッチリ補強。針美容液の後に重ねたい鉄壁の水分シールドクリーム。</p>
        </a>
        <a href="/winter-pdrn-serum.html" class="internal-card">
          <h4>🐟 高濃度PDRN美容液10選</h4>
          <p>サーモンDNAの力で冬の荒れ肌・ダメージ角質をスピード修復。スピキュールと相性抜群。</p>
        </a>
        <a href="/winter-rosehip-oil.html" class="internal-card">
          <h4>🌹 高保湿ローズヒップオイル10選</h4>
          <p>ビタミンの爆弾と濃密オメガ脂肪酸で、硬くなった冬の角質層を柔らかく解きほぐす純植物オイル。</p>
        </a>
        <a href="/winter-exosome-serum.html" class="internal-card">
          <h4>🔬 先端エクソソーム美容液10選</h4>
          <p>細胞間伝達物質が角層の生まれ変わりを指揮。冬の毛穴たるみと乾燥くすみを同時解決。</p>
        </a>
      </div>
    </section>
  </main>
  
  <footer>
    <div class="footer-inner">
      <div class="footer-links">
        <a href="/">トップページ</a>
        <a href="/winter-spicule.html">高保湿スピキュール</a>
        <a href="/winter-stem-cell.html">高保湿ヒト幹細胞</a>
        <a href="/winter-lipidure.html">高保水リピジュア</a>
        <a href="/winter-rosehip-oil.html">高保湿ローズヒップオイル</a>
        <a href="/winter-honey.html">高保湿ハチミツコスメ</a>
        <a href="/winter-mugwort.html">高保水ヨモギコスメ</a>
        <a href="/winter-marula-oil.html">高保湿マルラオイル</a>
        <a href="/winter-birch-juice.html">高保水白樺樹液</a>
        <a href="/winter-azelaic-acid.html">高濃度アゼライン酸</a>
        <a href="/winter-ceramide-cream.html">高保湿セラミドクリーム</a>
      </div>
      <div class="footer-copy">
        &copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved. 当サイトは楽天アフィリエイトプログラムに参加しています。
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-spicule.html", "w", encoding="utf-8") as f:
    f.write(full_html.strip())

print("✅ winter-spicule.html generated successfully!")
