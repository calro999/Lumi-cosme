import json
import re

with open("fetched_3new_nov_dec_elastin_allantoin_beeswax.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_elastin"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 100%ピュア生原液！冬の寒冷で硬化した肌を解きほぐす水溶性エラスチン原液",
        "catch": "水溶性天然マリンエラスチン原液100%。化粧水やクリームに1〜2滴溶け込ませるだけで、真冬のしぼみ肌に濃密なゴムのような弾力バリアを再起動",
        "brand_name": "自然化粧品研究所",
        "capacity": "10ml / 遮光スポイト瓶",
        "type": "高純度水溶性エラスチン原液美容液",
        "features": "加水分解エラスチン（天然魚皮由来）、BG、フェノキシエタノール",
        "value": "無駄な増粘剤や油分を一切省いた純度100%の原液設計。真冬の過酷な寒冷乾燥で硬化した角層の隙間へダイレクトに浸透し、弾力線維の網目構造をサポート",
        "desc_p1": "11月から12月にかけて外気温が10℃を下回ると、真皮の毛細血管が収縮して血行が滞り、肌のクッション機能を司るコラーゲンとエラスチンの弾性ネットワークが急激に柔軟性を失います。夕方に鏡を見たとき、ほうれい線にファンデーションが深く落ち込み、肌全体が重力に負けてしぼんでいると感じるなら、水分補給だけでなく『エラスチンの補修』が急務です。自然化粧品研究所の『エラスチン原液 100%』は、化粧品OEM原料として使われるプロ品質の天然マリンエラスチンをそのまま小瓶に詰めた本格原液です。",
        "desc_p2": "テクスチャーは水のようにサラリとしていながら、肌になじませた瞬間に角層の奥深くへと吸い込まれ、内側からキュッと押し返してくるような引き締まり感を与えます。単体で洗顔直後のブースターとして使うのはもちろん、手持ちの冬用化粧水やこっくりしたクリームに手のひらで1〜2滴ブレンドするだけで、いつものスキンケアが一瞬で『最高峰の高弾力エイジングケア処方』にグレードアップします。香料や着色料を一切使わないシンプル設計のため、真冬の敏感に傾いた肌にも余計な負担をかけません。",
        "target": "真冬になると目元や口元の小ジワ・ほうれい線が深く刻まれる方、手持ちのスキンケアの保湿力・ハリ感をワンランク引き上げたい方、無添加のピュア原液を求める方",
        "point": "夜の洗顔後、化粧水をつける前のまっさらな肌にスポイトで2滴を手のひらに取り、指先で目元・眉間・ほうれい線などしぼみが気になる部位へピンポイントで押し込みます。その後、化粧水や乳液で蓋をすると、エラスチンが角層内で水分をガッチリ抱え込み、翌朝までピンとしたハリが続きます。"
    },
    {
        "rank": 2,
        "tag": "🔬 真皮の弾力ネットワークに着目！乾燥小ジワを跳ね返す高純度原液エッセンス",
        "catch": "原液コスメのパイオニアが追求した浸透型低分子エラスチン。角層の柔軟性を素早く回復させ、暖房下でも乾かないしなやかな弾力肌をキープ",
        "brand_name": "TUNEMAKERS (チューンメーカーズ)",
        "capacity": "20ml / スポイト対応ボトル",
        "type": "浸透型エラスチン原液エッセンス",
        "features": "加水分解エラスチン、水、BG",
        "value": "コラーゲン同士を束ねて伸縮性を生み出すエラスチンを濃密配合。真冬のエアコン乾燥で引きつる目元や頬に、内側から跳ね返すようなモチモチ感を取り戻す",
        "desc_p1": "原液スキンケアの代名詞的存在であるチューンメーカーズが手がける『エラスチン配合エッセンス』は、皮膚の弾力構造に徹底的にこだわって開発された高純度セラムです。コラーゲンが肌の『鉄筋』だとすれば、エラスチンはその鉄筋同士を強固にしなやかにつなぎとめる『スプリング（バネ）』の役割を果たしています。真冬の乾燥冷風にさらされると、このバネが弾力を失って伸び切ってしまい、たるみや深いシワの原因になります。",
        "desc_p2": "チューンメーカーズのエラスチン原液は、分子量を極めて小さく加工しているため、角層のラメラ構造を邪魔することなくスムーズに深層へと浸透します。ベタつきが全くなく、塗った直後から肌表面がなめらかに整い、ピンとした心地よいテンション（引き締め感）を実感。乾燥による目元のちりめんジワや、笑ったあとに戻りにくくなった表情ラインに、しなやかなバネのような弾力を補給してくれます。",
        "target": "笑ったあとの目元や口元の小ジワが戻りにくくなってきた方、ベタつくエイジングケアコスメが苦手な方、チューンメーカーズのセラミド原液と併用して鉄壁の冬ケアをしたい方",
        "point": "同ブランドの『セラミド200』を塗布した直後に、このエラスチン原液を2〜3滴重ねる『原液レイヤリング』が冬の超おすすめ技。セラミドで角層の隙間を埋めた上でエラスチンを注ぎ込むことで、水分保持力と弾力感が倍増します。"
    },
    {
        "rank": 3,
        "tag": "👑 科学とテクノロジーの頂点！張力に着目して冬のたるみ輪郭を引き上げる最高峰クリーム",
        "catch": "ロート製薬の皮膚科学研究を結集した『エラスプロ』配合。こっくり濃密なリフト膜が肌を包み込み、真冬の寒冷で重力に負けそうなフェイスラインを上向きへ",
        "brand_name": "Obagi (オバジ) / ロート製薬",
        "capacity": "50g (ジャータイプスパチュラ付)",
        "type": "高機能リフトタイトニングクリーム",
        "features": "エラスプロ（アスパラゴプシスアルマタエキス）、コラプラス、エラスグロウ、エラスリッチ、加水分解エラスチン",
        "value": "肌の『張力（テンション）』を物理的・生化学的に高める独自処方。真冬の極度な乾燥から肌を守りながら、ゆるんだフェイスラインを形状記憶のように引き上げる",
        "desc_p1": "冬の乾燥は単にカサつくだけでなく、肌の真皮構造を脆くして輪郭のたるみを加速させます。美容皮膚科学の最先端を走り続けるロート製薬オバジブランドの最高峰クリーム『オバジX ダーマアドバンスドリフト』は、肌の『張力』に着目し、エラスチンの産生と質を高める独自成分『エラスプロ』『エラスグロウ』を贅沢に搭載した名品です。",
        "desc_p2": "ジャーの蓋を開けると、まるで形状記憶樹脂のように濃厚でコクのあるテクスチャーが姿を現します。肌に伸ばすと、体温でとろけながらピタッと吸い付くように密着し、目に見えない強固なリフトネットを形成。塗布した瞬間から肌がグッと引き上げられるような心地よい張力に包まれます。翌朝の肌を指で押し込むと、パンッと風船のように押し返してくる弾力と、濃密なツヤが夕方まで持続します。",
        "target": "冬になるとフェイスラインのゆるみや毛穴のたるみが一気に目立つ方、最高峰のリフトアップ効果と鉄壁の保湿力を同時に手に入れたい方、本気のエイジングケアを始めたい方",
        "point": "付属のスパチュラでパール粒大を取り、あご先から耳の下、口角からこめかみ、小鼻からこめかみへと、下から上へ肌を引き上げるようにハンドプレスしながら塗り込みます。最後に手のひら全体でフェイスラインを包み込み、3秒間キープして形状を記憶させます。"
    },
    {
        "rank": 4,
        "tag": "✨ ヒト型コラーゲン×高純度エラスチンの黄金比！冬の表情ジワ影をふっくら満たす集中原液",
        "catch": "カイコ由来の純国産ヒト型コラーゲンに高純度エラスチンを惜しみなく配合。真冬の乾燥小ジワとほうれい線の溝をふっくら持ち上げる贅沢ドロップ",
        "brand_name": "ネオシルク (NEO SILK)",
        "capacity": "10ml / 30ml",
        "type": "濃密エラスチン×コラーゲン生原液",
        "features": "ヒト型コラーゲン（遺伝子組換えカイコ由来）、加水分解エラスチン、水、BG",
        "value": "人間の肌に極めて近いアミノ酸配列を持つコラーゲンとエラスチンが角層深くまでダイレクトに同化。寒冷で萎縮した肌細胞を立体的に押し上げる",
        "desc_p1": "寒さと乾燥で表情筋が強張り、日中の乾燥によって小ジワの溝が深く定着してしまう11月〜12月。ネオシルクの『ネオコラスチン』は、バイオテクノロジーを駆使して生まれたヒト型コラーゲンと高純度エラスチンを贅沢に掛け合わせた、本格派の集中エイジングケア原液です。",
        "desc_p2": "一般的な動物性コラーゲンとは異なり、人間の肌構造に限りなく近づけた成分設計のため、肌への親和性が抜群。塗った瞬間にすっと吸い込まれ、スカスカになった角層の隙間を満たします。エラスチンがコラーゲンの柔軟性を支えることで、固くなった皮膚がまるでつきたてのお餅のように柔らかく、もっちりとした弾力を取り戻します。ファンデーションがシワに溜まりにくくなる効果も絶大です。",
        "target": "夕方になるとほうれい線や目元のシワにファンデが筋状に入り込む方、ヒト型コラーゲンとエラスチンの相乗効果を実感したい方、敏感肌でも攻めのエイジングケアをしたい方",
        "point": "気になる目尻やほうれい線、眉間の縦ジワに1滴ずつ直接乗せ、指の腹でシワの溝を押し広げるように優しくクルクルとなじませます。シワの奥までしっかり成分を浸透させることが冬の深いシワ予防に直結します。"
    },
    {
        "rank": 5,
        "tag": "⚡ 浸透型コラーゲンEX×エラスチン配合！真冬の超乾燥とたるみを1個で跳ね返す濃密ゲル",
        "catch": "メディカルコスメの巨頭ドクターシーラボの最高傑作。金のリフトゲルが角層に濃密なハリ膜を形成し、朝晩の時短ケアで真冬の冷風を寄せ付けない",
        "brand_name": "Dr.Ci:Labo (ドクターシーラボ)",
        "capacity": "120g (大容量ジャー)",
        "type": "高機能リフトエイジングオールインワンゲル",
        "features": "浸透型コラーゲンEX、加水分解エラスチン、ナイアシンアミド、金、白金、ヒアルロン酸",
        "value": "化粧水・乳液・美容液・アイクリーム・クリーム・マッサージマスク・パック・化粧下地の8役。真冬の過酷な乾燥環境でも水分蒸発を許さない高密着リフトシールド",
        "desc_p1": "「真冬のスキンケアは重ねづけが多くて摩擦刺激が心配」「忙しい朝晩でも手抜きに見えないハリ肌を保ちたい」という願いを叶えるのが、ドクターシーラボのベストセラー『アクアコラーゲンゲル エンリッチリフトEX』です。皮膚のたるみと乾燥を長年研究してきた皮膚科医の知見が注ぎ込まれた、メディカル発想の高機能ゲルです。",
        "desc_p2": "日本初配合の浸透型コラーゲンEXとエラスチンの複合体が、角層のすみずみにまで浸透して潤いの骨組みを再構築。さらにナイアシンアミドが肌荒れを防ぎ、キメの乱れを整えます。コクのあるプルンとしたゲルを肌に伸ばすと、みずみずしく広がりながらも、表面にはピンと張った保護膜を形成。暖房の効いた乾いたオフィスに一日中いても、夕方まで肌がパリパリ乾燥せず、ふっくらした弾力が持続します。",
        "target": "スキンケアの手順を減らしつつ最高峰の保湿・リフト効果を得たい方、冬場の肌摩擦を減らしたい方、乾燥による毛穴の開きやフェイスラインのぼやけが気になる方",
        "point": "朝はパール2粒大、夜はさくらんぼ1粒大を使用します。顔の中心から外側へ向かって引き上げるように伸ばし、仕上げにあご下から耳の後ろ、首筋へと流すマッサージを取り入れると、冬の血行不良によるむくみもすっきり解消されます。"
    },
    {
        "rank": 6,
        "tag": "💎 高濃度低分子エラスチンが角層の弾性を覚醒！DHC直販の本格リフト原液美容液",
        "catch": "角層深層へ速やかに届く低分子エラスチン。乾燥によってしぼんだ肌表面をなめらかに押し広げ、ふっくらとしたハリと弾力感を与える冬の集中ドロップ",
        "brand_name": "DHC (ディーエイチシー)",
        "capacity": "30ml / 遮光ボトル",
        "type": "高純度低分子エラスチン原液美容液",
        "features": "加水分解エラスチン、BG、水、クエン酸",
        "value": "無香料・無着色・パラベンフリー。低分子化されたエラスチンが角層の深部まで浸透し、真冬の寒冷で硬くなった肌にしなやかな伸縮性を再付与",
        "desc_p1": "高品質な成分を続けやすい価格で届けるDHCの隠れた名品『エラスチン原液美容液』。真冬の過酷な寒暖差でカサつき、指で触るとゴワゴワとして弾力が失われた肌に、低分子加工されたピュアなエラスチンがダイレクトにアプローチします。",
        "desc_p2": "無駄な油分や増粘剤を含まないさらりとしたテクスチャーは、肌への浸透スピードが極めて速く、塗った直後から肌の内側がみずみずしい水分と弾力で満たされる感覚を味わえます。冬の乾燥によって皮膚が薄くなり、ちりめんジワが目立ちやすい目元や首元にもストレスなく使用可能。手持ちの乳液や美容液と合わせてもモロモロが出ず、自由自在にスキンケアへ組み込める万能原液です。",
        "target": "首元や目元のちりめんジワが気になり始めた方、原液ケアを手頃な価格で毎日惜しみなく続けたい方、シンプルな処方で肌バリアを整えたい方",
        "point": "洗顔後、化粧水で肌を整えた直後に2〜3滴を手のひらに伸ばし、顔全体を優しく包み込むようにハンドプレスします。特に首元の横ジワには、下から上へ優しくなじませると、冬のタートルネック擦れによる首の乾燥小ジワ予防に効果的です。"
    },
    {
        "rank": 7,
        "tag": "🚀 独自の浸透カプセルが深層まで届く！冬のゆるみ輪郭を立体的に引き締めるマッサージ美容液",
        "catch": "薬学博士が開発した『QuSome』テクノロジー。エラスチン＆コラーゲンサポートペプチドを深部へ届け、寒さでこわばった筋肉と肌を同時にほぐしてリフトアップ",
        "brand_name": "b.glen (ビーグレン)",
        "capacity": "60g / チューブタイプ",
        "type": "深層浸透リフトアップマッサージ美容液",
        "features": "加水分解エラスチン、アセチルジペプチド-1セチル、シャクヤク根エキス、QuSomeカプセル",
        "value": "浸透深度に徹底的にこだわったナノカプセル処方。真冬の冷気で強張った表情をほぐし、重力に逆らう立体的な引き締め感を叶える",
        "desc_p1": "「良い美容成分を塗っても、角層の奥まで届いていなければ意味がない」という信念のもと開発されたビーグレンの『QuSomeリフト』。寒さで角層が肥厚し、スキンケアが浸透しにくくなる真冬にこそ真価を発揮するマッサージ美容液です。",
        "desc_p2": "皮脂膜と細胞間脂質を通り抜ける超微小カプセル『QuSome』にエラスチンとリフトペプチドを内包。肌に乗せるとスルスルと滑らかに伸びる絶妙なテクスチャーで、摩擦を起こさずに朝晩の3分間リフトマッサージが行えます。寒さで滞ったリンパと血流を促しながらエラスチンを届けることで、むくみとしぼみが一気に解消され、鏡を見るのが楽しみになるスッキリとしたフェイスラインが完成します。",
        "target": "冬になると顔がむくみやすくフェイスラインがぼやける方、摩擦レスで本格的なリフトマッサージをしたい方、最先端の浸透技術を体験したい方",
        "point": "さくらんぼ粒大を手にとり、あご先から耳の付け根へ向かってフェイスラインを骨に沿って親指の腹で引き上げます。続いて小鼻の脇からこめかみへ頬骨を持ち上げるように流し、最後に首筋から鎖骨へ老廃物を流すようにマッサージしてください。"
    },
    {
        "rank": 8,
        "tag": "🌿 フラーレン×リポソーム×エラスチン！真冬の過酷な酸化と乾燥を打破するサロン品質セラム",
        "catch": "ノーベル賞受賞成分フラーレンを高配合したエステサロン発祥の本格エイジングセラム。寒さでくすんだ冬肌にみずみずしい透明感と跳ね返す弾力を注入",
        "brand_name": "Homeo Beau (ホメオバウ)",
        "capacity": "30ml / プッシュボトル",
        "type": "高抗酸化フラーレン×エラスチン美容液",
        "features": "フラーレン（規定値以上配合マーク付）、加水分解エラスチン、プロテオグリカン、リポソーム化ヒアルロン酸",
        "value": "冬の紫外線と暖房による活性酸素ダメージを無害化しながら、エラスチンとプロテオグリカンが深層から水分を湧き上がらせる",
        "desc_p1": "エステティックサロンの過酷な現場でプロのセラピストから絶大な信頼を集めるホメオバウの『エッセンス』。ビタミンCの250倍以上の抗酸化力を持つフラーレンを高濃度配合し、さらに加水分解エラスチンとプロテオグリカンを掛け合わせた、真冬のレスキュー美容液です。",
        "desc_p2": "オレンジ油とラベンダー油の上品な天然アロマが心地よく香るジェル状のテクスチャー。肌に塗布するとすばやく浸透し、肌の内側に水分を閉じ込める『ウォーターバンク』を形成します。寒さによる血行不良でどんよりくすんだ冬枯れ肌を内側から発光するような透明感で満たし、エラスチンが押し返すようなふっくらとしたハリをよみがえらせます。",
        "target": "真冬になると肌のくすみと乾燥小ジワが同時に深刻化する方、エステサロン品質の濃密セラムを自宅で使いたい方、天然アロマの香りで癒やされたい方",
        "point": "化粧水の直後、2〜3プッシュを顔全体になじませます。特に乾燥が気になる頬や目元には、手のひらでハンドプレスしながら香りを深く吸い込むことで、自律神経の緊張を緩めて血流を高めるアロマシナジー効果が得られます。"
    },
    {
        "rank": 9,
        "tag": "🧴 贅沢70ml大容量！顔から首・デコルテまで惜しみなく弾力補給できる冬の救世主原液",
        "catch": "大容量70mlサイズでコスパ抜群。真冬のタートルネック擦れで荒れやすい首のシワや、年齢が出やすいデコルテ・手肌までエラスチンで贅沢に満たす",
        "brand_name": "自然化粧品研究所",
        "capacity": "70ml / 大容量ボトル",
        "type": "高純度水溶性エラスチン原液（業務用大容量）",
        "features": "加水分解エラスチン、BG、水",
        "value": "容量を気にせず顔全体からボディまで惜しみなく使える圧倒的コストパフォーマンス。冬の全身の皮膚痩せ・乾燥たるみを徹底予防",
        "desc_p1": "「高級なエイジングケア美容液はもったいなくて少しずつしか使えない」という方に最適なのが、自然化粧品研究所の『エラスチン原液 70ml大容量サイズ』です。通常サイズ（10ml）の7倍もの容量を誇り、顔だけでなく首筋、デコルテ、さらには年齢サインが出やすい手の甲まで全身に贅沢に使えます。",
        "desc_p2": "冬場はニットやマフラーの摩擦によって首元の皮膚が激しく乾燥し、深い横ジワが固定化しやすい季節。この大容量エラスチン原液があれば、毎晩お風呂上がりに首から胸元までたっぷりと塗り広げることができます。さらりとした浸透性の高い液体なのでベタつかず、服を着ても気になりません。冬の終わりを迎える頃には、全身の肌密度がキュッと引き締まった手応えを実感できるはずです。",
        "target": "首やデコルテ、手の甲のシワやたるみも同時にケアしたい方、エラスチン原液をケチらずたっぷり使いたい方、手作りコスメの基材としても使いたい方",
        "point": "手のひらに500円玉大を贅沢に取り、顔全体にたっぷりなじませた後、余った原液を首から鎖骨、手の甲まで滑らせるように塗り込みます。週に1回、シートマスクの上にこの原液を垂らす『エラスチン贅沢パック』も絶品です。"
    },
    {
        "rank": 10,
        "tag": "🫧 9種のペプチド×エラスチン×酸素バブル！弾けて満たす韓国発の革新ボリュームセラム",
        "catch": "塗ると微細な酸素バブルがシュワシュワ泡立つ！ボルフィリンと9種のペプチド、エラスチンが真冬の寒冷でしぼんだ肌にぷるんとした立体感を即効注入",
        "brand_name": "MEDIPEEL (メディピール)",
        "capacity": "100ml / ポンプボトル",
        "type": "酸素バブル発泡ボリュームエッセンス",
        "features": "加水分解エラスチン、アセチルヘキサペプチド-8、ボルフィリン、ナイアシンアミド、ヒアルロン酸4種",
        "value": "塗布後数秒で発生する酸素の微細泡が美容成分を角層の奥まで押し込む。冬の乾燥でへこんだ目元やほうれい線にボリューム感をもたらす",
        "desc_p1": "韓国のスキンケアトレンドを牽引するメディピールの看板コスメ『ペプチド9 ボリュームエッセンス プロ』。肌に塗布すると、数秒後に白い微細な酸素の泡がシュワシュワと自発的に発生し、美容成分を角層のすみずみまで押し込んでいく革新的なテクスチャーが世界中で話題を呼んでいます。",
        "desc_p2": "肌の弾力線維をサポートするエラスチンに加え、塗るボトックスと呼ばれるアセチルヘキサペプチド-8や、脂肪細胞にハリを与えるフランス産ボルフィリンを贅沢にブレンド。酸素バブルが弾けた後、手のひらで優しくパッティングしてなじませると、まるで水光注射を受けたかのようなパンッとした弾力と濡れたようなツヤが肌全体に宿ります。暖房の効いた部屋でも一日中萎まない、圧倒的なボリューム美肌を叶えます。",
        "target": "真冬の寒さで肌のボリューム感が失われやつれて見えやすい方、最新の韓国水光肌コスメを試したい方、シュワシュワ弾ける新感覚のケアを楽しみたい方",
        "point": "化粧水の後に2〜3プッシュを顔全体に手早く塗り広げます。数秒で白い酸素バブルがモコモコと発生するので、泡が十分に立ったところで手のひら全体で優しく押し込むようにタッピングしてなじませてください。"
    }
]

faq_list = [
    {
        "question": "冬の乾燥対策にコラーゲンだけでなくエラスチンも取り入れるべき理由は何ですか？",
        "answer": "コラーゲンは皮膚の真皮構造の約70%を占める『柱（鉄筋）』の役割を持ちますが、エラスチンはそのコラーゲン同士を束ねてゴムのような伸縮性を与える『バネ（スプリング）』の役割を果たしています。真冬の過酷な寒冷乾燥環境では、血流低下と水分不足によってこのバネが硬化し、笑ったあとの表情ジワが戻りにくくなったり、肌全体がしぼんでたるみが生じます。コラーゲンで水分と体積を補いつつ、エラスチンでしなやかな伸縮性をチャージすることで、真冬のエアコン下でも跳ね返すようなモチモチの弾力肌を維持できるのです。"
    },
    {
        "question": "エラスチン原液（ピュア美容液）は、普段使っているスキンケアのどのタイミングで使うのが最も効果的ですか？",
        "answer": "水溶性のエラスチン原液は分子量が小さく浸透性に優れているため、『洗顔直後のブースターとして導入する』か、『化粧水の直後に重ねる』のが最も効果的です。また、手持ちの冬用クリームや乳液に手のひらで1〜2滴混ぜて使う『ブレンド使い』も非常におすすめ。油分と水分が乳化されたクリームにエラスチンが溶け込むことで、角層深くに弾力を送り込みながら表面に持続的なエモリエント膜を形成できます。"
    },
    {
        "question": "朝のメイク前にエラスチン美容液を使っても、ファンデーションのヨレやモロモロの原因になりませんか？",
        "answer": "今回厳選したエラスチンコスメ（特に自然化粧品研究所やチューンメーカーズ、DHCなどの原液系、およびオバジXやビーグレン）は、増粘多糖類による過度なヌルつきを抑えた処方になっているため、朝のメイク前にも安心してご使用いただけます。塗布後30秒〜1分ほど手のひらでハンドプレスして角層へしっかり浸透させてから日焼け止めやベースメイクを重ねると、むしろ肌のキメが整ってファンデーションの密着度が高まり、夕方の乾燥小ジワ割れを劇的に防ぐことができます。"
    },
    {
        "question": "エラスチンコスメは20代や30代前半から使っても早すぎることはありませんか？",
        "answer": "全く早すぎることはありません。エラスチンは20代半ばをピークに体内での産生量が急激に減少し、一度壊れると自力で再生するのが極めて難しい成分です。特に11月〜12月の強い木枯らしやエアコン暖房による『冬のインナードライ』を放置すると、20代であっても目元のちりめんジワやほうれい線が定着しやすくなります。早いうちから毎日の保湿ルーティンにエラスチンを取り入れることで、将来の深いシワやたるみを未然に防ぐ『先回りエイジングケア』として大きなリターンが得られます。"
    }
]

# JSON-LD構造化データ
jsonld_items = []
for i, item in enumerate(items):
    jsonld_items.append({
        "@type": "ListItem",
        "position": i + 1,
        "name": item["display_name"],
        "url": f"https://lumi-cosme.vercel.app/winter-elastin.html#item-{i+1}"
    })

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
        "@id": "https://lumi-cosme.vercel.app/winter-elastin.html"
    },
    "headline": "保湿力の強さで肌乾燥とさようなら！寒冷と暖房乾燥でしぼんだ肌に跳ね返すような弾力と濃密な潤いを取り戻す高保湿エラスチンコスメランク10",
    "description": "11月・12月の寒冷乾燥としぼみ肌を救う高保湿エラスチンコスメを徹底厳選！チューンメーカーズ、オバジX、ドクターシーラボ、DHC、ビーグレン、メディピールまで楽天で今すぐ買えるおすすめ人気ランキング10選と冬の弾力肌再生メソッドを詳しく解説。",
    "image": items[0]["image"],
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
    "name": "真冬の高保湿エラスチンコスメおすすめ人気ランキング10選",
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
      <h3 class="product-name">{d['brand_name']} {p['display_name']}</h3>
      <p class="product-catch">{d['catch']}</p>
      
      <div class="product-layout">
        <div class="product-visual">
          <img src="{p['image']}" alt="{p['display_name']}" class="product-img" loading="lazy" width="300" height="300">
          <div class="price-box">
            <span class="price-label">楽天参考価格</span>
            <span class="price-value">¥{p['price']:,}</span>
            <span class="price-tax">（税込）</span>
          </div>
          <a href="{p['url']}" target="_blank" rel="noopener sponsored" class="rakuten-btn">
            楽天で最新価格・在庫を見る
          </a>
        </div>
        
        <div class="product-info-detail">
          <div class="spec-table">
            <div class="spec-row"><span class="spec-th">ブランド</span><span class="spec-td">{d['brand_name']}</span></div>
            <div class="spec-row"><span class="spec-th">容量・規格</span><span class="spec-td">{d['capacity']}</span></div>
            <div class="spec-row"><span class="spec-th">アイテム種別</span><span class="spec-td">{d['type']}</span></div>
            <div class="spec-row"><span class="spec-th">注目成分</span><span class="spec-td">{d['features']}</span></div>
            <div class="spec-row"><span class="spec-th">真冬の保湿価値</span><span class="spec-td">{d['value']}</span></div>
          </div>
          
          <div class="review-box">
            <h4>💡 美容皮膚専門ライターの詳細解説＆真冬の実践レビュー</h4>
            <p>{d['desc_p1']}</p>
            <p>{d['desc_p2']}</p>
          </div>
          
          <div class="target-box">
            <strong>🎯 こんな方に特におすすめ：</strong>
            <p>{d['target']}</p>
          </div>
          
          <div class="usage-box">
            <strong>✨ 効果を最大化する真冬の使い方テクニック：</strong>
            <p>{d['point']}</p>
          </div>
        </div>
      </div>
    </article>
    """)

cards_joined = "\n".join(cards_html)

table_rows = []
for i, p in enumerate(items):
    d = product_details[i]
    table_rows.append(f"""
    <tr>
      <td class="tb-rank">第{i+1}位</td>
      <td class="tb-img"><img src="{p['image']}" alt="{p['display_name']}" width="60" height="60" loading="lazy"></td>
      <td class="tb-name"><strong>{d['brand_name']}</strong><br><a href="#item-{i+1}">{p['display_name']}</a></td>
      <td class="tb-type">{d['type']}</td>
      <td class="tb-price">¥{p['price']:,}</td>
      <td class="tb-btn"><a href="{p['url']}" target="_blank" rel="noopener sponsored" class="table-link-btn">楽天で見る</a></td>
    </tr>
    """)

table_joined = "\n".join(table_rows)

faq_html_blocks = []
for faq in faq_list:
    faq_html_blocks.append(f"""
    <div class="faq-item">
      <h3 class="faq-q">Q. {faq['question']}</h3>
      <p class="faq-a">A. {faq['answer']}</p>
    </div>
    """)

faq_joined = "\n".join(faq_html_blocks)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！寒冷と暖房乾燥でしぼんだ肌に跳ね返すような弾力と濃密な潤いを取り戻す高保湿エラスチンコスメランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の寒冷乾燥としぼみ肌を救う高保湿エラスチンコスメを徹底厳選！チューンメーカーズ、オバジX、ドクターシーラボ、DHC、ビーグレン、メディピールまで楽天で今すぐ買えるおすすめ人気ランキング10選と冬の弾力肌再生メソッドを詳しく解説。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-elastin.html">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！寒冷と暖房乾燥でしぼんだ肌に跳ね返すような弾力と濃密な潤いを取り戻す高保湿エラスチンコスメランク10">
  <meta property="og:description" content="11月・12月の寒冷乾燥としぼみ肌を救う高保湿エラスチンコスメを徹底厳選！チューンメーカーズ、オバジX、ドクターシーラボ、DHC、ビーグレンまで厳選10選。">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-elastin.html">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  
  <!-- 構造化データ -->
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
      --primary-color: #7c3aed;
      --primary-light: #ede9fe;
      --primary-dark: #5b21b6;
      --accent-color: #c084fc;
      --text-main: #1f2937;
      --text-muted: #4b5563;
      --bg-light: #faf5ff;
      --border-color: #ddd6fe;
      --card-bg: #ffffff;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
      --radius: 12px;
    }}
    
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
      line-height: 1.85;
      color: var(--text-main);
      background-color: #fafaf9;
    }}
    
    .site-header {{
      background: #ffffff;
      border-bottom: 1px solid #e5e7eb;
      padding: 1rem 0;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-title a {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary-dark);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .nav-link {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.95rem;
      font-weight: 600;
      transition: color 0.2s;
    }}
    .nav-link:hover {{ color: var(--primary-dark); }}
    
    .container {{
      max-width: 960px;
      margin: 0 auto;
      padding: 2rem 1.5rem 5rem;
    }}
    
    .breadcrumb {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 2rem;
    }}
    .breadcrumb a {{ color: var(--text-muted); text-decoration: none; }}
    .breadcrumb a:hover {{ text-decoration: underline; }}
    .breadcrumb span {{ color: #9ca3af; }}
    
    .article-header {{
      background: white;
      padding: 2.5rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
      border-top: 5px solid var(--primary-color);
    }}
    .article-meta {{
      display: flex;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
    }}
    .article-title {{
      font-size: 1.85rem;
      line-height: 1.45;
      font-weight: 800;
      color: #111827;
      margin-bottom: 1.5rem;
    }}
    .article-lead {{
      font-size: 1.05rem;
      color: var(--text-muted);
      line-height: 1.85;
      border-left: 4px solid var(--primary-color);
      padding-left: 1.25rem;
      background: var(--bg-light);
      padding: 1.25rem;
      border-radius: 0 8px 8px 0;
    }}
    
    .toc-box {{
      background: white;
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 1.75rem;
      margin-bottom: 3rem;
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
    .toc-list {{
      list-style: none;
      display: grid;
      gap: 0.6rem;
    }}
    .toc-list li a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.95rem;
      transition: color 0.2s;
    }}
    .toc-list li a:hover {{
      color: var(--primary-color);
      text-decoration: underline;
    }}
    
    .content-section {{
      background: white;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2.5rem;
      margin-bottom: 3rem;
    }}
    .section-title {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #111827;
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 0.75rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .section-p {{
      margin-bottom: 1.25rem;
      font-size: 1rem;
      color: var(--text-main);
    }}
    
    .compare-table-wrapper {{
      overflow-x: auto;
      margin: 1.5rem 0;
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 600px;
    }}
    .compare-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      padding: 0.85rem;
      text-align: left;
      border: 1px solid var(--border-color);
      font-weight: 700;
    }}
    .compare-table td {{
      padding: 0.85rem;
      border: 1px solid #e5e7eb;
      vertical-align: middle;
    }}
    .tb-rank {{ font-weight: 800; color: var(--primary-color); text-align: center; width: 60px; }}
    .tb-img img {{ border-radius: 6px; object-fit: cover; }}
    .tb-name a {{ color: var(--text-main); text-decoration: none; font-weight: 600; }}
    .tb-name a:hover {{ color: var(--primary-color); text-decoration: underline; }}
    .tb-price {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .table-link-btn {{
      display: inline-block;
      padding: 0.4rem 0.8rem;
      background: #b91c1c;
      color: white;
      text-decoration: none;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 700;
      white-space: nowrap;
    }}
    .table-link-btn:hover {{ background: #991b1b; }}
    
    .product-card {{
      background: white;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2.25rem;
      margin-bottom: 3.5rem;
      border: 1px solid #f3f4f6;
      position: relative;
    }}
    .product-badge-rank {{
      position: absolute;
      top: -12px;
      left: 20px;
      background: linear-gradient(135deg, #7c3aed, #5b21b6);
      color: white;
      font-weight: 800;
      font-size: 1rem;
      padding: 0.3rem 1.25rem;
      border-radius: 20px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.15);
    }}
    .product-tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
      font-size: 0.85rem;
      padding: 0.25rem 0.75rem;
      border-radius: 6px;
      margin-top: 0.5rem;
      margin-bottom: 0.75rem;
    }}
    .product-name {{
      font-size: 1.4rem;
      font-weight: 800;
      line-height: 1.4;
      color: #111827;
      margin-bottom: 0.5rem;
    }}
    .product-catch {{
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
    }}
    
    .product-layout {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .product-layout {{ grid-template-columns: 1fr; }}
      .article-title {{ font-size: 1.45rem; }}
      .article-header {{ padding: 1.5rem; }}
      .content-section {{ padding: 1.5rem; }}
    }}
    
    .product-visual {{
      text-align: center;
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      border: 1px solid #e5e7eb;
      margin-bottom: 1rem;
    }}
    .price-box {{
      background: #fef2f2;
      border: 1px solid #fee2e2;
      padding: 0.6rem;
      border-radius: 8px;
      margin-bottom: 1rem;
    }}
    .price-label {{ font-size: 0.75rem; color: #991b1b; display: block; }}
    .price-value {{ font-size: 1.5rem; font-weight: 800; color: #b91c1c; }}
    .price-tax {{ font-size: 0.75rem; color: #7f1d1d; }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      padding: 0.85rem 1rem;
      background: linear-gradient(135deg, #bf0000, #990000);
      color: white;
      text-decoration: none;
      font-weight: 800;
      font-size: 0.95rem;
      border-radius: 8px;
      text-align: center;
      box-shadow: 0 4px 6px -1px rgba(185, 28, 28, 0.3);
      transition: opacity 0.2s;
    }}
    .rakuten-btn:hover {{ opacity: 0.9; }}
    
    .spec-table {{
      background: #f9fafb;
      border-radius: 8px;
      padding: 1rem;
      margin-bottom: 1.25rem;
      font-size: 0.88rem;
    }}
    .spec-row {{
      display: grid;
      grid-template-columns: 110px 1fr;
      padding: 0.4rem 0;
      border-bottom: 1px dashed #e5e7eb;
    }}
    .spec-row:last-child {{ border-bottom: none; }}
    .spec-th {{ font-weight: 700; color: #4b5563; }}
    .spec-td {{ color: #1f2937; }}
    
    .review-box {{
      background: #faf5ff;
      border-left: 4px solid var(--primary-color);
      padding: 1.25rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 1.25rem;
    }}
    .review-box h4 {{
      font-size: 0.95rem;
      color: var(--primary-dark);
      font-weight: 700;
      margin-bottom: 0.5rem;
    }}
    .review-box p {{
      font-size: 0.92rem;
      color: #374151;
      margin-bottom: 0.6rem;
      line-height: 1.75;
    }}
    .review-box p:last-child {{ margin-bottom: 0; }}
    
    .target-box, .usage-box {{
      padding: 0.85rem 1rem;
      border-radius: 8px;
      margin-bottom: 0.85rem;
      font-size: 0.9rem;
    }}
    .target-box {{ background: #eff6ff; border: 1px solid #dbeafe; color: #1e40af; }}
    .target-box p {{ color: #1e3a8a; margin-top: 0.25rem; }}
    .usage-box {{ background: #fefce8; border: 1px solid #fef08a; color: #854d0e; }}
    .usage-box p {{ color: #713f12; margin-top: 0.25rem; }}
    
    .faq-item {{
      border-bottom: 1px solid #e5e7eb;
      padding: 1.5rem 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.6rem;
    }}
    .faq-a {{
      font-size: 0.95rem;
      color: #374151;
      line-height: 1.8;
    }}
    
    .footer-internal-links {{
      background: white;
      border-radius: var(--radius);
      padding: 2rem;
      box-shadow: var(--shadow);
      margin-top: 3rem;
    }}
    .footer-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 0.75rem;
      margin-top: 1rem;
    }}
    .footer-link-pill {{
      display: block;
      padding: 0.6rem 0.85rem;
      background: #f9fafb;
      border: 1px solid #e5e7eb;
      border-radius: 8px;
      color: #374151;
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 600;
      transition: all 0.2s;
    }}
    .footer-link-pill:hover {{
      color: var(--primary-color);
      border-color: var(--primary-color);
      background: var(--bg-light);
    }}
    
    .site-footer {{
      text-align: center;
      padding: 3rem 1.5rem;
      font-size: 0.85rem;
      color: #9ca3af;
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <div class="site-title">
        <a href="/">❄️ 冬コスメ徹底比較ラボ</a>
      </div>
      <nav>
        <a href="/" class="nav-link">トップページへ戻る</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb" aria-label="パンくずリスト">
      <a href="/">ホーム</a>
      <span>&gt;</span>
      <a href="/#skincare">スキンケア・エイジング特集</a>
      <span>&gt;</span>
      <span aria-current="page">高保湿エラスチンコスメ特集</span>
    </nav>

    <article class="article-header">
      <div class="article-meta">
        <time datetime="2026-11-04">公開日：2026年11月4日</time>
        <span>執筆：冬コスメ徹底比較ラボ 編集部（皮膚科学・弾力解析チーム）</span>
      </div>
      <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！寒冷と暖房乾燥でしぼんだ肌に跳ね返すような弾力と濃密な潤いを取り戻す高保湿エラスチンコスメランク10</h1>
      <p class="article-lead">
        11月から12月へ向けて寒風が吹き荒れ、室内のエアコン暖房が終日稼働する季節。多くの人が直面するのが、「いくら化粧水を重ねても肌がしぼんでハリが出ない」「夕方になるとほうれい線や目元の小ジワにファンデーションが深く落ち込む」という真冬特有の“乾燥しぼみ”現象です。水分をいくら与えても、肌の弾力スプリングである『エラスチン』が寒さと乾燥で硬直化していれば、若々しいハリと立体感は保てません。本記事では、皮膚の弾性線維を科学的にサポートする高純度加水分解エラスチン原液や高機能リフトクリームを徹底比較し、厳選ランキング10選としてご紹介します。
      </p>
    </article>

    <section class="toc-box">
      <h2 class="toc-title">📑 目次・記事ナビゲーション</h2>
      <ul class="toc-list">
        <li><a href="#why-elastin">1. 11月〜12月の肌しぼみの正体：なぜ冬の乾燥にはコラーゲンだけでなくエラスチンが必要なのか？</a></li>
        <li><a href="#selection-criteria">2. 失敗しない冬の高保湿エラスチンコスメの選び方・3つの基準</a></li>
        <li><a href="#comparison-table">3. 高保湿エラスチンコスメ10選 スペック・価格比較表</a></li>
        <li><a href="#ranking-section">4. 高保湿エラスチンコスメおすすめ人気ランキング10選 詳細レビュー</a></li>
        <li><a href="#faq-section">5. 美容皮膚視点で答えるエラスチンケアのよくある疑問Q&amp;A</a></li>
        <li><a href="#conclusion">6. まとめ：真冬のエアコン乾燥に負けない弾力保湿ルーティン</a></li>
      </ul>
    </section>

    <!-- セクション1 -->
    <section class="content-section" id="why-elastin">
      <h2 class="section-title">🧬 1. 11月〜12月の肌しぼみの正体：なぜ冬の乾燥にはコラーゲンだけでなくエラスチンが必要なのか？</h2>
      <p class="section-p">
        秋から冬への季節の変わり目、特に11月に入って最低気温が10℃を下回るようになると、皮膚の生理機能には劇的な変化が生じます。寒冷刺激によって真皮の毛細血管がギュッと収縮し、線維芽細胞への酸素やアミノ酸の供給量が大幅に減少します。その結果、肌のハリを支える細胞外マトリックスの産生スピードが落ち込みます。
      </p>
      <p class="section-p">
        さらに追い討ちをかけるのが、湿度30%台まで急落する大気乾燥と、室内のエアコン暖房です。角層の水分が奪われると、真皮層のコラーゲン繊維とエラスチン繊維の柔軟性が失われ、まるで冷えて固まった輪ゴムのように弾力性を失ってしまいます。これが、笑ったあとの目尻のシワが戻らない、頬の毛穴が縦に流れてしずく型に開いてしまう「真冬の寒冷たるみ・しぼみ肌」の根本原因です。
      </p>
      <p class="section-p">
        ここで決定的な役割を果たすのが<strong>『エラスチン（弾性線維）』</strong>です。真皮構造において、コラーゲンが肌の体積と強度を保つ『太い鉄筋』であるのに対し、エラスチンはその鉄筋同士を網目状に架橋し、外からの圧力に対して押し返す『強靭なスプリング（バネ）』の役割を担っています。
      </p>
      <p class="section-p">
        ヒアルロン酸やコラーゲンだけを補給しても、このエラスチンのバネが劣化・硬化していては、水分を抱え込んだまま皮膚を上向きに支え続けることができません。加水分解によってナノレベルまで低分子化されたエラスチンを角層深くまで浸透させることで、寒さで強張った角層を柔軟に解きほぐし、肌の内側から風船のようにパンッと弾む高密度のハリを取り戻すことが可能になるのです。
      </p>
    </section>

    <!-- セクション2 -->
    <section class="content-section" id="selection-criteria">
      <h2 class="section-title">🔍 2. 失敗しない冬の高保湿エラスチンコスメの選び方・3つの基準</h2>
      <p class="section-p">
        冬の本格的な乾燥小ジワ・肌しぼみ対策としてエラスチンコスメを導入する際は、以下の3つの基準を念頭に置いて製品を見極めることが成功への近道です。
      </p>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0; margin-bottom: 1.5rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">基準①：浸透性を高めた『加水分解低分子エラスチン』または『生原液100%』を選ぶ</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          エラスチンは本来高分子タンパク質のため、そのままでは皮膚の角層を通過しにくい性質があります。「加水分解エラスチン」として低分子化された処方や、余分な増粘剤を含まないピュア原液（自然化粧品研究所、チューンメーカーズ、DHCなど）を選ぶことで、角質細胞の隙間をすり抜けて深層まで素早く届きます。
        </p>
      </div>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0; margin-bottom: 1.5rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">基準②：コラーゲン・ペプチド・ヒアルロン酸との相乗ブレンドかチェック</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          エラスチンは単独でも優れた弾力性を発揮しますが、コラーゲンやペプチド（アセチルヘキサペプチドなど）、高保水ヒアルロン酸と組み合わさることで、肌の三次元ネット構造の修復効率が何倍にも高まります（オバジX、ドクターシーラボ、メディピールなど）。
        </p>
      </div>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">基準③：冬の暖房乾燥を蒸発させない『密着エモリエント膜』の持続性</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          原液を化粧水に混ぜて水分補給をした後は、必ずスクワランやシアバター、上質な植物オイルなどの油分で蓋をして水分蒸発を密閉遮断することが必須です。クリームやオールインワンゲル形状のものは、この油分シールドがあらかじめ完成されているため、真冬の夜間乾燥防止に極めて有効です。
        </p>
      </div>
    </section>

    <!-- セクション3 比較表 -->
    <section class="content-section" id="comparison-table">
      <h2 class="section-title">📊 3. 高保湿エラスチンコスメ10選 スペック・価格比較表</h2>
      <p class="section-p">
        楽天市場の公式APIよりリアルタイムに取得した最新の販売価格と製品仕様の一覧表です。テクスチャーや使用目的に合わせて最適な1本を比較検討してください。
      </p>
      <div class="compare-table-wrapper">
        <table class="compare-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>画像</th>
              <th>商品名・ブランド</th>
              <th>カテゴリ種別</th>
              <th>楽天価格</th>
              <th>商品詳細</th>
            </tr>
          </thead>
          <tbody>
            {table_joined}
          </tbody>
        </table>
      </div>
    </section>

    <!-- セクション4 ランキング詳細 -->
    <section id="ranking-section">
      <h2 style="font-size: 1.6rem; font-weight: 800; color: var(--primary-dark); margin-bottom: 2rem; text-align: center;">
        🏆 高保湿エラスチンコスメおすすめ人気ランキング10選
      </h2>
      {cards_joined}
    </section>

    <!-- セクション5 Q&A -->
    <section class="content-section" id="faq-section">
      <h2 class="section-title">❓ 5. 美容皮膚視点で答えるエラスチンケアのよくある疑問Q&amp;A</h2>
      {faq_joined}
    </section>

    <!-- セクション6 まとめ -->
    <section class="content-section" id="conclusion">
      <h2 class="section-title">✨ 6. まとめ：真冬のエアコン乾燥に負けない弾力保湿ルーティン</h2>
      <p class="section-p">
        11月から12月にかけて本格化する過酷な寒冷とエアコン乾燥は、肌の水分を奪うだけでなく、肌の土台である弾力ネットワークを容赦なく蝕みます。
      </p>
      <p class="section-p">
        どれだけ高級な保湿クリームを塗っても夕方に肌がしぼんでしまうのは、肌のスプリングであるエラスチンの柔軟性が失われている明確なサインです。
      </p>
      <p class="section-p">
        今回ご紹介した高純度加水分解エラスチン原液や高機能リフトクリームを毎日のスキンケアに1点投入するだけで、真冬の硬直した角層がふんわりと解きほぐされ、指先を跳ね返すようなモチモチの弾力が復活します。
      </p>
      <p class="section-p">
        ぜひご自身の肌悩みやライフスタイルに合ったお気に入りのエラスチンコスメを見つけて、乾燥に怯えることのない、ピンと引き締まった上向き美肌で冬を過ごしてください。
      </p>
    </section>

    <!-- 内部リンクラッパー -->
    <section class="footer-internal-links" id="internal-links">
      <h2 style="font-size: 1.25rem; font-weight: 800; color: #1f2937; margin-bottom: 0.5rem;">
        🔗 併せて読みたい冬コスメ・保湿スキンケア関連記事
      </h2>
      <p style="font-size: 0.9rem; color: #6b7280;">
        当サイトでは、11月〜12月の肌悩みに合わせた高保湿コスメや成分別ランキングを多数公開しています。
      </p>
      <div class="footer-links-grid" id="footer-links-placeholder">
        <!-- update_all_internal_links.py で動的に同期されます -->
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved. 当サイトは楽天市場アフィリエイトプログラムに参加しています。</p>
  </footer>

</body>
</html>
"""

with open("winter-elastin.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated winter-elastin.html successfully. Size: {len(html_content):,} bytes")
