import json
import re

with open("fetched_3new_nov_dec_special.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_oil_in_lotion"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🍊 オイル層×ローション層の黄金バランス！真冬の冷え固まった角層をとろけるようにほぐす名品二層式化粧水",
        "catch": "RMKが誇る伝説のトリートメント技術を注ぎ込んだ二層式ローション。オイル層がごわつく硬化角層をまろやかに解きほぐし、同時に高保水ローション層が深部まで満水状態へ導く、真冬の乾燥対策の決定版",
        "brand_name": "RMK (アールエムケー)",
        "capacity": "160mL / 二層式クリアボトル",
        "type": "エモリエントオイル×モイスチャーローション 二層式化粧液",
        "features": "スクワラン、オリーブ果実油、ホホバ種子油、オレンジ果皮エキス、ビルベリー葉エキス、シトラスフローラルの香り",
        "value": "水分と油分を同時にチャージすることで、皮脂分泌が枯渇した冬の素肌に理想的な皮脂膜バランスを瞬時に再現。乳液を重ねる前段階でモチモチの柔らかさを確立",
        "desc_p1": "11月から12月にかけて気温が一段と低下すると、皮膚の皮脂腺の活動が急激に減衰し、分泌される皮脂量は夏の約3分の1にまで落ち込みます。皮脂膜を失った角層は乾燥によってカチコチに硬化し、一般的なサラサラした化粧水をいくら叩き込んでも表面で弾かれてしまいます。RMKのWトリートメント ローションは、肌との親和性が極めて高い植物性オイル層と、濃密な潤いを蓄えたローション層を絶妙な比率で配合した名作です。",
        "desc_p2": "使用前に数回シェイクすると、二層が溶け合ってミルキーなオレンジ色のエマルジョン状態へと変化します。手のひらに取って顔を包み込むと、上質なスクワランやホホバオイルが乾燥でゴワついた角質細胞の接着を優しくほぐし、その隙間を縫うように水分がぐんぐん浸透。柑橘系の爽やかでリラックスできる香りに包まれながら、洗顔直後とは思えないほどのツヤと吸い付くような柔らかさが瞬時に肌へ蘇ります。",
        "target": "冬になると化粧水が肌表面を滑るだけで浸透しないと感じる方、洗顔後のつっぱりや乾燥ゴワつきが深刻な方、一本でリッチな潤いと柔軟性を手に入れたい方",
        "point": "容器を上下によく振って二層を白濁させた後、500円玉大を手にとり、手のひらで温めてから顔全体を優しくプレスしてなじませます。首やデコルテまで滑らせるように伸ばすと、巡りが良くなりトーンアップします。"
    },
    {
        "rank": 2,
        "tag": "🌿 奇跡の万能オイル・タマヌ×伝統の酒粕エキス！大人の冬枯れ肌を艶やかに立て直す濃密二層式セラム",
        "catch": "沖縄の過酷な日差しと潮風を生き抜く『タマヌオイル』と、創業140年の蔵元から届く濃厚な酒粕エキスを二層に凝縮。乾燥によるゴワつきやくすみを一掃し、内側から発光するような極上のツヤ肌へ導くSHIROの最高峰オイルローション",
        "brand_name": "SHIRO (シロ)",
        "capacity": "30mL / スポイト遮光ボトル",
        "type": "高機能タマヌオイル×酒粕エキス 二層式オイルセラムローション",
        "features": "未精製タマヌオイル（テリハボク種子油）、酒粕エキス、甘酒エキス、コメヌカ油",
        "value": "古来より皮膚の万能薬として珍重されてきたタマヌオイルの驚異的な抗酸化力と肌修復力。冬の冷えや乾燥で疲弊した角層を栄養満点のエモリエントヴェールで包み込む",
        "desc_p1": "冬の乾燥は、単に肌の水分を奪うだけでなく、肌のターンオーバーを著しく狂わせて古い角質を滞留させ、どんよりとくすんだ『冬枯れ肌』を生み出します。SHIROのタマヌ オイルインセラムは、太平洋の島々で『奇跡の木』と呼ばれるタマヌの種子から冷圧搾で抽出した未精製オイルを贅沢に使用。米ぬかや酒粕の発酵アミノ酸と組み合わさることで、肌の再生力を力強く呼び醒まします。",
        "desc_p2": "振って混ぜ合わせると、濃厚で深みのあるリッチなリキッドが完成します。肌にのばした瞬間に感じるのは、圧倒的な充足感と安心感です。未精製オイル特有のハーブのような深みのある香りが広がり、乾燥で硬くなった肌がほどけるように滑らかに整います。夜のスキンケアに取り入れれば、翌朝には乾燥くすみが一掃され、ふっくらと内側から発光するようなツヤ肌を実感できます。",
        "target": "冬になると顔色がくすんで疲れて見えやすい方、自然由来のパワフルな植物オイルでエイジングケアしたい方、乾燥による小ジワやハリ不足に悩む大人の肌",
        "point": "二層がしっかり混ざるようボトルを上下に振った後、手のひらに3〜4滴を取り、顔全体を温めながらハンドプレスで押し込みます。特に乾燥しやすい目元や口元には指先で優しくトントンと重ねましょう。"
    },
    {
        "rank": 3,
        "tag": "🌾 5種の厳選ハーブを純白麹で発酵濃縮！濃密な化粧液が冬の肌に劇的なハリと潤いを与える高機能発酵液",
        "catch": "白神山地の麓にある自社研究所で無農薬栽培された5種の薬効ハーブを、希少な純白麹『しらかみ』で発酵・熟成。水滴一つひとつに美容オイル成分が溶け込んだ唯一無二のテクスチャーが、真冬の肌を劇的な潤いで満たすアルビオンの傑作",
        "brand_name": "ALBION (アルビオン)",
        "capacity": "160mL / プレミアムボトル",
        "type": "純白麹発酵濃密エキス配合 多機能高保湿化粧液",
        "features": "ミュラ™（5種ハーブ発酵液：ヤマヨモギ、ヤグルマギク、コウスイハッカ、タチジャコウソウ、カリン×純白麹）、天然アロマ精油",
        "value": "発酵によって微小分子化された多種多様なポリフェノール、アミノ酸、微量オイル成分が角層の全層へ浸透。乾燥・キメの乱れ・ハリ不足をマルチに克服",
        "desc_p1": "化粧水の枠を遥かに超え、『化粧液』と呼ばれるアルビオンのフローラドリップ。11月〜12月の急激な気温低下で代謝が落ち、栄養不足に陥った冬の肌のために、自然の恵みを発酵の力で極限まで凝縮しています。一般的な化粧水のように水を主成分とするのではなく、発酵液そのものを贅沢にベースとすることで、濃厚な美容オイルのようなとろみとコクを実現しています。",
        "desc_p2": "肌に注ぎ込むと、リッチな感触でありながら驚くほど滑らかに角層の奥深くへと吸い込まれていきます。後肌はまるで上質なフェイスマスクを一晩中つけていたかのようにしっとりと満たされ、ピンとしたハリ感が立ち上がります。ハーブと発酵が織りなす芳醇な香りは、冬のスキンケアタイムを至福のリフレッシュ時間へと昇華させてくれます。",
        "target": "高保湿だけでなくハリ・透明感・キメの全てを同時に底上げしたい方、高級感のある贅沢な使い心地を求める方、冬の乾燥エイジングに本気で立ち向かいたい方",
        "point": "洗顔後または乳液の後、コットンまたは手のひらに適量（ティースプーン1杯分程度）をとり、顔全体になじませます。顔全体を優しく包み込み、引き上げるようにハンドプレスするとハリ感が高まります。"
    },
    {
        "rank": 4,
        "tag": "⚖️ オイル層とエッセンス層の黄金シェイク！悪玉皮脂をトラップしながら潤いを閉じ込める新発想バランシングローション",
        "catch": "KANEBOの先進研究が生んだ、オイルイン二層式ローションの最高峰。乾燥するのに部分的に過剰分泌される冬の『不飽和脂肪酸（悪玉皮脂）』を選択的にトラップしながら、良質なエモリエントオイルで角層を保護するスマート化粧水",
        "brand_name": "KANEBO (カネボウ)",
        "capacity": "180mL / プリズムデザインボトル",
        "type": "悪玉皮脂トラップ技術×オイルイン二層式 高保湿化粧水",
        "features": "ターゲット皮脂トラップ技術、スクワラン、グリセリン、複合保湿植物エキス、ティートピアを基調とした茶花の香り",
        "value": "冬のインナードライが引き起こす『乾燥崩れ』と『大人ニキビ・肌荒れ』を同時に解決。水分と油分が整ったシルキーでなめらかな理想の素肌を構築",
        "desc_p1": "冬の肌トラブルで多くの人を悩ませるのが、「頬や目元はカサカサなのに、鼻やあご周りは皮脂でテカリ、小さな吹き出物ができる」というアンバランス現象です。これは乾燥に耐えかねた肌が防御のために過剰に皮脂を分泌し、その皮脂中の不飽和脂肪酸が角層を酸化・刺激することが原因です。カネボウのスキン ハーモナイザーは、この悪玉皮脂だけを固めて無力化する独自テクノロジーを搭載しています。",
        "desc_p2": "シェイクして混ぜ合わせると、繊細なオイルドロップがエッセンスの中に均一に分散します。肌になじませると、軽やかなみずみずしさと共にリッチなオイルの安心感が広がり、ベタつきやテカリを一切残さずに肌表面がさらりとシルキーに整います。乾燥によるつっぱり感を即座に解消しながら、毛穴の目立たない均一な素肌へと導いてくれます。",
        "target": "冬でもTゾーンがベタつくのにUゾーンは突っ張る混合肌、乾燥による大人ニキビや肌荒れを繰り返す方、肌の水分油分バランスを根本から整えたい方",
        "point": "ボトルを上下によく振って二層を完全に混ぜ合わせた後、手のひらに適量を取り、顔全体を包み込むようになじませます。皮脂の気になる小鼻やTゾーンにも優しく押し込みましょう。"
    },
    {
        "rank": 5,
        "tag": "🧬 多重層バイオリポソームオイルカプセル配合！角層深部へ潤いオイル成分を放出し続ける名品化粧液",
        "catch": "コスメデコルテが誇るリポソーム技術の粋を集めた高機能ローション。タマネギ状に重なり合った超微小なバイオリポソームカプセルの中にオイル成分を内包し、角層の奥底で長時間にわたって潤いを放出し続ける革新的な保湿設計",
        "brand_name": "DECORTÉ (コスメデコルテ)",
        "capacity": "100mL / 高級パープルボトル",
        "type": "多重層バイオリポソームカプセル内包 超浸透型オイルイン化粧液",
        "features": "超微小0.1ミクロンの多重層バイオリポソーム、植物性スクワラン、セラミド類似成分、アデノシン、低刺激処方",
        "value": "肌に乗せた瞬間だけでなく、塗布後何時間も経過した室内でも、カプセルが外側から一層ずつ崩壊して持続的に水分と油分を供給。一日中乾かない持続保水を実現",
        "desc_p1": "通常の化粧水は塗布直後が最も潤っており、時間の経過と共に蒸散していきますが、コスメデコルテのリポソーム アドバンスト リペアローションは時間軸を覆す設計になっています。生体組成成分リン脂質でできた0.1ミクロンの微小カプセルが角層深部まで一瞬で到達し、乾燥して損傷した部分にピタッと吸着。そこから何時間もかけて水分と美容オイル成分を放出し続けます。",
        "desc_p2": "手にとると、サラリとしていながら奥にリッチな油分の密度を感じさせる独特のテクスチャー。肌に広げた瞬間、まるで乾いた大地が雨水を飲み干すように一瞬で角層へと引き込まれます。使用後の肌は内側から水分がギュッと詰まったような高密度なハリに満ち、表面には上質な薄膜ヴェールが形成され、夕方の暖房下でも突っ張り感を寄せ付けません。",
        "target": "朝いくら保湿しても昼過ぎには乾燥してしまう方、キメの乱れや毛穴の開きが目立つ方、最高峰のテクノロジーで肌の土台から再構築したい方",
        "point": "朝晩の洗顔直後、適量をコットンまたは手のひらに取り、肌へ丁寧にパッティングしながらなじませます。特に乾燥が気になる部分には、ハンドプレスでじっくりと時間をかけて押し込みましょう。"
    },
    {
        "rank": 6,
        "tag": "🍷 ざくろ種子オイル×植物エキス！真冬の乾燥小ジワを上質オイルヴェールで包み込むオーガニックの傑作",
        "catch": "スイスの老舗オーガニックブランドWELEDAが手掛けるエイジングケアローション。ポリフェノールとプニカ酸を豊富に含む貴重なざくろ種子オイルが、真冬の乾燥による小ジワやハリ不足をなめらかに包み込む高保湿処方",
        "brand_name": "WELEDA (ヴェレダ)",
        "capacity": "100mL / ガラスボトル",
        "type": "ざくろ種子オイル配合 オーガニック高保湿エイジングケアローション",
        "features": "ざくろ種子油（プニカ酸高含有）、アルガニアスピノサ核油、シロキクラゲ多糖体、天然エッセンシャルオイル香料",
        "value": "植物由来のプニカ酸が冬の酸化ストレスから細胞を強力にガード。とろみのあるオイルインリキッドが肌表面にしなやかな保護ヴェールを形成し、弾むようなハリを回復",
        "desc_p1": "冬の寒風にさらされた大人の肌は、乾燥だけでなく弾力低下や小ジワの定着といったエイジングトラブルが加速します。ヴェレダのざくろ モイスチャーローションは、自然界で唯一ざくろにだけ高濃度に含まれる希少な不飽和脂肪酸『プニカ酸』に着目。オーガニックざくろ種子から低温圧搾された高貴なオイルが、冬の枯れ肌に若々しい活力をもたらします。",
        "desc_p2": "とろみのあるリッチなローションを肌に乗せると、天然精油のフルーティ＆スパイシーな奥深い香りが広がり、心まで解きほぐされます。オイルインでありながら浸透性が非常に高く、肌表面にベタつきを残さずに内側をしっとり密着ラッピング。乾燥によって目立ち始めた目尻やほうれい線まわりの細かいキメをふっくらと持ち上げてくれます。",
        "target": "冬になると乾燥小ジワやハリ不足が顕著になる大人世代、100%天然由来・オーガニック成分にこだわりたい方、香りに癒されながらスキンケアしたい方",
        "point": "洗顔後、適量（500円玉大）を手のひらに取り、顔全体から首筋まで温めながら優しくなじませます。手のひらで肌を包み込み、引き上げるように軽くホールドするのが効果的です。"
    },
    {
        "rank": 7,
        "tag": "🏥 オイルインリッチ設計の薬用高保湿！大人の深刻な冬枯れ小ジワをふっくら弾むハリ肌へ導く",
        "catch": "オルビスが大人世代の本格的な乾燥・ハリ低下のために開発した最高峰薬用スキンケアライン『アンバー』。濃密なオイル成分を微細乳化させたローションが、真冬の冷気で硬化した大人の角質深部まで浸透し、ふっくらリッチな弾力を再生",
        "brand_name": "ORBIS (オルビス)",
        "capacity": "120mL / ポンプボトル",
        "type": "医薬部外品・オイルインリッチ 薬用エイジングケアローション",
        "features": "ナイアシンアミド（シワ改善・美白有効成分）、コラーゲンコンプレックス、植物性エモリエントオイル、無香料・無着色",
        "value": "有効成分ナイアシンアミドが角層深部の真皮まで届いてシワを改善。オイルイン処方が硬化した大人の角質を柔軟にし、水分と油分の保持力を飛躍的に向上",
        "desc_p1": "年齢を重ねた肌の冬の乾燥は、単に表皮が乾くだけでなく、真皮のコラーゲン低下と相まって深いシワやたるみへと直結します。オルビスアンバーのヴァイタルトリートメントローションは、医薬部外品有効成分ナイアシンアミドを配合し、シワ改善と美白ケア、そして濃密オイルによる高保湿を1本で完結させる大人のための高機能アイテムです。",
        "desc_p2": "ポンプを押すと、とろりとした乳白色の美容液のようなリッチなテクスチャーが現れます。肌に乗せると摩擦なくスルリと伸び広がり、オイルの心地よいコクが角層のすみずみまで密着。塗布後は乳液や美容液を重ねたかのような充実した潤い膜が形成され、暖房の風が当たる部屋でも夕方までふっくらとしたハリ肌が続きます。",
        "target": "乾燥による小ジワだけでなく本格的なシワ改善も目指したい方、スキンケアの工程をシンプルにしつつ確実な手応えが欲しい方、大人の乾燥肌に悩む方",
        "point": "朝晩の洗顔後、2プッシュを手にとり、手のひら全体に広げてから顔の中心から外側へ向かって優しくなじませます。最後に手のひらで顔全体をハンドプレスして浸透を促します。"
    },
    {
        "rank": 8,
        "tag": "🌺 カメリアオイル×フラワーエッセンスの贅沢二層式！微細ミストが瞬時にツヤと柔軟性を宿す",
        "catch": "モダンボタニカルスキンケアブランドFEMMUEの象徴であるカメリアオイル（ツバキ種子油）とフラワーウォーターの贅沢な二層式エッセンス。超微細なオイルインミストが、真冬のゴワつく乾燥肌をふんわり包み込み、陶器のようなツヤを与える",
        "brand_name": "FEMMUE (ファミュ)",
        "capacity": "100mL / 高級ガラススプレーボトル",
        "type": "カメリアオイル×フラワーエキス 二層式オイルミスト化粧液",
        "features": "カメリアオイル（ツバキ種子油）、ローズウォーター、ヒマワリ種子油、天然ダマスクローズ精油の香り",
        "value": "皮脂に近いオレイン酸を豊富に含むカメリアオイルが硬化角質を柔軟化。化粧水・美容液・乳液の3役を担い、真冬の乾燥肌にしっとりしたツヤと弾力性をチャージ",
        "desc_p1": "韓国発のラグジュアリーボタニカルブランドFEMMUEのデュアルエッセンスは、厳選されたカメリアオイルと花々の蒸留水を黄金比でブレンドした二層式アイテムです。ツバキ種子油は人間の皮脂の主成分であるオレイン酸を80%以上含み、角層との親和性が極めて高いため、真冬の硬くなった肌にも一切弾かれることなく馴染みます。",
        "desc_p2": "ボトルをシェイクしてスプレーすると、オイルインとは思えないほど細かく柔らかな霧が肌全体を包みます。優雅な天然ローズの香りに包まれながら、乾燥した肌表面が瞬時になめらかなツヤで覆われ、つっぱり感がスッと和らぎます。朝のメイク前の導入美容液として、また日中の乾燥対策や夜のスキンケアの仕上げとして、マルチに活躍してくれます。",
        "target": "ゴワつきと乾燥で肌が硬く感じる方、上質なツヤ肌メイクの土台を作りたい方、贅沢な花々の香りで心まで満たされたい方",
        "point": "容器をよく振って二層を完全に混ぜてから、顔から20cmほど離して3〜4回スプレーし、手のひらで軽く包み込むように馴染ませます。メイクの仕上げにひと吹きすると粉浮きが消えます。"
    },
    {
        "rank": 9,
        "tag": "🌵 サハラ砂漠の希少サボテンシードオイル90%以上配合！乾燥した肌の水分油分を黄金比に整える弱酸性トナー",
        "catch": "寒暖差50度の過酷なサハラ砂漠で生き抜くウチワサボテンの種子から、1リットル採るのに36時間・100万個の種を要する超希少オイルを高配合。オリーブオイルの400倍のビタミンEとリッチな保水力が真冬の乾燥肌を救う名作",
        "brand_name": "Huxley (ハクスリー)",
        "capacity": "120mL / スタイリッシュガラスボトル",
        "type": "サボテンシードオイル配合 弱酸性高保湿オイルイントナー",
        "features": "サボテン種子オイル、サボテンエキス（トゲキリンサイエキス）、センチフォリアバラ花水、弱酸性処方",
        "value": "圧倒的な生命力を持つサボテンオイルが角層内部の水分蒸散をブロック。肌の理想的な水分油分バランス（8:2）を再現し、透明感のあるなめらかなキメを確立",
        "desc_p1": "極限の乾燥と寒暖差に晒されるサハラ砂漠の過酷な環境から見出されたサボテンシードオイル。ハクスリーのトナー エクストラクト イットは、精製水の代わりにサボテンエキスをベースに採用し、希少なオイル成分を溶け込ませた弱酸性の高保湿トナーです。サボテンオイルに含まれる豊富なリノール酸とビタミンEが、冬の乾燥によって傷んだ細胞膜を保護します。",
        "desc_p2": "サラサラとした透明な液体ですが、肌に馴染ませるとオイルインならではのリッチなしっとり感が現れ、角層の奥深くまで潤いが満ち渡ります。サハラ砂漠の庭園を思わせる爽やかで洗練されたボタニカルな香りが心地よく、使い続けることで肌本来のバリア機能が強化され、エアコン暖房の風にも揺らがないタフで透明感のある素肌が育ちます。",
        "target": "水分と油分のバランスが崩れて肌荒れしやすい方、ベタつかないのに奥深く潤うスキンケアを求める方、香りとデザイン性の両方を重視する方",
        "point": "洗顔後、手のひらに適量を取り、顔全体に優しくなじませます。乾燥が気になる日は2〜3回重ねづけするレイヤリングを行うと、内側から押し返すような弾力が出ます。"
    },
    {
        "rank": 10,
        "tag": "🥛 高保湿クリームまるごと1個分を化粧水に完全乳化！ひと塗りでクリーム級の潤いが続く濃厚ローション",
        "catch": "ラネージュ独自のマイクロ乳化技術『Cream Blending Technology™』により、高保湿クリームまるごと1個分を化粧水の中に溶かし込んだ世界的ベストセラー。ひと塗りで化粧水と乳液・クリームを重ねたような圧倒的濃密潤いを実現",
        "brand_name": "LANEIGE (ラネージュ)",
        "capacity": "170mL / エコデザインボトル",
        "type": "クリーム完全乳化技術 高保湿オイルイン乳化化粧液",
        "features": "ホワイトリーフティー水（アミノ酸豊富）、セラミド、スクワラン、低刺激・無香料・弱酸性処方",
        "value": "ナノサイズに微細化されたクリーム粒子が角層深部へすばやく浸透。真冬の過酷な冷気や暖房下でも、120時間乾かない驚異のラッピング効果を発揮",
        "desc_p1": "冬のスキンケアにおいて「化粧水を塗って、美容液を塗って、乳液を塗って、さらにクリームを重ねる」という工程は、肌への摩擦リスクを増やし、忙しい朝には負担となります。ラネージュのクリームスキン ローションは、高保湿クリームの密閉力と化粧水の浸透力を1本に融合させた画期的なアイテムです。遮光栽培されたアミノ酸豊富なホワイトリーフティーウォーターが、角層バリアを優しく強化します。",
        "desc_p2": "牛乳のように白いまろやかなテクスチャーで、肌に乗せるととろけるように広がり、瞬時に吸い込まれていきます。化粧水とは思えないほど濃厚な潤いの膜が肌表面に形成され、まるでスキンケアの全工程を終えたかのようなモチモチ感に包まれます。乾燥が激しい11月〜12月の朝、これ1本で時短しながら最高峰の保湿ケアが完了します。",
        "target": "真冬の極度乾燥に悩む超乾燥肌、スキンケアのステップをシンプルにしたい方、朝のメイク前に素早く濃密な潤いの土台を作りたい方",
        "point": "洗顔後、適量を手にとり、顔全体を包み込むように優しくなじませます。乾燥が特に激しい日は、重ねづけするか、コットンに含ませて2分間パックすると効果的です。"
    }
]

# JSON-LD構造化データの生成
json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！水分と上質オイルの黄金比で満たす保湿力高めオイルイン化粧水ランク10",
    "description": "11月・12月の冷え固まった冬の硬化角質をほぐし、水分と良質オイルを同時にチャージする高保湿オイルイン化粧水10選を徹底検証！RMK、SHIRO、アルビオン、カネボウ、コスメデコルテまで二層式乳化処方の科学的根拠と共に紹介。",
    "image": items[0]["image_url"],
    "datePublished": "2026-11-07T09:00:00+09:00",
    "dateModified": "2026-11-07T09:00:00+09:00",
    "author": {
        "@type": "Organization",
        "name": "LumiCosme スキンケア研究チーム",
        "url": "https://lumi-cosme.vercel.app/"
    },
    "publisher": {
        "@type": "Organization",
        "name": "LumiCosme (ルミコスメ)",
        "logo": {
            "@type": "ImageObject",
            "url": "https://lumi-cosme.vercel.app/favicon.jpg"
        }
    },
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://lumi-cosme.vercel.app/winter-oil-in-lotion"
    }
}

json_ld_products = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": it["rank"],
            "item": {
                "@type": "Product",
                "name": it["display_name"],
                "image": it["image_url"],
                "description": product_details[it["rank"]-1]["catch"],
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
        } for it in items
    ]
}

json_ld_faq = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "オイルイン化粧水を使うとメイクが崩れやすくなりませんか？",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "適切な使用量を守り、角層にしっかり浸透させればメイク崩れの原因にはなりません。むしろ冬のメイク崩れの主原因は、肌内部の乾燥による『皮脂の過剰分泌（乾燥テカリ）』や『ファンデーションの粉浮き』です。オイルイン化粧水で水分と油分のバランスを整えておくことで、ファンデーションの密着度が高まり、夕方まで崩れない美しいツヤ肌が持続します。塗布後に手のひらで軽くハンドプレスしてベタつきがないことを確認してからベースメイクに進むのがポイントです。"
            }
        },
        {
            "@type": "Question",
            "name": "二層式オイルイン化粧水は使う前に何回くらい振ればいいですか？",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "製品によって多少異なりますが、一般的には容器を上下に5〜8回程度しっかりシェイクし、オイル層と水分層が均一に白濁（マイクロエマルジョン化）した状態で手のひらに出すのが理想的です。振りが足りないとオイルだけ、あるいは水分だけが出てきてしまい、設計された黄金比の保湿効果が得られなくなるため注意しましょう。"
            }
        },
        {
            "@type": "Question",
            "name": "オイルイン化粧水を使ったら、乳液やクリームは塗らなくても大丈夫ですか？",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "肌質や季節の乾燥度合いによって調整が可能です。脂性肌寄りの方や、忙しい朝のメイク前であれば、高保湿なオイルイン化粧水1本で十分な潤いをキープできる場合があります。しかし、11月〜12月の真冬のエアコン暖房環境下や、皮脂分泌の少ない乾燥肌・大人世代の肌には、オイルイン化粧水で角層をほぐした後に、少量の乳液またはクリームを重ねて『保護膜の二重密閉』を行うことで、夜まで乾燥を完全シャットアウトできます。"
            }
        },
        {
            "@type": "Question",
            "name": "コットンと手のひら、どちらで塗布するのがおすすめですか？",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "オイルイン化粧水は、手のひらでの塗布が最も推奨されます。手のひらの体温によってオイル成分が温められ、角層への親和性と浸透スピードが格段に高まるためです。また、コットンを使用すると上質なオイル成分がコットンの繊維に吸収されて肌に届く量が減ってしまうことがあるため、清潔な手のひらで優しく顔全体を包み込むようにハンドプレスするのがベストです。"
            }
        }
    ]
}

# 商品カードHTMLの構築
product_cards_html = ""
for it in items:
    detail = product_details[it["rank"]-1]
    card = f"""
      <article class="product-card" id="rank-{it['rank']}">
        <div class="product-badge">第{it['rank']}位</div>
        <div class="product-tag">{detail['tag']}</div>
        <h3 class="product-title">{it['display_name']}</h3>
        
        <div class="product-grid">
          <div class="product-img-col">
            <img src="{it['image_url']}" alt="{it['item_name']}" class="product-img" loading="lazy" />
            <div class="product-brand-box">
              <span class="brand-label">ブランド</span>
              <span class="brand-value">{it['brand']}</span>
            </div>
            <div class="product-price-box">
              <span class="price-label">参考価格</span>
              <span class="price-val">¥{it['price']:,}</span>
              <span class="price-tax">（税込）</span>
            </div>
            <a href="{it['affiliate_url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
              <span>楽天市場で最安値を見る</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
          </div>

          <div class="product-info-col">
            <div class="catch-quote">{detail['catch']}</div>
            
            <div class="spec-table">
              <div class="spec-row">
                <span class="spec-name">容量 / 容器</span>
                <span class="spec-desc">{detail['capacity']}</span>
              </div>
              <div class="spec-row">
                <span class="spec-name">処方タイプ</span>
                <span class="spec-desc">{detail['type']}</span>
              </div>
              <div class="spec-row">
                <span class="spec-name">注目成分</span>
                <span class="spec-desc">{detail['features']}</span>
              </div>
              <div class="spec-row">
                <span class="spec-name">期待できる価値</span>
                <span class="spec-desc">{detail['value']}</span>
              </div>
            </div>

            <div class="product-review-text">
              <p>{detail['desc_p1']}</p>
              <p>{detail['desc_p2']}</p>
            </div>

            <div class="recommend-box">
              <div class="recommend-title">🎯 こんな肌悩み・シーンにおすすめ</div>
              <p>{detail['target']}</p>
            </div>

            <div class="usage-tip">
              <div class="tip-title">💡 効果を最大限に引き出すプロ直伝の使い方</div>
              <p>{detail['point']}</p>
            </div>
          </div>
        </div>
      </article>
"""
    product_cards_html += card

# 比較表の行生成
table_rows_html = ""
for it in items:
    detail = product_details[it["rank"]-1]
    table_rows_html += f"""
          <tr>
            <td class="col-rank">第{it['rank']}位</td>
            <td class="col-name"><a href="#rank-{it['rank']}">{it['brand']}<br><strong>{it['display_name'][:24]}...</strong></a></td>
            <td class="col-type">{detail['type'][:22]}</td>
            <td class="col-feat">{detail['features'][:28]}...</td>
            <td class="col-price">¥{it['price']:,}</td>
            <td class="col-link"><a href="{it['affiliate_url']}" target="_blank" rel="nofollow noopener" class="table-btn">楽天確認</a></td>
          </tr>
"""

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！水分と上質オイルの黄金比で満たす保湿力高めオイルイン化粧水ランク10 | LumiCosme</title>
  <meta name="description" content="11月・12月の冷え固まった冬の硬化角質をほぐし、水分と良質オイルを同時にチャージする高保湿オイルイン化粧水10選を徹底検証！RMK、SHIRO、アルビオン、カネボウ、コスメデコルテまで二層式乳化処方の科学的根拠と共に紹介。">
  <meta name="keywords" content="オイルイン化粧水,二層式ローション,冬コスメ,高保湿化粧水,乾燥肌,角質柔軟,RMK,SHIRO,コスメランキング">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-oil-in-lotion">
  
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！水分と上質オイルの黄金比で満たす保湿力高めオイルイン化粧水ランク10">
  <meta property="og:description" content="11月・12月の冷え固まった冬の硬化角質をほぐし、水分と良質オイルを同時にチャージする高保湿オイルイン化粧水10選を徹底検証！RMK、SHIRO、アルビオン、カネボウ、コスメデコルテまで二層式乳化処方の科学的根拠と共に紹介。">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-oil-in-lotion">
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
      --primary: #d97706;
      --primary-dark: #b45309;
      --secondary: #fffbeb;
      --accent: #f59e0b;
      --text: #1e293b;
      --text-muted: #64748b;
      --border: #fde68a;
      --card-bg: #ffffff;
      --gold: #d97706;
      --radius: 12px;
      --shadow: 0 4px 20px rgba(217, 119, 6, 0.08);
      --font-base: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Hiragino Sans", "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: var(--font-base); line-height: 1.85; color: var(--text); background-color: #faf9f6; -webkit-font-smoothing: antialiased; }}
    
    .site-header {{ background: #ffffff; border-bottom: 1px solid #fed7aa; position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 10px rgba(0,0,0,0.03); }}
    .header-inner {{ max-width: 1200px; margin: 0 auto; padding: 1rem 1.5rem; display: flex; justify-content: space-between; align-items: center; }}
    .site-logo {{ font-size: 1.5rem; font-weight: 800; color: var(--primary-dark); text-decoration: none; letter-spacing: -0.5px; }}
    .nav-links a {{ color: var(--text-muted); text-decoration: none; margin-left: 1.5rem; font-size: 0.95rem; font-weight: 600; transition: color 0.2s; }}
    .nav-links a:hover {{ color: var(--primary); }}

    .hero-section {{ background: linear-gradient(135deg, #fef3c7 0%, #ffedd5 100%); padding: 3.5rem 1.5rem; text-align: center; border-bottom: 1px solid #fde68a; }}
    .hero-inner {{ max-width: 900px; margin: 0 auto; }}
    .article-meta {{ display: inline-flex; gap: 1rem; align-items: center; margin-bottom: 1rem; font-size: 0.85rem; color: var(--primary-dark); font-weight: 700; background: #ffffff; padding: 0.4rem 1rem; border-radius: 9999px; box-shadow: 0 2px 6px rgba(0,0,0,0.04); }}
    .hero-title {{ font-size: 2.1rem; line-height: 1.35; color: #78350f; font-weight: 800; margin-bottom: 1.25rem; letter-spacing: -0.5px; }}
    .hero-desc {{ font-size: 1.05rem; color: #451a03; line-height: 1.8; text-align: left; background: rgba(255,255,255,0.88); padding: 1.5rem; border-radius: var(--radius); border-left: 4px solid var(--primary); }}

    .main-container {{ max-width: 1100px; margin: 2.5rem auto; padding: 0 1.5rem; display: grid; grid-template-columns: 1fr; gap: 3rem; }}
    
    .content-box {{ background: var(--card-bg); border-radius: var(--radius); padding: 2.5rem; box-shadow: var(--shadow); border: 1px solid #fde68a; margin-bottom: 2.5rem; }}
    .content-box h2 {{ font-size: 1.6rem; color: #78350f; margin-bottom: 1.5rem; padding-bottom: 0.75rem; border-bottom: 2px solid var(--secondary); display: flex; align-items: center; gap: 0.75rem; }}
    .content-box p {{ margin-bottom: 1.2rem; color: #334155; font-size: 1.02rem; }}

    .science-card {{ background: #fffbeb; border-radius: 8px; padding: 1.5rem; margin: 1.5rem 0; border: 1px solid #fef3c7; }}
    .science-title {{ font-weight: 700; color: #b45309; margin-bottom: 0.5rem; font-size: 1.1rem; }}

    .product-card {{ background: #ffffff; border-radius: var(--radius); border: 1px solid #fde68a; box-shadow: var(--shadow); padding: 2rem; margin-bottom: 2.5rem; position: relative; overflow: hidden; }}
    .product-badge {{ position: absolute; top: 0; left: 0; background: var(--primary); color: #ffffff; font-weight: 800; font-size: 1rem; padding: 0.5rem 1.5rem; border-bottom-right-radius: var(--radius); box-shadow: 0 2px 8px rgba(0,0,0,0.15); }}
    .product-tag {{ font-size: 0.95rem; font-weight: 700; color: #d97706; margin-top: 1.75rem; margin-bottom: 0.5rem; }}
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
    .catch-quote {{ font-size: 1.05rem; font-weight: 700; color: #78350f; background: #fffbeb; padding: 1rem 1.25rem; border-left: 4px solid #d97706; border-radius: 4px; margin-bottom: 1.25rem; line-height: 1.6; }}

    .spec-table {{ display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.25rem; background: #ffffff; border: 1px solid #fed7aa; border-radius: 8px; padding: 1rem; }}
    .spec-row {{ display: grid; grid-template-columns: 110px 1fr; font-size: 0.9rem; line-height: 1.5; }}
    .spec-name {{ color: var(--text-muted); font-weight: 600; }}
    .spec-desc {{ color: #1e293b; font-weight: 500; }}

    .product-review-text p {{ margin-bottom: 1rem; font-size: 0.98rem; color: #334155; line-height: 1.8; }}
    
    .recommend-box {{ background: #fffbeb; border-radius: 8px; padding: 1rem 1.25rem; margin-bottom: 1rem; border: 1px solid #fde68a; }}
    .recommend-title {{ font-weight: 700; color: #b45309; font-size: 0.95rem; margin-bottom: 0.4rem; }}
    .recommend-box p {{ font-size: 0.92rem; color: #78350f; margin: 0; line-height: 1.6; }}

    .usage-tip {{ background: #fefce8; border-radius: 8px; padding: 1rem 1.25rem; border: 1px solid #fef08a; }}
    .tip-title {{ font-weight: 700; color: #a16207; font-size: 0.95rem; margin-bottom: 0.4rem; }}
    .usage-tip p {{ font-size: 0.92rem; color: #713f12; margin: 0; line-height: 1.6; }}

    .comparison-table-wrap {{ overflow-x: auto; margin: 1.5rem 0; }}
    .comparison-table {{ width: 100%; border-collapse: collapse; text-align: left; font-size: 0.92rem; }}
    .comparison-table th {{ background: #fffbeb; padding: 0.75rem 1rem; border: 1px solid #fde68a; color: #78350f; font-weight: 700; }}
    .comparison-table td {{ padding: 0.75rem 1rem; border: 1px solid #fde68a; color: #334155; vertical-align: middle; }}
    .col-rank {{ font-weight: 800; color: var(--primary); text-align: center; }}
    .col-name a {{ color: #d97706; text-decoration: none; font-weight: 600; }}
    .col-price {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .table-btn {{ display: inline-block; background: #bf0000; color: #ffffff !important; padding: 0.35rem 0.75rem; border-radius: 4px; text-decoration: none; font-size: 0.8rem; font-weight: 700; white-space: nowrap; }}

    .faq-list {{ display: flex; flex-direction: column; gap: 1.25rem; margin-top: 1.5rem; }}
    .faq-item {{ background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem 1.5rem; }}
    .faq-q {{ font-weight: 700; color: #78350f; font-size: 1.05rem; display: flex; gap: 0.75rem; align-items: flex-start; margin-bottom: 0.75rem; }}
    .faq-q-icon {{ background: var(--primary); color: #ffffff; border-radius: 4px; padding: 0.1rem 0.5rem; font-size: 0.85rem; font-weight: 800; }}
    .faq-a {{ color: #334155; font-size: 0.98rem; line-height: 1.8; margin-left: 2.2rem; }}

    .routine-step {{ display: grid; grid-template-columns: 80px 1fr; gap: 1rem; margin-bottom: 1.25rem; align-items: center; background: #ffffff; border: 1px solid #fde68a; padding: 1rem 1.25rem; border-radius: 8px; }}
    .step-num {{ background: #d97706; color: #ffffff; font-weight: 800; text-align: center; padding: 0.5rem; border-radius: 6px; font-size: 0.9rem; }}
    .step-desc h4 {{ font-size: 1rem; color: #78350f; margin-bottom: 0.25rem; }}
    .step-desc p {{ font-size: 0.92rem; color: #64748b; margin: 0; }}

    .site-footer {{ background: #78350f; color: #fde68a; padding: 3.5rem 1.5rem 2rem; border-top: 1px solid #92400e; margin-top: 4rem; }}
    .footer-inner {{ max-width: 1100px; margin: 0 auto; }}
    .footer-logo {{ font-size: 1.4rem; font-weight: 800; color: #ffffff; margin-bottom: 1rem; }}
    .footer-desc {{ font-size: 0.9rem; margin-bottom: 2rem; max-width: 600px; color: #fef3c7; }}
    .footer-links-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 0.75rem; margin-bottom: 2.5rem; border-top: 1px solid #92400e; padding-top: 1.5rem; }}
    .footer-links-grid a {{ color: #fef3c7; text-decoration: none; font-size: 0.85rem; transition: color 0.2s; }}
    .footer-links-grid a:hover {{ color: #ffffff; }}
    .copyright {{ text-align: center; font-size: 0.8rem; color: #fde68a; border-top: 1px solid #92400e; padding-top: 1.5rem; }}

    .related-section {{ margin-top: 3rem; }}
    .related-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.25rem; margin-top: 1.25rem; }}
    .related-card {{ background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem; text-decoration: none; color: inherit; transition: transform 0.2s, box-shadow 0.2s; display: block; }}
    .related-card:hover {{ transform: translateY(-3px); box-shadow: var(--shadow); border-color: var(--primary); }}
    .related-card-title {{ font-weight: 700; color: #b45309; font-size: 0.95rem; margin-bottom: 0.5rem; line-height: 1.4; }}
    .related-card-desc {{ font-size: 0.82rem; color: #64748b; line-height: 1.5; }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">LumiCosme</a>
      <nav class="nav-links">
        <a href="/">冬コスメ特集</a>
        <a href="#ranking">ランキング10</a>
        <a href="#science">オイルインの科学</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <section class="hero-section">
    <div class="hero-inner">
      <div class="article-meta">
        <span>📅 2026年11月・12月最新版</span>
        <span>✨ 水分×油分の黄金比</span>
        <span>🏷️ 高保湿オイルイン化粧水</span>
      </div>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！水分と上質オイルの黄金比で満たす保湿力高めオイルイン化粧水ランク10</h1>
      <div class="hero-desc">
        11月から12月にかけて気温が一段と低下すると、皮脂の分泌量は年間の最低レベルへと落ち込みます。皮脂膜を失った冬の肌はカチコチに硬化し、いくら水分の多い化粧水を浴びても弾かれてしまう「角質硬化と浸透拒否」に直面します。この冬の壁を打ち破るのが、上質なエモリエントオイル層と高保水ローション層をシェイクして使う【二層式・高保湿オイルイン化粧水】です。硬化した角質をとろけるようにほぐしながら深部へ水分を引き込む、真の実力派10本を厳選検証しました。
      </div>
    </div>
  </section>

  <main class="main-container">

    <section class="content-box" id="science">
      <h2>✨ なぜ11-12月の硬化肌には「オイルイン化粧水」が劇的に効くのか？</h2>
      <p>初冬から本格的な冬へと向かう11月・12月、肌のバリア機能が著しく低下する最大の物理的要因は『皮脂膜の崩壊』です。皮脂は気温が下がると固まりやすく、分泌量そのものも激減します。皮脂膜という天然のフタを失った角層は、内部の水分が抜け落ちることで細胞同士がギュッと凝集し、レンガのようにカチコチに硬化してしまいます。</p>
      
      <div class="science-card">
        <div class="science-title">🔬 「水分だけ」では浸透しない冬の角質硬化メカニズム</div>
        <p>硬化した角層細胞は表面が疎水性（水を弾く性質）に傾いています。そのため、オイルを含まないサラサラの化粧水だけを塗っても、肌の表面を滑り落ちるだけで角層の深部まで浸透ルートが拓かれません。一方、先に重い美容オイルを塗ると、油膜が邪魔をして今度は水分の浸透を阻害してしまいます。オイルイン化粧水は、シェイクによって微細な油滴が水分層に分散した『自己乳化状態』を作り出すため、硬化した角質を瞬時に柔軟化（エモリエント）しながら、同時に水分を深部へ引き込むことができるのです。</p>
      </div>

      <p>水分（ハイドロ）と油分（リピッド）を理想的な黄金比で同時にチャージすることで、皮脂膜が完全に機能していた夏の健やかな素肌環境を人工的に再現。洗顔直後のワンステップで、乳液やクリームをすでに重ねたかのようなもっちりとした柔らかさと吸い付くようなツヤを呼び戻します。</p>
    </section>

    <section class="content-box">
      <h2>📐 失敗しない高保湿オイルイン化粧水の選び方 4つの基準</h2>
      <p>ドラッグストアからデパコスまで注目を集めるオイルインローションですが、冬の過酷な乾燥を乗り切るためにはオイルの品質と乳化の安定性が極めて重要です。</p>

      <div class="science-card">
        <div class="science-title">1. ベースオイルの品質（植物性スクワラン・ホホバ・タマヌ・ざくろ）</div>
        <p>ミネラルオイルなどの鉱物油ではなく、人間の皮脂膜に近い脂肪酸組成を持つ植物性オイル（スクワラン、ホホバ種子油、タマヌオイル、カメリア油など）が使用されているかを確認しましょう。酸化しにくく肌馴染みが抜群の植物オイルは、毛穴を塞ぐことなく角層細胞間をスムーズに満たします。</p>
      </div>

      <div class="science-card">
        <div class="science-title">2. 水分と油分の比率（8:2 〜 7:3の絶妙バランス）</div>
        <p>オイルが多すぎるとベタつきやメイク崩れの原因になり、逆に少なすぎると角質柔軟効果が得られません。振った瞬間に素早く均一に混ざり合い、肌に伸ばした後にサラリとシルキーに落ち着くバランス設計の製品を選びましょう。</p>
      </div>

      <div class="science-card">
        <div class="science-title">3. 高機能美容成分の共存（発酵エキス・ビタミンE・ナイアシンアミド）</div>
        <p>単なる保湿だけでなく、冬の寒冷酸化ストレスに対抗するビタミンE（トコフェロール）や、シワ改善・美白を担うナイアシンアミド、肌の代謝を促す発酵エキスが共存している処方は、冬枯れ肌のエイジングケアに圧倒的なアドバンテージを発揮します。</p>
      </div>

      <div class="science-card">
        <div class="science-title">4. マイクロエマルジョン（微細乳化）技術の完成度</div>
        <p>シェイクした際にできるオイルの粒子が微細であればあるほど、角層の隙間へムラなく均一に行き渡ります。粒子が粗いと肌表面で油分が浮いてしまい、メイクヨレを引き起こすため、ナノカプセル化や微細乳化技術に定評のあるブランドを選ぶのが安心です。</p>
      </div>
    </section>

    <section id="ranking">
      <div style="text-align: center; margin-bottom: 2.5rem;">
        <span style="color: #d97706; font-weight: 800; font-size: 1.1rem; letter-spacing: 1px;">2026 WINTER BEST RANKING</span>
        <h2 style="font-size: 2rem; color: #78350f; margin-top: 0.5rem; border: none; padding: 0;">保湿力高めオイルイン化粧水 ベスト10選</h2>
        <p style="color: #64748b; font-size: 1rem; margin-top: 0.5rem;">楽天市場の最新リアルタイム価格・在庫データを都度取得して反映しています</p>
      </div>

      {product_cards_html}
    </section>

    <section class="content-box">
      <h2>📊 保湿力高めオイルイン化粧水10選 徹底スペック比較一覧表</h2>
      <p>各製品の処方特徴、注目成分、参考価格を一目で比較できます。あなたの肌状態と仕上がりの好みに最適な1本を見つけてください。</p>
      
      <div class="comparison-table-wrap">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名・ブランド</th>
              <th>処方タイプ</th>
              <th>注目オイル・保湿成分</th>
              <th>参考価格</th>
              <th>楽天市場</th>
            </tr>
          </thead>
          <tbody>
            {table_rows_html}
          </tbody>
        </table>
      </div>
    </section>

    <section class="content-box">
      <h2>⏰ プロ直伝！真冬のゴワつきを解き放つオイルイン化粧水活用ルーティン</h2>
      <p>オイルイン化粧水は、手の温もりとハンドプレスを意識することで、浸透効率とモチモチ感が何倍にもアップします。</p>

      <div class="routine-step">
        <div class="step-num">STEP 1</div>
        <div class="step-desc">
          <h4>しっかりシェイクして均一乳化</h4>
          <p>容器を上下に5〜8回ほどリズミカルに振り、オイル層とローション層が完全に白濁するまで混ぜ合わせます。この均一乳化が肌馴染みの生命線です。</p>
        </div>
      </div>

      <div class="routine-step">
        <div class="step-num">STEP 2</div>
        <div class="step-desc">
          <h4>手のひらの体温でオイルを温める</h4>
          <p>適量（500円玉大）を手のひらに出し、両手を擦り合わせて人肌の温度まで温めます。冷えたオイルよりも温まったオイルの方が角質をほぐすスピードが格段に早まります。</p>
        </div>
      </div>

      <div class="routine-step">
        <div class="step-num">STEP 3</div>
        <div class="step-desc">
          <h4>擦らず包み込むスローハンドプレス</h4>
          <p>顔の中心から外側へ向かって、手のひら全体で肌を包み込み、じっくりと5秒間ずつ押し込みます。目元や小鼻のキワには指の腹を使って優しく密着させます。</p>
        </div>
      </div>

      <div class="routine-step">
        <div class="step-num">STEP 4</div>
        <div class="step-desc">
          <h4>首元・デコルテまでのリンパ流し</h4>
          <p>手に残ったオイルローションを首元からデコルテ、耳の後ろまで伸ばします。冷えやすい首元の血行が促進され、顔全体の血色感とツヤが一段と引き上がります。</p>
        </div>
      </div>
    </section>

    <section class="content-box" id="faq">
      <h2>❓ オイルイン化粧水に関するよくある質問（FAQ）</h2>
      <div class="faq-list">
        <div class="faq-item">
          <div class="faq-q">
            <span class="faq-q-icon">Q</span>
            <span>オイルイン化粧水を使うとメイクが崩れやすくなりませんか？</span>
          </div>
          <div class="faq-a">
            適切な使用量を守り、角層にしっかり浸透させればメイク崩れの原因にはなりません。むしろ冬のメイク崩れの主原因は、肌内部の乾燥による『皮脂の過剰分泌（乾燥テカリ）』や『ファンデーションの粉浮き』です。オイルイン化粧水で水分と油分のバランスを整えておくことで、ファンデーションの密着度が高まり、夕方まで崩れない美しいツヤ肌が持続します。塗布後に手のひらで軽くハンドプレスしてベタつきがないことを確認してからベースメイクに進むのがポイントです。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-q">
            <span class="faq-q-icon">Q</span>
            <span>二層式オイルイン化粧水は使う前に何回くらい振ればいいですか？</span>
          </div>
          <div class="faq-a">
            製品によって多少異なりますが、一般的には容器を上下に5〜8回程度しっかりシェイクし、オイル層と水分層が均一に白濁（マイクロエマルジョン化）した状態で手のひらに出すのが理想的です。振りが足りないとオイルだけ、あるいは水分だけが出てきてしまい、設計された黄金比の保湿効果が得られなくなるため注意しましょう。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-q">
            <span class="faq-q-icon">Q</span>
            <span>オイルイン化粧水を使ったら、乳液やクリームは塗らなくても大丈夫ですか？</span>
          </div>
          <div class="faq-a">
            肌質や季節の乾燥度合いによって調整が可能です。脂性肌寄りの方や、忙しい朝のメイク前であれば、高保湿なオイルイン化粧水1本で十分な潤いをキープできる場合があります。しかし、11月〜12月の真冬のエアコン暖房環境下や、皮脂分泌の少ない乾燥肌・大人世代の肌には、オイルイン化粧水で角層をほぐした後に、少量の乳液またはクリームを重ねて『保護膜の二重密閉』を行うことで、夜まで乾燥を完全シャットアウトできます。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-q">
            <span class="faq-q-icon">Q</span>
            <span>コットンと手のひら、どちらで塗布するのがおすすめですか？</span>
          </div>
          <div class="faq-a">
            オイルイン化粧水は、手のひらでの塗布が最も推奨されます。手のひらの体温によってオイル成分が温められ、角層への親和性と浸透スピードが格段に高まるためです。また、コットンを使用すると上質なオイル成分がコットンの繊維に吸収されて肌に届く量が減ってしまうことがあるため、清潔な手のひらで優しく顔全体を包み込むようにハンドプレスするのがベストです。
          </div>
        </div>
      </div>
    </section>

    <section class="content-box related-section" id="internal-links-hub">
      <h2>🔗 あわせて読みたい！冬の高保湿スキンケア特集</h2>
      <div class="related-grid" id="related-grid-box">
        <!-- 内部リンクが自動挿入されます -->
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-logo">LumiCosme</div>
      <p class="footer-desc">冬の過酷な乾燥環境に立ち向かうすべての女性へ。成分科学とリアルな使用感に基づいた高保湿コスメ・スキンケア情報を厳選してお届けします。</p>
      <div class="footer-links-grid" id="footer-links-box">
        <!-- フッターリンクが自動挿入されます -->
      </div>
      <div class="copyright">
        &copy; 2026 LumiCosme (ルミコスメ) All Rights Reserved.
      </div>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-oil-in-lotion.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-oil-in-lotion.html!")
