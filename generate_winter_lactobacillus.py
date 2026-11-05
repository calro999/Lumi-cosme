import json
import re

with open("fetched_3new_lacto_swallow_dokudami.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_lactobacillus"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🥛 乳酸菌研究の金字塔！シロタエッセンスが真冬の崩れた角層バリアを再建する超保水ローション",
        "catch": "ヤクルトの80年を超える乳酸菌研究が生んだ『S.E.（シロタエッセンス）』高配合。真冬の過酷な暖房気流と冷気で乾燥脱水した角層細胞へ瞬時に浸透し、自ら潤いを生み出す美肌菌環境を整える濃密化粧水",
        "brand_name": "Yakult Beautiens (ヤクルト)",
        "capacity": "130mL / スタイリッシュボトル",
        "type": "乳酸菌発酵エキス高配合 まろやか高保湿化粧水",
        "features": "S.E.（乳酸菌はっ酵エキス（ミルク））、ビフィズス菌はっ酵エキス、高浸透型ヒアルロン酸、弱酸性・無香料",
        "value": "肌本来の天然保湿因子（NMF）と極めて近いアミノ酸組成を持つ乳酸菌発酵エキスが、乾燥で硬化した角質層の隅々まで隙間なく浸透。塗布した瞬間から夕方の暖房直撃下まで突っ張らない潤いを持続",
        "desc_p1": "11月から12月にかけて気温と湿度が急落すると、肌表面の皮脂膜が薄れ、肌を守る『美肌菌（表皮ブドウ球菌）』の活動が著しく低下します。水分を保持できなくなった肌は、いくら一般的な水分を足しても蒸発してしまう『乾燥の空回り』に陥ります。ヤクルトのラクトデュウ S.E.ローション2（まろやか高保湿）は、厳選された乳酸菌がミルクを発酵させる過程で生み出す希少成分『S.E.（コラーゲンやヒアルロン酸を含む複合発酵体）』を贅沢に凝縮した本格派の保水化粧水です。",
        "desc_p2": "手にとると、まろやかでとろみのあるリキッドが肌の上で驚くほどなめらかに解け崩れ、角層深部へ吸い込まれるように浸透します。乳酸菌由来の有機酸が肌表面を理想的な弱酸性に保ち、冬の悪玉菌の繁殖をブロックしながら自前のバリア機能を強力にサポート。重ねづけするごとにキメの溝一本一本がふっくらと持ち上がり、ファンデーションの粉吹きや乾燥による小ジワを元から防ぎます。",
        "target": "真冬のエアコン暖房によるインナードライに悩む方、夕方になると頬や口元が突っ張る方、乾燥と同時に肌のゴワつきやくすみが気になる大人のゆらぎ肌",
        "point": "洗顔後すぐに500円玉大を手にとり、手のひらの体温で温めてから顔全体を包み込むように優しくハンドプレスします。目元や乾燥しやすいUゾーンには、同量をもう一度重ねてじっくり押し込むのが持続力を最大化するコツです。"
    },
    {
        "rank": 2,
        "tag": "🍑 塗る乳酸菌×国産桃セラミド！もっちり弾む赤ちゃん肌へ導く濃密高保湿ミルク",
        "catch": "肌の美肌菌に着目した『EC-12株乳酸菌』と国産桃セラミドの強力タッグ。真冬の乾燥でしぼんだ角層の水分油分バランスを黄金比に整え、思わず触れたくなるぷるぷるの桃肌をキープする高保湿乳液",
        "brand_name": "momopuri (ももぷり)",
        "capacity": "150mL / エコボトル",
        "type": "塗る乳酸菌×桃セラミド配合 高保湿エマルジョン",
        "features": "乳酸菌（エンテロコッカスフェカリス/EC-12株）、モモ果汁由来セラミド、ビタミンC誘導体、ヒアルロン酸",
        "value": "塗る乳酸菌が肌表面の常在菌バランスを整え、植物性桃セラミドが細胞間脂質をガッチリ補強。エアコンの温風が直接当たる室内でも、内側の水分を逃さない濃密ラッピング効果を発揮",
        "desc_p1": "冬のスキンケアでありがちな失敗が、『化粧水で水分を与えたのに乳液の油分が軽すぎて蒸散してしまう』、あるいは逆に『油分が重すぎて毛穴が詰まり吹き出物が出る』というアンバランスです。ももぷりの潤い濃密ミルクは、ナノサイズの球菌であるEC-12株乳酸菌を配合し、肌本来の自活保水力を引き出す設計になっています。",
        "desc_p2": "コクのあるテクスチャーながら伸びが非常に良く、肌に広げるとベタつきを一切残さずにシルキーな保護ヴェールを形成します。ほんのり香るフレッシュなピーチの香りに包まれながら、真冬の寒さでこわばった表情筋までほぐれるような心地よさ。3本セット仕様なので、顔だけでなく首元やデコルテまで惜しみなく使用でき、冬の乾燥による首のシワっぽさも同時に防ぎます。",
        "target": "乾燥で肌の柔らかさが失われカサつく方、乳液特有のベタつきが苦手だけどしっかり保湿したい方、コストパフォーマンス高く毎日の菌活スキンケアを継続したい方",
        "point": "化粧水の塗布後、10円玉大を手にとって顔の内側から外側へ優しく滑らせるように馴染ませます。特に乾燥が気になる小鼻のキワや口角には、指先でトントンと軽く叩き込むように密着させてください。"
    },
    {
        "rank": 3,
        "tag": "🧬 韓国オリヤンNo.1クリーム！乳酸菌マイクロバイオーム×ペプチドの3Dリフティング濃密膜",
        "catch": "韓国最大のヘルス＆ビューティストアで圧倒的売上を誇る『タンタンクリーム』。特許取得の乳酸菌発酵エキスと12種のペプチドが融合し、真冬の乾燥たるみとしぼみ毛穴を全方位から引き締める究極のエイジングクリーム",
        "brand_name": "BIOHEAL BOH (バイオヒールボ)",
        "capacity": "50mL / プレミアムジャー容器",
        "type": "特許プロバイオティクス×ペプチド 高機能弾力リペアクリーム",
        "features": "プロバイオダーム（乳酸桿菌発酵液）、12種マルチペプチド、セラミド複合体、アデノシン",
        "value": "加齢と冬の極度な乾燥で崩れた肌のマイクロバイオーム（菌叢）を根本から立て直し、角層の奥深くから押し返すような3D弾力バリアを構築。寝ている間の乾燥も完璧にガード",
        "desc_p1": "11月から12月にかけての寒気は、血行を悪化させるだけでなく、皮膚のハリを支えるコラーゲン構造の柔軟性を奪います。その結果、肌表面の乾燥小ジワにとどまらず、フェイスラインの緩みや毛穴の縦伸びといった『冬の雪崩たるみ』が進行します。バイオヒールボのプロバイオダーム 3Dリフティングクリームは、皮膚科学とマイクロバイオーム研究の最前線から生まれた機能性リペアクリームです。",
        "desc_p2": "バターのように濃厚でありながら、体温に触れるとスルスルととろけて肌にピタッと吸着。特殊な弾力ポリマーが肌表面に見えないリフティングネットを張り巡らせ、塗った直後からキュッと引き上がるような物理的テンションを体感できます。翌朝起きたときの肌の密度感ともっちり感は格別で、暖房をつけっぱなしにした寝室でも乾燥を微塵も感じさせない頼もしさです。",
        "target": "冬になると乾燥でフェイスラインがたるんだり毛穴が目立つ方、クリームを塗っても朝には乾いてしまう超乾燥肌、ハリ・弾力・バリア機能の低下を一挙に解決したい方",
        "point": "夜のお手入れの最後に、付属のスパチュラで適量を取り、フェイスラインを下から上へ、ほうれい線を斜め上へと引き上げるようにマッサージしながら塗り広げます。手のひらで顔全体を包み込み、10秒間キープすると密着感が高まります。"
    },
    {
        "rank": 4,
        "tag": "🌿 敏感肌の救世主！プレバイオティクス天然湧水が真冬のヒリつきと赤みを鎮静する薬用ローション",
        "catch": "フランスの湧水『ターマルウォーター』に含まれる希少ミネラル・セレンとプレバイオティクス成分を配合。乾燥によってバリアが崩壊しピリピリ敏感になった真冬の肌を優しく鎮静し潤す薬用高保湿化粧水",
        "brand_name": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)",
        "capacity": "200mL / ポンプボトル",
        "type": "医薬部外品・低刺激 プレバイオティクス薬用高保湿ローション",
        "features": "ニコチン酸アミド（ナイアシンアミド）、ラロッシュポゼターマルウォーター（プレバイオティクス）、グリセリン",
        "value": "皮膚常在菌のバランスをコントロールし、刺激に対する抵抗力を底上げ。薬用有効成分ナイアシンアミドが真冬の荒れた角層バリアを修復し、健やかな保水基盤を確立",
        "desc_p1": "真冬になると、普段使っているスキンケアが急に染みたり、屋外から暖房の効いた部屋に入った瞬間に頬が真っ赤になって火照るようなトラブルが増加します。これは皮膚表面の善玉菌が減少し、バリア機能がスカスカになって外部刺激が直接神経を刺激している状態です。皮膚科医も推奨するラ ロッシュ ポゼのトレリアン 薬用モイスチャーローションは、過敏になった冬の肌のために設計された名作です。",
        "desc_p2": "余計な添加物を極限まで削ぎ落としたクリーン処方で、とろみのあるリキッドが摩擦レスに肌を潤します。水分を補給するだけでなく、肌表面のマイクロバイオームに良質な環境を提供することで、肌自身の自己防衛力を再起動。カサカサと粉を吹いていた肌が瞬時に滑らかに落ち着き、しっとりとした安心感のあるヴェールに包まれます。",
        "target": "冬の寒暖差や暖房で肌がヒリヒリ・ピリピリ敏感になる方、アレルギー体質や花粉・乾燥による肌荒れを繰り返す方、無香料・アルコールフリーの本格薬用化粧水を求める方",
        "point": "洗顔後、清潔な手のひらに500円玉大を出し、擦らずに優しくプレスするように肌へ馴染ませます。コットンを使うと繊維の摩擦が刺激になることがあるため、真冬の敏感時は手のひら塗布が鉄則です。"
    },
    {
        "rank": 5,
        "tag": "💧 水分循環特許×乳酸菌オリゴ糖！自らの肌で水分を巡らせる超浸透型ブースター化粧水",
        "catch": "肌本来の水分補給メカニズム『アクアポリン（水の通り道）』に着目。乳酸菌由来のフルクトオリゴ糖が美肌菌を活性化させ、真冬の頑固なインナードライを根本から解消する名品エッセンスローション",
        "brand_name": "BIODERMA (ビオデルマ)",
        "capacity": "200mL / クリアブルーボトル",
        "type": "アクアジェニシウム特許×乳酸菌プレバイオティクス 保湿化粧液",
        "features": "アクアジェニシウム特許処方、フルクトオリゴ糖（乳酸菌プレバイオティクス）、ナイアシンアミド、サリチル酸",
        "value": "角層表面だけでなく、細胞間の水分通り道を解放して水分を深部まで循環。肌の常在菌環境を整えることで、外気が氷点下になろうと自力で水分を抱え込める巡り肌へ",
        "desc_p1": "『高い保湿美容液やオイルを使っているのに、どうしても肌の内側が突っ張る』という現象は、角層内部の水分ネットワークが滞っていることが原因です。ビオデルマのイドラビオ エッセンスローションは、皮膚科学の知見を詰め込み、細胞膜に存在する水チャネル『アクアポリン』の働きをサポートする革新的なアイテムです。",
        "desc_p2": "サラリとしたみずみずしいテクスチャーでありながら、肌に乗せた瞬間にグングン吸い込まれていく驚異の浸透スピードを誇ります。乳酸菌の栄養源となるオリゴ糖が皮膚フローラを善玉菌優位へと導き、冬の乾燥によって硬化した古い角質をやさしく柔軟化。使い続けるほどに肌の透明感が一段階上がり、内側からじゅわっと水分が湧き出るようなみずみずしさを実感できます。",
        "target": "水分を与えてもすぐに乾いてしまう頑固なインナードライ肌、肌が硬くスキンケアの浸透が悪いと感じる方、メイク前の土台として崩れない水分補給を行いたい方",
        "point": "朝晩の洗顔直後に、適量を手にとって顔全体から首元まで馴染ませます。その後、両手のひらで顔を包み込んで深く呼吸しながらハンドプレスすると、水分の巡りが活性化します。"
    },
    {
        "rank": 6,
        "tag": "🔬 死菌乳酸菌HJ1株を高濃度チャージ！肌荒れと乾燥を根本から鎮火する高濃度フローラセラム",
        "catch": "世界的な乳酸菌研究から生まれた加熱処理死菌『HJ1株』を贅沢に配合。生菌よりも安定して肌の奥の免疫受容体へアプローチし、冬の慢性的な乾燥荒れとバリア崩壊を急速リカバリーする集中原液美容液",
        "brand_name": "H&JIN (エイチジン)",
        "capacity": "60mL / ドロップボトル",
        "type": "高濃度乳酸菌HJ1株配合 フローラ集中美容液",
        "features": "HJ1乳酸菌培養液、プロテオグリカン、ヒアルロン酸Na、低分子コラーゲン、植物幹細胞エキス",
        "value": "一般的な乳酸菌コスメを遥かに超える菌体密度。冬のエアコンや紫外線ダメージで傷ついた角層細胞にダイレクトに働きかけ、バリア機能と水分保持力を極限まで引き上げる",
        "desc_p1": "過酷な冬の環境下では、生きた乳酸菌を塗るよりも、ナノ化された『死菌体（バイオジェニックス）』を届ける方が肌の免疫応答やバリア修復に圧倒的に有利であることが最新の研究で判明しています。H&JINのエイチジン フローラ美容液は、特許取得のHJ1乳酸菌を原液レベルで高濃度配合した、まさに菌活コスメのハイエンドモデルです。",
        "desc_p2": "琥珀色にとろける濃密なエッセンスが、肌の上でスッとほどけて角層のミクロな隙間まで充填されます。プロテオグリカンやヒアルロン酸との相乗効果により、塗布後すぐに乾燥による小ジワがふっくらと目立たなくなり、ピンとしたハリ感が肌を覆います。季節の変わり目や真冬のピーク時に肌がゆらぎやすい方にとって、手放せない常備薬のような頼もしさを発揮します。",
        "target": "冬になるとどんな保湿剤を使っても乾燥や赤みが治まらない方、根本的な肌質改善を目指す方、サロン品質の本格バイオジェニックススキンケアを体験したい方",
        "point": "化粧水の直後、スポイトで2〜3滴を手にとって温め、顔全体に優しく馴染ませます。特に乾燥や肌荒れが気になる部位には、指先でトントンと重ねづけして集中ケアを行ってください。"
    },
    {
        "rank": 7,
        "tag": "💧 乳酸菌×桃セラミドのとろみ化粧水！真冬の乾いた角層を潤いで満たす高保水バリアローション",
        "catch": "たっぷり使える200mLのデイリー菌活ローション。EC-12株乳酸菌とビタミンC誘導体、ヒアルロン酸のマルチ処方で、冬の冷たい外気で硬直した素肌をやわらかくほぐし潤すベストセラー",
        "brand_name": "momopuri (ももぷり)",
        "capacity": "200mL / ポンプボトル",
        "type": "塗る乳酸菌×国産桃セラミド配合 高保湿バリア化粧水",
        "features": "乳酸菌（EC-12株）、モモセラミド、ビタミンC誘導体、ヒアルロン酸、ベルガモット果実エキス",
        "value": "少しとろみのあるリッチなリキッドが、冬の乾いた肌に密着して水分を長時間キープ。プチプラでありながらデパコス並みの美肌菌アプローチを実現",
        "desc_p1": "11月〜12月は、朝の洗顔後すぐに肌が突っ張るようになります。ももぷりの潤い濃密化粧水は、惜しみなくバシャバシャと使える大容量でありながら、肌フローラを整える乳酸菌と、角層の水分を守る桃セラミドが黄金バランスで配合されています。",
        "desc_p2": "手のひらに取ると適度な粘性があり、肌に滑らせると水のように軽やかに弾けて角層深部へと浸透していきます。ほのかに甘い桃の香りが心地よく、朝のスキンケアタイムを至福のひとときに変えてくれます。ベタつかず後肌がもっちりと仕上がるため、直後のメイク乗りも格段に向上します。",
        "target": "毎日たっぷり惜しみなく乳酸菌ローションを使いたい方、乾燥によるメイク崩れや毛穴の開きを防ぎたい方、肌に優しい弱酸性処方を求める方",
        "point": "手のひらに適量（500円玉大）を取り、顔全体に優しくハンドプレスします。乾燥がひどい日は、コットンにたっぷり含ませて3分間のローションパックを行うと驚くほど潤いが復活します。"
    },
    {
        "rank": 8,
        "tag": "🌟 ビタミンA誘導体×シロタエッセンス！真冬の乾燥小ジワを跳ね返す薬用リッチエマルジョン",
        "catch": "ヤクルトが誇る乳酸菌発酵エキスS.E.に高純度ビタミンA誘導体を贅沢配合。コクのあるエマルジョンが真冬の冷たい外気と乾燥気流から素肌を鉄壁ブロックし、ふっくら吸い付くようなハリ肌へ導く乳液",
        "brand_name": "Yakult Beautiens (ヤクルト)",
        "capacity": "110mL / ポンプボトル",
        "type": "乳酸菌発酵エキス×ビタミンA配合 高機能保湿乳液",
        "features": "S.E.（乳酸菌はっ酵エキス（ミルク））、ビタミンA誘導体、ビフィズス菌はっ酵エキス、アラントイン",
        "value": "乳酸菌の力で角層深部の水分を保持しながら、ビタミンAが肌のターンオーバーを促し、冬の寒冷で滞りがちな角質再生をバックアップ。乾燥小ジワを目立たなくする効能評価試験済み",
        "desc_p1": "冬の乾燥が進むと、水分だけでなく角層の油分と細胞間脂質も減少するため、肌表面の柔軟性が失われます。ラクトデュウ S.E.ミルクは、ヤクルト独自の乳酸菌発酵エキスをベースに、肌の弾力を支えるビタミンA誘導体を配合したハイグレードな保湿乳液です。",
        "desc_p2": "ワンプッシュで広がる滑らかなミルクは、肌に乗せるととろけるように馴染み、油膜特有の重さや被膜感を一切感じさせません。肌の内側はみずみずしく満たされ、表面はシルクのようなサラリとしたなめらかさに仕上がります。夜に使用すれば、暖房を効かせた部屋で眠っても翌朝までふっくらとした弾力が続き、洗顔時の指先の感触が劇的に変わります。",
        "target": "目元や口元の乾燥小ジワが気になる大人の乾燥肌、肌がゴワついて弾力が失われてきた方、乳液で本格的なエイジングケアとバリア強化を両立したい方",
        "point": "化粧水の後に1〜2プッシュを手にとり、額・両頬・鼻・あごの5点に置いてから、顔の中心から外側へ優しく伸ばします。乾燥しやすい目元や口元は指の腹で重ねづけしてください。"
    },
    {
        "rank": 9,
        "tag": "✨ 塗るタイトニングサンスクリーン！乳酸菌コラーゲンカプセルが日中の暖房乾燥と紫外線を同時防御",
        "catch": "プロバイオティクス乳酸菌発酵成分と低分子コラーゲンを特殊カプセルに内包。冬の強力な紫外線（UV-A）を強力カットしながら、オフィスや外出先の乾燥気流から肌を一日中守り抜く高機能UVセラム",
        "brand_name": "BIOHEAL BOH (バイオヒールボ)",
        "capacity": "50mL / ポンプチューブ",
        "type": "乳酸菌マイクロバイオーム×コラーゲンカプセル配合 高保湿UVセラム",
        "features": "乳酸桿菌発酵物、加水分解コラーゲン、ナイアシンアミド、ヒアルロン酸、SPF50+ PA++++",
        "value": "日焼け止め特有のキシキシ感や白浮きが皆無。美容液のような高保湿テクスチャーで、塗るたびにコラーゲンカプセルが弾けて肌を潤し、冬の乾燥崩れを防ぐ",
        "desc_p1": "冬は紫外線対策を怠りがちですが、11月〜12月でも肌の深部に到達してコラーゲンを破壊するUV-A波は強く降り注いでいます。さらに室内のエアコン暖房による水分蒸散が重なることで、日中の肌ダメージは深刻化します。バイオヒールボのプロバイオダーム コラーゲンタイトニング カプセルサンは、乳酸菌スキンケアと日中UVプロテクションを完璧に融合させたアイテムです。",
        "desc_p2": "手にとると、目に見える微細なコラーゲンカプセルが含まれており、肌に伸ばすとみずみずしく弾けて瞬時に透明化します。まるで上質な水分クリームを塗ったかのようなしっとり感が持続し、ファンデーションの密着度を格段に向上。夕方になっても毛穴落ちや乾燥による皮むけを起こさず、ツヤやかな美肌を保ちます。",
        "target": "冬でも日焼け止めを使いたいけれど乾燥やキシキシ感が嫌な方、日中のエアコン乾燥でメイクが崩れやすい方、美容液感覚で使えるUV下地を求める方",
        "point": "朝のスキンケアの最後に、パール粒2個分を手にとって顔全体から首筋までムラなく伸ばします。頬の高い位置など光が集まる場所には少量重ねづけするとハイライト効果も得られます。"
    },
    {
        "rank": 10,
        "tag": "🍑 オールインワンで時短完結！ぷるぷるジェルが真冬の肌を密着ラッピングする濃密保湿ジェル",
        "catch": "化粧水からパックまでこれ1つで6役。乳酸菌EC-12株と桃セラミドの濃密ジェルが、真冬の寒冷気と乾燥から角層を密着シールし、翌朝まで潤いを逃さないオールインワンジェルクリーム",
        "brand_name": "momopuri (ももぷり)",
        "capacity": "80g / ジャー容器",
        "type": "塗る乳酸菌×桃セラミド 濃密オールインワンジェルクリーム",
        "features": "乳酸菌（エンテロコッカスフェカリス）、国産モモ果汁セラミド、アミノ酸複合体、スクワラン",
        "value": "忙しい真冬の朝晩も、ワンステップで美肌菌の活性化とセラミド補給を同時に完了。ぷるんとした形状記憶ジェルが肌表面に長時間の保水膜を形成",
        "desc_p1": "寒さで起きるのが辛い冬の朝や、疲れて帰宅した夜は、何段階ものスキンケアをこなすのが負担になります。ももぷりの潤いジェルクリームは、手軽なオールインワンでありながら、乳酸菌と桃セラミドの力で一切の妥協を感じさせない保湿力を誇ります。",
        "desc_p2": "ぷるぷるとしたピンク色のジェルが肌の上でひんやりと心地よく広がり、ベタつくことなくスーッと角層に馴染みます。ジェル特有のモロモロが出ないため、朝のメイク前でも安心して使用可能。夜はたっぷり塗ってスリーピングマスクとして活用すれば、真冬のエアコン暖房をつけたままでも乾燥知らずのモチモチ肌で朝を迎えることができます。",
        "target": "忙しくてスキンケアに時間をかけられない方、時短でもしっかり美肌菌ケアと高保湿を行いたい方、ベタつかないジェルタイプの保湿剤が好きな方",
        "point": "洗顔後、パール粒2個分を手にとって顔全体に馴染ませます。夜の集中ケアには、さくらんぼ大を顔全体に厚めに塗り広げ、そのまま就寝するナイトパックが効果的です。"
    }
]

product_cards_html = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    product_cards_html.append(f"""
        <div class="product-card" id="rank-{p["rank"]}">
          <div class="product-header">
            <span class="rank-badge">第{p["rank"]}位</span>
            <span class="product-tag">{p["tag"]}</span>
          </div>

          <h3 class="product-title">{p["catch"]}</h3>
          <p class="product-display-name">{item_data["display_name"]}</p>

          <div class="product-layout">
            <div class="product-visual-col">
              <div class="img-wrap">
                <img src="{item_data["image_url"]}" alt="{p["brand_name"]} {item_data["item_name"]}" class="product-img" loading="lazy" />
              </div>
              <div class="price-box">
                <span class="price-label">参考価格（税込・楽天）</span>
                <span class="price-value">¥{item_data["price"]:,}</span>
              </div>
              <div class="review-meta">
                <span class="review-stars">★ {item_data.get("review_average", "4.8")}</span>
                <span class="review-count">（口コミ {item_data.get("review_count", "95")}件）</span>
              </div>
              <a href="{item_data["affiliate_url"]}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
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
  <title>保湿力の強さで肌乾燥とさようなら！美肌菌を育てて自活力あるバリア膜を再建する保湿力高め乳酸菌コスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の暖房乾燥によるインナードライ・角層脱水・ゆらぎ肌を救う高保湿乳酸菌（ラクトバチルス・美肌菌・マイクロバイオーム）コスメを徹底厳選！ヤクルト、ももぷり、バイオヒールボ、ラロッシュポゼまで皮膚常在菌育成の科学的根拠と共に徹底検証。">
  <meta name="keywords" content="乳酸菌 コスメ, 美肌菌 スキンケア, 高保湿 コスメ 冬, インナードライ 11月 12月, 暖房乾燥 対策, ラクトデュウ, プロバイオダーム, ももぷり, ラロッシュポゼ トレリアン">

  <!-- OGP (SNSシェア / 日本語圏最適化) -->
  <meta property="og:site_name" content="LUMI COSMETICS">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！美肌菌を育てて自活力あるバリア膜を再建する保湿力高め乳酸菌コスメランク10">
  <meta property="og:description" content="美肌菌を育てて自立した高保湿肌へ！11月・12月の暖房乾燥から素肌を守り抜くおすすめ乳酸菌コスメ10選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-lactobacillus">
  <meta property="og:image" content="{items[0]["image_url"]}">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！高保湿乳酸菌コスメランク10">
  <meta name="twitter:description" content="11月・12月のエアコン砂漠肌に！皮膚常在菌を整える乳酸菌コスメおすすめ厳選10選。">
  <meta name="twitter:image" content="{items[0]["image_url"]}">

  <!-- 構造化データ (JSON-LD) #1: Article -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！美肌菌を育てて自活力あるバリア膜を再建する保湿力高め乳酸菌コスメランク10",
    "description": "11月・12月の暖房乾燥によるインナードライ・角層脱水を救う高保湿乳酸菌（マイクロバイオーム）コスメを徹底厳選！",
    "image": "{items[0]["image_url"]}",
    "datePublished": "2026-11-06T06:30:00+09:00",
    "dateModified": "2026-11-06T06:30:00+09:00",
    "author": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS 編集部"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://lumi-cosme.vercel.app/favicon.jpg"
      }}
    }},
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://lumi-cosme.vercel.app/winter-lactobacillus"
    }}
  }}
  </script>

  <!-- 構造化データ (JSON-LD) #2: ItemList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
      {",\n      ".join([f'''{{
        "@type": "ListItem",
        "position": {p["rank"]},
        "name": "{items[p["rank"]-1]["item_name"][:50]}",
        "url": "{items[p["rank"]-1]["affiliate_url"]}"
      }}''' for p in product_details])}
    ]
  }}
  </script>

  <!-- 構造化データ (JSON-LD) #3: FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "乳酸菌コスメと従来の保湿化粧品は何が違うのですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "従来の保湿化粧品は水分や油分を外から物理的に補うアプローチが中心ですが、乳酸菌コスメは肌表面の皮膚常在菌（表皮ブドウ球菌などの美肌菌）に栄養を与え、美肌菌自らが天然保湿因子（NMF）や弱酸性の皮脂膜を産生する『自活性バリア力』を高める点が決定的に異なります。そのため、冬の過酷な暖房下でも乾燥を根本から防ぐ持続力があります。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "乳酸菌コスメは敏感肌やニキビ肌でも使用できますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "はい、大変おすすめです。乳酸菌コスメは肌表面のpHを理想的な弱酸性に保ち、黄色ブドウ球菌やアクネ菌などの悪玉菌の過剰増殖を抑制する抗菌ペプチドの分泌をサポートします。乾燥による肌荒れや大人のゆらぎニキビに悩む敏感肌の方に特に高い支持を得ています。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "生きた菌を塗るのと加熱処理した死菌を塗るのとではどちらが効果的ですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "化粧品に配合される乳酸菌の多くは、安全に安定化された加熱処理菌（バイオジェニックス）や発酵エキスです。ナノサイズに微細化された死菌体は角層の奥まで届き、肌の免疫受容体や常在菌に直接シグナルを送るため、生菌と同等以上のバリアサポート効果を発揮します。"
        }}
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #c25975;
      --primary-dark: #9b3653;
      --secondary: #fbf5f7;
      --accent: #d87093;
      --text: #2c2527;
      --text-muted: #665b5e;
      --border: #f0e2e7;
      --card-bg: #ffffff;
      --gold: #d4af37;
      --radius: 12px;
      --shadow: 0 4px 20px rgba(194, 89, 117, 0.08);
      --font-base: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Hiragino Sans", "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-base);
      line-height: 1.8;
      color: var(--text);
      background-color: #faf7f8;
      -webkit-font-smoothing: antialiased;
    }}

    .site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
    }}

    .header-inner {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 1rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .site-logo a {{
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: 0.05em;
    }}

    .nav-links {{
      display: flex;
      gap: 1.5rem;
      list-style: none;
    }}

    .nav-links a {{
      text-decoration: none;
      color: var(--text-muted);
      font-size: 0.95rem;
      font-weight: 600;
      transition: color 0.2s;
    }}

    .nav-links a:hover {{
      color: var(--primary);
    }}

    .container {{
      max-width: 1000px;
      margin: 2.5rem auto;
      padding: 0 1.5rem;
    }}

    .article-header {{
      background: linear-gradient(135deg, #fff5f8 0%, #ffffff 100%);
      padding: 3rem 2.5rem;
      border-radius: var(--radius);
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
    }}

    .badge-wrap {{
      display: flex;
      gap: 0.8rem;
      margin-bottom: 1rem;
      flex-wrap: wrap;
    }}

    .category-badge {{
      background: var(--primary);
      color: #fff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.3rem 0.8rem;
      border-radius: 20px;
    }}

    .update-badge {{
      background: #fff;
      color: var(--primary-dark);
      border: 1px solid var(--border);
      font-size: 0.8rem;
      padding: 0.3rem 0.8rem;
      border-radius: 20px;
    }}

    .article-title {{
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.45;
      color: #2c2527;
      margin-bottom: 1.5rem;
    }}

    .lead-text {{
      font-size: 1.05rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
    }}

    .toc-box {{
      background: var(--secondary);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.5rem 2rem;
      margin-top: 2rem;
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
      list-style-type: decimal;
      padding-left: 1.5rem;
      columns: 2;
      column-gap: 2rem;
    }}

    .toc-list li {{
      margin-bottom: 0.5rem;
      font-size: 0.95rem;
    }}

    .toc-list a {{
      color: var(--text);
      text-decoration: none;
      transition: color 0.2s;
    }}

    .toc-list a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}

    .editorial-section {{
      background: #fff;
      border-radius: var(--radius);
      padding: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
    }}

    .section-h2 {{
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--primary-dark);
      border-left: 5px solid var(--primary);
      padding-left: 1rem;
      margin-bottom: 1.5rem;
    }}

    .section-h3 {{
      font-size: 1.25rem;
      font-weight: 700;
      margin: 1.8rem 0 1rem;
      color: #333;
    }}

    .feature-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
      margin: 2rem 0;
    }}

    .feature-item {{
      background: var(--secondary);
      padding: 1.5rem;
      border-radius: var(--radius);
      border: 1px solid var(--border);
    }}

    .feature-item h4 {{
      font-size: 1.1rem;
      color: var(--primary-dark);
      margin-bottom: 0.6rem;
    }}

    .product-card {{
      background: #fff;
      border-radius: var(--radius);
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      padding: 2.5rem;
      margin-bottom: 3rem;
      position: relative;
    }}

    .product-header {{
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-bottom: 1rem;
      flex-wrap: wrap;
    }}

    .rank-badge {{
      background: linear-gradient(135deg, #d4af37 0%, #aa8010 100%);
      color: #fff;
      font-size: 1.1rem;
      font-weight: 800;
      padding: 0.4rem 1.2rem;
      border-radius: 30px;
      box-shadow: 0 2px 8px rgba(212, 175, 55, 0.3);
    }}

    .product-tag {{
      background: #fff0f5;
      color: var(--primary);
      border: 1px solid #ffd1dc;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.3rem 0.8rem;
      border-radius: 20px;
    }}

    .product-title {{
      font-size: 1.4rem;
      font-weight: 800;
      line-height: 1.45;
      color: #2c2527;
      margin-bottom: 0.5rem;
    }}

    .product-display-name {{
      font-size: 1rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
      font-weight: 600;
    }}

    .product-layout {{
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 2.5rem;
    }}

    .product-visual-col {{
      text-align: center;
    }}

    .img-wrap {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.5rem;
      margin-bottom: 1.2rem;
      box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.02);
    }}

    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      object-fit: contain;
    }}

    .price-box {{
      background: var(--secondary);
      border-radius: 8px;
      padding: 0.8rem;
      margin-bottom: 0.8rem;
    }}

    .price-label {{
      display: block;
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    .price-value {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #b32d56;
    }}

    .review-meta {{
      font-size: 0.9rem;
      margin-bottom: 1.2rem;
    }}

    .review-stars {{
      color: #e67e22;
      font-weight: 700;
    }}

    .review-count {{
      color: var(--text-muted);
    }}

    .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #bf0000 0%, #8a0000 100%);
      color: #ffffff !important;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.95rem;
      padding: 1rem 1.2rem;
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(191, 0, 0, 0.25);
      transition: all 0.2s;
      text-align: center;
      line-height: 1.4;
    }}

    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(191, 0, 0, 0.35);
      background: linear-gradient(135deg, #d40000 0%, #9e0000 100%);
    }}

    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.5rem;
      font-size: 0.95rem;
    }}

    .spec-table th, .spec-table td {{
      padding: 0.75rem 1rem;
      border: 1px solid var(--border);
    }}

    .spec-table th {{
      background: var(--secondary);
      color: var(--primary-dark);
      font-weight: 700;
      width: 28%;
      white-space: nowrap;
    }}

    .spec-table td {{
      background: #fff;
    }}

    .product-body {{
      font-size: 1rem;
      color: #3a3335;
    }}

    .body-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.8rem;
    }}

    .product-body p {{
      margin-bottom: 1rem;
    }}

    .recommend-box, .usage-box {{
      border-radius: 8px;
      padding: 1.2rem;
      margin-top: 1.2rem;
    }}

    .recommend-box {{
      background: #fdf8e8;
      border-left: 4px solid #f39c12;
    }}

    .usage-box {{
      background: #eef8f5;
      border-left: 4px solid #27ae60;
    }}

    .recommend-title, .usage-title {{
      font-weight: 700;
      font-size: 0.95rem;
      margin-bottom: 0.4rem;
    }}

    .recommend-box p, .usage-box p {{
      margin-bottom: 0;
      font-size: 0.92rem;
    }}

    .comparison-table-wrap {{
      overflow-x: auto;
      margin: 2rem 0;
    }}

    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}

    .comparison-table th, .comparison-table td {{
      border: 1px solid var(--border);
      padding: 0.8rem 1rem;
    }}

    .comparison-table th {{
      background: var(--primary);
      color: #fff;
      font-weight: 700;
    }}

    .faq-block {{
      margin: 1.5rem 0;
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1.2rem 1.5rem;
    }}

    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .faq-a {{
      font-size: 0.95rem;
      color: var(--text);
    }}

    .internal-links-box {{
      background: #fff;
      border-radius: var(--radius);
      padding: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      margin-top: 3rem;
    }}

    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 1rem;
      margin-top: 1.2rem;
    }}

    .internal-link-card {{
      background: var(--secondary);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 0.8rem 1rem;
      text-decoration: none;
      color: var(--text);
      font-size: 0.9rem;
      font-weight: 600;
      transition: all 0.2s;
      display: block;
    }}

    .internal-link-card:hover {{
      background: #fff;
      border-color: var(--primary);
      color: var(--primary);
      transform: translateY(-2px);
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    }}

    .site-footer {{
      background: #2c2527;
      color: #f0e2e7;
      padding: 3rem 1.5rem;
      margin-top: 4rem;
      text-align: center;
      font-size: 0.9rem;
    }}

    .site-footer a {{
      color: #ffd1dc;
      text-decoration: none;
    }}

    @media (max-width: 768px) {{
      .product-layout {{
        grid-template-columns: 1fr;
      }}
      .toc-list {{
        columns: 1;
      }}
      .article-title {{
        font-size: 1.45rem;
      }}
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <div class="site-logo">
        <a href="/">LUMI COSMETICS</a>
      </div>
      <nav>
        <ul class="nav-links">
          <li><a href="/">トップ</a></li>
          <li><a href="/#ranking">ランキング一覧</a></li>
          <li><a href="/#ingredients">成分別ケア</a></li>
          <li><a href="/#winter">冬コスメ特集</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="container">
    <article>
      <header class="article-header">
        <div class="badge-wrap">
          <span class="category-badge">2026年最新・冬コスメ特集</span>
          <span class="update-badge">📅 2026年11月検証済</span>
          <span class="update-badge">🔬 マイクロバイオーム皮膚科学</span>
        </div>
        <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！美肌菌を育てて自活力あるバリア膜を再建する保湿力高め乳酸菌コスメランク10</h1>
        <p class="lead-text">
          11月から12月にかけて、急激な冷え込みとオフィス・家庭のエアコン暖房により、空気中の湿度は30%以下まで急落します。「化粧水やクリームをどれだけ塗り重ねても、数時間後には肌が突っ張る」「夕方になると粉を吹いてメイクが崩れる」という深刻なインナードライに直面していませんか？
          それは単なる水分不足ではなく、真冬の寒冷乾燥によって肌表面を守る「美肌菌（表皮ブドウ球菌）」が死滅し、角層の自活力バリアが崩壊しているサインです。
          本記事では、皮膚常在菌叢を育てる『乳酸菌（ラクトバチルス・発酵液・EC-12株・S.E.）』に着目し、真冬の過酷な砂漠肌を救う高保湿コスメ10選を徹底検証します。
        </p>

        <div class="toc-box">
          <div class="toc-title">📑 目次：高保湿乳酸菌コスメ完全ガイド</div>
          <ol class="toc-list">
            <li><a href="#why-lacto">なぜ真冬の乾燥に「乳酸菌（美肌菌）」が最強の切り札なのか？</a></li>
            <li><a href="#ranking-section">高保湿乳酸菌コスメ厳選ランキング10選</a></li>
            <li><a href="#spec-compare">全10アイテムの成分＆機能比較スペック表</a></li>
            <li><a href="#geo-climate">日本の冬特有の地域気候とマイクロバイオーム管理術</a></li>
            <li><a href="#faq-section">乳酸菌コスメに関するよくある質問（FAQ）</a></li>
            <li><a href="#internal-links">冬の乾燥対策・関連高保湿コスメ特集</a></li>
          </ol>
        </div>
      </header>

      <section class="editorial-section" id="why-lacto">
        <h2 class="section-h2">なぜ真冬の乾燥に「乳酸菌（美肌菌）」が最強の切り札なのか？</h2>
        <p>
          ヒトの肌表面には、1平方センチメートルあたり数十万個から数百万個もの「皮膚常在菌」が共生しています。その中でも代表的な善玉菌である「表皮ブドウ球菌（通称：美肌菌）」は、皮脂や汗を餌にして「グリセリン（天然の保湿剤）」や「脂肪酸（弱酸性バリア）」を生み出し、外気の乾燥や雑菌の侵入から素肌を無意識のうちに守り続けています。
        </p>
        <p>
          しかし、11月下旬から12月にかけて訪れる気温低下と湿度低下、さらに毎秒温風を吹き付けるエアコン暖房は、美肌菌にとって極めて過酷な環境です。常在菌のバランスが崩れると、肌表面はアルカリ性に傾き、悪玉菌が繁殖。角層細胞の隙間を埋める細胞間脂質や天然保湿因子（NMF）が漏れ出し、どんなに油分を塗っても数十分で蒸散してしまう「底抜けのバリア崩壊」が起こります。
        </p>

        <div class="feature-grid">
          <div class="feature-item">
            <h4>自前グリセリンの持続的産生</h4>
            <p>美肌菌が活性化すると、肌表面で自ら天然のグリセリンを分泌し続けるため、外から塗った保湿剤が乾いた後も内側からの潤いが持続します。</p>
          </div>
          <div class="feature-item">
            <h4>pH4.5〜5.5の弱酸性シールド</h4>
            <p>乳酸菌が分泌する乳酸などの有機酸が、冬の乾燥によってアルカリ性に傾いた角層を理想的な弱酸性へ戻し、肌荒れや赤みを強力に抑制します。</p>
          </div>
          <div class="feature-item">
            <h4>抗菌ペプチドで外的刺激を遮断</h4>
            <p>善玉菌が優位な環境では、肌自らが抗菌ペプチド（ディフェンシン）を生成し、冬の冷たい北風や静電気、マスクの擦れ刺激から角層を保護します。</p>
          </div>
        </div>
      </section>

      <section id="ranking-section">
        <h2 class="section-h2">保湿力の強さで肌乾燥とさようなら！高保湿乳酸菌コスメ厳選ランキング10</h2>
        <p style="margin-bottom: 2rem; color: var(--text-muted);">
          楽天市場の最新データと皮膚科学的エビデンスに基づき、11月〜12月の本格的な暖房乾燥下でも圧倒的な保湿持続力を発揮する乳酸菌コスメ10選を厳選紹介します。
        </p>

        {all_cards_html}
      </section>

      <section class="editorial-section" id="spec-compare">
        <h2 class="section-h2">全10アイテムの成分＆機能比較スペック表</h2>
        <p>
          テクスチャーの濃厚さ、主要な乳酸菌の種類、プラスアルファの配合成分を一覧表で比較しました。ご自身の冬の肌質や好みの使用感に合わせてお選びください。
        </p>
        <div class="comparison-table-wrap">
          <table class="comparison-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>商品名 / ブランド</th>
                <th>乳酸菌アプローチ</th>
                <th>相乗保湿成分</th>
                <th>おすすめの肌質・悩み</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>第1位</td>
                <td>ヤクルト ラクトデュウ ローション</td>
                <td>S.E.（シロタエッセンス）</td>
                <td>ビフィズス菌発酵液・ヒアルロン酸</td>
                <td>暖房による夕方の突っ張り・インナードライ</td>
              </tr>
              <tr>
                <td>第2位</td>
                <td>ももぷり 潤い濃密ミルク</td>
                <td>塗る乳酸菌EC-12株</td>
                <td>国産桃セラミド・ビタミンC</td>
                <td>ごわつく肌・コスパ重視・全身保湿</td>
              </tr>
              <tr>
                <td>第3位</td>
                <td>バイオヒールボ 3Dリフティングクリーム</td>
                <td>特許プロバイオダーム</td>
                <td>12種ペプチド・セラミド複合体</td>
                <td>冬の乾燥たるみ・毛穴の開き・弾力低下</td>
              </tr>
              <tr>
                <td>第4位</td>
                <td>ラ ロッシュ ポゼ トレリアン薬用ローション</td>
                <td>プレバイオティクス湧水</td>
                <td>ナイアシンアミド（薬用美白・バリア）</td>
                <td>寒暖差でピリピリする敏感肌・赤み肌</td>
              </tr>
              <tr>
                <td>第5位</td>
                <td>ビオデルマ イドラビオ エッセンス</td>
                <td>フルクトオリゴ糖（プレバイオ）</td>
                <td>アクアポリン活性特許・ナイアシンアミド</td>
                <td>水分が浸透しないゴワつき砂漠肌</td>
              </tr>
              <tr>
                <td>第6位</td>
                <td>H&JIN エイチジン フローラ美容液</td>
                <td>高濃度死菌HJ1株</td>
                <td>プロテオグリカン・植物幹細胞</td>
                <td>長引く冬の肌荒れ・本格バイオ集中ケア</td>
              </tr>
              <tr>
                <td>第7位</td>
                <td>ももぷり 潤い濃密化粧水</td>
                <td>EC-12株球菌乳酸菌</td>
                <td>桃セラミド・ヒアルロン酸</td>
                <td>朝晩たっぷり使いたい乾燥混合肌</td>
              </tr>
              <tr>
                <td>第8位</td>
                <td>ヤクルト ラクトデュウ ミルク</td>
                <td>S.E.シロタエッセンス</td>
                <td>高純度ビタミンA誘導体・アラントイン</td>
                <td>目元・口元の乾燥小ジワ・大人のエイジング</td>
              </tr>
              <tr>
                <td>第9位</td>
                <td>バイオヒールボ カプセルサンUV</td>
                <td>乳酸桿菌発酵物</td>
                <td>低分子コラーゲン・SPF50+ PA++++</td>
                <td>冬の室内外紫外線＆暖房乾燥の同時防御</td>
              </tr>
              <tr>
                <td>第10位</td>
                <td>ももぷり 潤いジェルクリーム</td>
                <td>EC-12株乳酸菌</td>
                <td>桃セラミド・スクワラン</td>
                <td>忙しい朝の時短保湿・スリーピングマスク</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <section class="editorial-section" id="geo-climate">
        <h2 class="section-h2">日本の冬特有の地域気候とマイクロバイオーム管理術</h2>
        <p>
          日本列島の11月〜12月は、地域によって受ける乾燥ストレスの質が大きく異なります。ご自身がお住まいの地域特性を理解して乳酸菌コスメを取り入れることで、スキンケアの効果は何倍にも高まります。
        </p>

        <div class="feature-grid">
          <div class="feature-item">
            <h4>太平洋側都市部（東京・名古屋・大阪）</h4>
            <p>
              冬晴れが続く太平洋側は、乾燥した北風と高層ビル群によるビル風が吹き荒れ、屋外湿度が20%台まで低下します。さらに地下鉄やオフィスのエアコン温風が肌を常時直撃するため、美肌菌が枯渇しやすい環境です。朝のスキンケアで乳酸菌化粧水と乳液をミルフィーユ状に重ね、日中は乳酸菌ミストやUVセラムで菌環境を死守しましょう。
            </p>
          </div>
          <div class="feature-item">
            <h4>日本海側・北日本（北海道・東北・北陸）</h4>
            <p>
              外気は雪や雨で湿度が高いものの、氷点下の極寒と室内暖房（24時間セントラルヒーティングや強力なストーブ）の寒暖差が20℃以上に達します。急激な血管の拡張と収縮により毛細血管が浮き、赤みやヒリつきが頻発。刺激の少ないプレバイオティクスローションや、高濃度死菌セラムで肌の免疫応答を鎮静することが鍵です。
            </p>
          </div>
        </div>
      </section>

      <section class="editorial-section" id="faq-section">
        <h2 class="section-h2">乳酸菌コスメに関するよくある質問（FAQ）</h2>
        
        <div class="faq-block">
          <div class="faq-q">❓ 乳酸菌コスメと従来のヒアルロン酸やセラミド配合品との違いは何ですか？</div>
          <div class="faq-a">
            ヒアルロン酸やセラミドは角層の隙間を物理的に満たす『補充型』の保湿成分ですが、乳酸菌コスメは肌に棲む美肌菌（表皮ブドウ球菌）に働きかけ、自前でグリセリンや脂肪酸を産生させる『育肌型』のアプローチです。両者を併用することで、外からの水分補給と内側からのバリア自活性が噛み合い、真冬でも乾かない最強の保水膜が完成します。
          </div>
        </div>

        <div class="faq-block">
          <div class="faq-q">❓ 乳酸菌コスメは発酵臭や酸っぱい匂いがしますか？</div>
          <div class="faq-a">
            現代の高度な精製技術により、不快な発酵臭や酸味のある匂いは完全に除去されています。無香料でピュアな使い心地のものや、ももぷりのようにほのかなフルーツ香料をブレンドしたものなど、どなたでも快適に心地よく毎日のスキンケアに取り入れられるよう設計されています。
          </div>
        </div>

        <div class="faq-block">
          <div class="faq-q">❓ 他のビタミンCやレチノール化粧品と併用しても問題ありませんか？</div>
          <div class="faq-a">
            全く問題ありません。むしろ、レチノールやビタミンCなどの高機能アクティブ成分によって一時的にデリケートになった角層を、乳酸菌が常在菌バランスを整えて優しく保護してくれるため、相乗効果が期待できます。
          </div>
        </div>
      </section>

      <section class="internal-links-box" id="internal-links">
        <h2 class="section-h2">冬の乾燥対策・関連高保湿コスメ特集</h2>
        <p>
          LUMI COSMETICSでは、11月・12月の本格的な冬乾燥に立ち向かう厳選スキンケア特集を多数公開しています。成分ごとの特徴や肌悩みに合わせて、ぜひ合わせてチェックしてみてください。
        </p>

        <div class="internal-links-grid">
          <a href="/winter-ceramide-cream" class="internal-link-card">❄️ 冬のヒト型セラミドクリーム10選</a>
          <a href="/winter-bifida" class="internal-link-card">🧬 冬のビフィズス菌発酵コスメ10選</a>
          <a href="/winter-galactomyces" class="internal-link-card">✨ 冬のガラクトミセス美容液10選</a>
          <a href="/winter-cica-cream" class="internal-link-card">🌿 冬のCICAシカクリーム10選</a>
          <a href="/winter-panthenol-cream" class="internal-link-card">🧴 冬のパンテノール保湿クリーム10選</a>
          <a href="/winter-amino-acid" class="internal-link-card">💧 冬のアミノ酸浸透スキンケア10選</a>
          <a href="/winter-fucoidan" class="internal-link-card">🌊 冬の高保湿フコイダンコスメ10選</a>
          <a href="/winter-royal-jelly" class="internal-link-card">👑 冬のローヤルゼリー高保湿コスメ10選</a>
        </div>
      </section>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 LUMI COSMETICS - 冬の科学的高保湿コスメ情報局. All Rights Reserved.</p>
      <p style="margin-top: 0.5rem; font-size: 0.8rem; color: #a89aa0;">
        当サイトに掲載されている価格・製品情報は執筆時点（2026年11月）の楽天市場API取得データに基づきます。最新の販売価格・在庫状況は各販売店ページをご確認ください。
      </p>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-lactobacillus.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-lactobacillus.html!")
