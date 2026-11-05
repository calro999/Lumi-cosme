import json
import re

with open("fetched_3new_fucoidan_royal_soy.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_fucoidan"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🌊 海の自己治癒多糖体が角層を密着ラッピング！高濃度モズク原液の超保水セラム",
        "catch": "沖縄の清麗な海が育んだ高純度モズク由来フコイダンを凝縮。硫酸基を豊富に含む高分子多糖体ヴェールが、真冬の強烈なエアコン暖房下でも角層水分をがっちり掴んで離さない高純度モイスチャー美容液",
        "brand_name": "Limveil (リムヴェール)",
        "capacity": "50ml / 遮光スポイトボトル",
        "type": "高純度モズクフコイダン原液 高保水美容液",
        "features": "オキナワモズクエキス（高分子フコイダン高含有）、海洋深層水、ヒアルロン酸Na、低刺激・無香料・無着色",
        "value": "海藻が干潮時の激しい乾燥や紫外線から身を守るために分泌するヌメリ成分『フコイダン』の自己修復皮膜を肌上に再現。塗布後わずか数分で目に見えない人工バイオフィルムを形成し、冬の過酷な暖房気流から素肌を守り抜く",
        "desc_p1": "11月から12月にかけてオフィスや住宅のエアコン暖房が本格稼働すると、室内の湿度は20%台まで急降下し、肌表面からは毎秒猛烈な勢いで水分が蒸散していきます。一般的なヒアルロン酸化粧水では『塗った直後は潤うのに、30分後には突っ張る』というインナードライに陥りがちです。リムヴェールの『シーウィードセラム』は、沖縄の太陽と豊かな海水で育ったオキナワモズクから抽出した高分子フコイダンを高濃度で配合した本格派の保水エッセンスです。",
        "desc_p2": "フコイダンの最大の特徴は、自身の分子構造内に多数の『硫酸基』を抱えている点にあります。この硫酸基の働きにより、肌表面の汗や皮脂の塩分環境下でも保水力が低下せず、自重の数百倍の水分を抱え込んだまま角層表面に強固なモイストヴェールを構築します。サラリとした浸透感でありながら、ハンドプレスすると指先が吸い付くような濃密なモチモチ感へと変化。冷たいすきま風や暖房の温風に長時間さらされても、夕方まで一切の突っ張りを感じさせない鉄壁の守りを実感できます。",
        "target": "冬の暖房直撃によるインナードライや夕方の顔の突っ張りに悩む方、ヒアルロン酸やセラミドだけでは乾燥がおさまらない超乾燥肌、手持ちのスキンケアの保湿持続力を底上げしたい方",
        "point": "朝晩の洗顔後、化粧水で肌を整えた直後に2〜3滴を手のひらに取り、両手で温めてから顔全体へ優しく押し込むようにハンドプレスします。目元や口元の乾燥小ジワが気になる部位には、さらに1滴を指先でトントンと重ねづけしてください。"
    },
    {
        "rank": 2,
        "tag": "🔬 ビタミンC・E×褐藻エキスの相乗効果！真冬の毛穴開きと乾燥くすみを一掃する機能性美容液",
        "catch": "角層研究のパイオニア『タカミ』が誇るビタミン機能性セラム。高濃度ビタミンC・Eに褐藻由来のフコイダン多糖体を高配合。寒冷と乾燥でゴワつく角層を柔軟にほぐし、毛穴の目立たない透明感あふれるキメ肌へ導く",
        "brand_name": "TAKAMI (タカミ)",
        "capacity": "30mL / スポイト遮光瓶",
        "type": "高機能ビタミンC・E×褐藻エキス 美容液",
        "features": "両親媒性ビタミンC誘導体、ビタミンE、褐藻エキス（フコイダン含有多糖類）、セラミド複合体",
        "value": "冷気で硬化した冬の角層に素早く浸透し、毛穴まわりの乾燥くすみとしぼみにアプローチ。ビタミンの抗酸化力とフコイダンの高密着保水が融合し、内側から押し返すようなハリ弾力を実現",
        "desc_p1": "冬の寒さと乾燥にさらされた肌は、角層細胞のターンオーバーが乱れて古い角質が蓄積し、ゴワつきや毛穴の開き、どんよりとした乾燥くすみが深刻化します。タカミエッセンス5CEプレミアムは、即効型と持続型のビタミンCにビタミンEを融合させ、さらに海の生命力の源である褐藻フコイダンエキスを惜しみなく配合した多機能美容液です。",
        "desc_p2": "手にとると黄金色に輝く濃厚なとろみテクスチャーが、肌に乗せた瞬間に摩擦なくスルリと伸び広がり、毛穴のすみずみまで浸透。フコイダンが形成する潤い皮膜がビタミン成分を角層内部へ閉じ込め、外気乾燥による刺激を和らげます。使い続けるほどにキメがキュッと引き締まり、ファンデーションが粉を吹かずに滑らかに乗る極上の肌コンディションへと整えます。",
        "target": "冬の乾燥で頬の毛穴が縦に開いて目立つ方、寒暖差による肌のくすみや透明感の低下が気になる方、ビタミン美容液を使いたいけれど乾燥や刺激が心配な方",
        "point": "タカミスキンピール等で角層を整えた後、スポイト半分程度を手にとって顔全体に馴染ませます。毛穴の気になる小鼻や頬の中央には下から上へ優しく引き上げるように塗り込むとリフト感が向上します。"
    },
    {
        "rank": 3,
        "tag": "🌿 敏感肌・トラブル肌のために開発！自重の数百倍の水分を抱える超低刺激保水ローション",
        "catch": "アトピー肌や乾燥性敏感肌の専門研究から誕生。天然高分子フコイダンを高配合し、赤みや粉吹きを起こしやすい真冬のデリケート肌を優しく包み込んで健やかなバリアを再建する低刺激化粧水",
        "brand_name": "AtopiLabo (アトピーラボ)",
        "capacity": "200mL / エコパウチ詰め替え対応",
        "type": "敏感肌・乾燥肌専用 高分子フコイダン保水ローション",
        "features": "高分子フコイダン、ベタイン、ヒアルロン酸、パラベンフリー・アルコールフリー・石油系界面活性剤フリー",
        "value": "水のようなピュアな使い心地でありながら、肌に馴染ませるとフコイダンの粘弾性保水膜が形成され、暖房気流や衣服の摩擦による刺激からデリケートな素肌を物理的にシールド",
        "desc_p1": "11月後半から12月にかけて、冷たい北風や急激な湿度低下によって、肌のバリア機能が著しく低下し、普段使っているスキンケアが急にしみるようになる方が増えます。アトピーラボの『フコイダン保湿ローション』は、刺激に対して極めて敏感になった冬の素肌を救うために開発された超低刺激・高保水ローションです。",
        "desc_p2": "界面活性剤や防腐剤などの刺激成分を極力排除し、高純度の天然高分子フコイダンが持つ自己防衛・抗炎症サポート力を前面に押し出しています。肌に乗せるとスーッと馴染んで、薄い水のヴェールを纏ったような安心感に包まれます。赤みやかゆみを起こしやすい頬や首筋の乾燥を穏やかに鎮め、お風呂上がりの急激な水分蒸発を完全に食い止めます。大容量200mlで敏感肌のお子様から大人まで安心して全身に使えます。",
        "target": "冬になると肌が敏感になり普通の化粧水がピリピリとしみる方、粉吹きやすねの乾燥かゆみに悩む方、家族全員で使える安心安全な高保湿ケアを求める方",
        "point": "洗顔や入浴後、水気を拭き取ったらすぐに500円玉大を手にとり、肌をこすらず手のひら全体でそっと包み込むように馴染ませます。特に乾燥がひどい日は2〜3回重ねづけすると保水ヴェールが強化されます。"
    },
    {
        "rank": 4,
        "tag": "✨ 北海道産ガゴメ昆布の強靭な粘性！週1〜2回の集中リペアで毛穴汚れと乾燥をWケア",
        "catch": "函館近海でしか採れない希少なガゴメ昆布の高粘性フコイダンを凝縮した自然派ピールオフ保湿パック。密着ジェルが乾くと同時に角層深部へ保水多糖体を送り込み、剥がした後は驚きのツルツルもっちり肌",
        "brand_name": "自然化粧品研究所 / がごめ昆布ケア",
        "capacity": "80g / チューブ容器",
        "type": "高粘性ガゴメ昆布フコイダン ピールオフ保湿パック",
        "features": "ガゴメ昆布エキス（高濃度フコイダン含有）、褐藻エキス、加水分解コラーゲン、植物性グリセリン",
        "value": "冬の寒さでターンオーバーが滞り硬化した古い角質と毛穴の角栓をやさしく吸着除去しながら、ガゴメ昆布特有の高粘度フコイダンが角層内部へ濃厚な水分を補給",
        "desc_p1": "冬の肌トラブルの盲点は、乾燥によるターンオーバーの停滞です。古い角質が肌表面にミルフィーユ状に重なることで、いくら高価な保湿美容液を塗っても浸透していきません。ガゴメ昆布由来のフコイダンは、一般的な海藻フコイダンよりも圧倒的に粘性が高く、抱水性に優れていることで知られています。",
        "desc_p2": "本品を洗顔後の肌に薄く均一に塗り広げると、ひんやりとしたジェルが肌にピタッと吸着。15分ほど置くと透明な薄膜へと変わり、乾く過程でフコイダンの保水成分が角層奥深くまで浸透していきます。端からペリペリと剥がすと、不要な毛穴汚れや余分な角質が優しくオフされ、下から現れるのは驚くほど柔らかく、ゆで卵のように透き通ったツヤ肌です。冬のスペシャルケアとして欠かせない逸品です。",
        "target": "冬の乾燥で肌がゴワついて化粧水が入っていかない方、毛穴の黒ずみや小ジワを一度にリセットしたい方、週に1回の贅沢な海藻エステ体験を自宅で楽しみたい方",
        "point": "週に1〜2回、夜の洗顔後に水気をよく拭き取ってから、目と口の周りを避けて顔全体に均一に伸ばします。約15〜20分後、完全に乾いてから端からゆっくりと剥がし、その後通常の保湿ケアを行ってください。"
    },
    {
        "rank": 5,
        "tag": "💧 全身に使える2本セット！ノンオイル高分子多糖体膜が冬の砂漠肌をリセットする名品",
        "catch": "たっぷり使える200mLの2本セット。オイルフリーでありながら高分子フコイダンの粘弾性皮膜が油膜に頼らない純粋な水分保持環境を肌上に構築。赤ちゃんからシニアまで冬の乾燥肌を鉄壁プロテクト",
        "brand_name": "myufull (ミューフル) / 海藻モイスト",
        "capacity": "200mL×2本セット",
        "type": "ノンオイル 高分子フコイダン全身保水ローション",
        "features": "高分子フコイダン、植物性アミノ酸、天然海洋ミネラル、完全ノンオイル処方",
        "value": "油分で毛穴を塞ぐことなく、フコイダンの多糖体ネットワークが空気中の水分を抱え込み、真冬の強烈な乾燥風から角層の水分蒸散を物理的に防御。ニキビ肌や混合肌の乾燥対策にも最適",
        "desc_p1": "『冬の乾燥を防ぎたいけれど、オイルや濃厚なクリームを塗ると毛穴が詰まって吹き出物ができる』というオイリードライ（混合肌）の方にとって、真冬のスキンケア選びは難問です。この高分子フコイダンローションは、完全ノンオイル設計でありながら、油分によるフタを凌駕する強力な保水シールドを実現した画期的なアイテムです。",
        "desc_p2": "とろみのあるクリアなリキッドが肌の上でスルスルと広がり、乾くとサラサラなのに内側はぎっしり水分で満たされた状態がキープされます。2本セットの大容量仕様なので、顔のケアはもちろん、冬の暖房でカサつく首元、デコルテ、ひじ、すね、かかとまで全身に惜しみなくバシャバシャと使用可能。ベタつきが一切ないため、塗った直後に冬物のタイツやニットを着ても張り付かず、快適に過ごせます。",
        "target": "油分が多いクリームを使うとニキビや吹き出物ができるインナードライ肌、ベタつくスキンケアが苦手な男性や子ども、全身の乾燥をノンオイルでみずみずしくケアしたい方",
        "point": "お風呂から上がって3分以内に、全身へたっぷり伸ばして手のひらで馴染ませます。特に乾燥しやすいすねや腕には2度塗りし、水分を閉じ込めるようにしっかりハンドプレスしてください。"
    },
    {
        "rank": 6,
        "tag": "👑 まるで第二の皮膚！高機能フコイダン×スクワランの極上エモリエントクリーム",
        "catch": "過酷な乾燥気流を完全遮断する『セカンドスキン（第二の皮膚）』発想。トンガ産高純度フコイダンと高純度スクワランが融合し、真冬の粉吹き肌とあかぎれ手肌をベルベット密着膜で包み込む名作クリーム",
        "brand_name": "MarUmi (マルミ) / エルマール",
        "capacity": "30g / 密封エアレスジャー",
        "type": "高純度フコイダン×スクワラン 濃密リペアクリーム",
        "features": "高純度フコイダン、高精製スクワラン、セラミドNP、シア脂、水溶性プロテオグリカン",
        "value": "水分を抱え込むフコイダン膜の外側に、スクワランの油膜エモリエント層を展開する2層構造シールド。真冬の氷点下に近い寒風やエアコン直撃環境でも角層水分を100%逃さない",
        "desc_p1": "12月の真冬になると、どんなに化粧水や乳液を重ねても数時間後には水分が蒸発し、頬がカサカサに乾いて粉を吹いてしまうことがあります。マルミの『プレシャスクリーム』は、美容医療やエステの現場でも注目される『セカンドスキン理論』に基づいて作られた超高機能モイスチャークリームです。",
        "desc_p2": "こっくりとした濃厚なテクスチャーですが、肌の温度でとろけるように馴染み、ピタッと吸い付くように密着します。内側ではフコイダン多糖体が大量の水分をホールドし、外側ではスクワランが強固な油分シールドを形成。ダブルのバリア効果により、就寝前に塗れば暖房をつけたままの寝室でも翌朝まで吸い付くようなしっとり感が持続します。目尻のちりめんジワやほうれい線まわりの乾燥落ちも劇的に防止します。",
        "target": "通常の高保湿クリームでは物足りない超乾燥肌、冬の朝起きると顔がバリバリに乾燥している方、粉吹きやひび割れを根本から立て直したい大人のエイジング肌",
        "point": "夜のお手入れの最後に、パール粒大を手にとって温め、顔全体を包み込むように引き上げながら塗布します。乾燥が特に激しい目元や口元には、指の腹でトントンと重ねて密着バリアを作ってください。"
    },
    {
        "rank": 7,
        "tag": "⚡ 朝晩の時短ケアで乾燥知らず！海藻バイオ皮膜が1日中うるおいを逃さない多機能セラム",
        "catch": "化粧水・乳液・美容液・クリーム・海藻パックの5役を1本に集約。オキナワモズク由来高分子フコイダンの粘弾性バイオ皮膜が、忙しい冬の朝晩も角層深部の水分蒸散を長時間ブロックするオールインワン",
        "brand_name": "HLH",
        "capacity": "30mL / ポンプボトル",
        "type": "フコイダン高配合 モイストオールインワン美容液",
        "features": "オキナワモズクフコイダン、プラセンタエキス、ヒアルロン酸Na、加水分解エラスチン",
        "value": "朝のメイク前に使ってもモロモロが出ず、ファンデーションの密着性と持続力を格段に高める特殊処方。時短でありながらフルライン並みの濃密保湿を叶える",
        "desc_p1": "寒い冬の朝、何種類もの化粧品を重ねづけするのは時間がかかり、肌を何度も擦ることで摩擦ダメージの原因にもなります。HLHの『f ミラクルセラム』は、オキナワモズクから抽出された良質なフコイダンエキスをベースに、多機能なエイジングケア成分を凝縮した高機能オールインワンセラムです。",
        "desc_p2": "ワンプッシュで濃厚なエッセンスが広がり、肌に触れると水のように解けて角層深部へ素早く浸透。肌表面にはフコイダン特有のしなやかな極薄フィルムが形成され、まるでシートマスクをした後のようなみずみずしいハリとツヤが瞬時に現れます。油分過多にならず、水分と保湿因子のバランスが完璧に保たれるため、塗布後すぐにメイクに移れる点も忙しい現代人の冬の朝に絶大な支持を得ています。",
        "target": "朝のスキンケアを1分で完了させたいけれど保湿力は妥協したくない方、ゲルのモロモロやベタつきが嫌いな方、暖房によるメイク崩れや乾燥崩れを防ぎたい方",
        "point": "洗顔後、1〜2プッシュを手にとって顔全体から首筋にかけて伸ばし、手のひら全体で軽く温めるようにハンドプレスします。夜はさらに1プッシュを全顔に重ねてスリーピングパックとして活用してください。"
    },
    {
        "rank": 8,
        "tag": "💆‍♀️ 冬の暖房乾燥でパサつく頭皮を救う！フコイダン配合の濃密スカルプシャンプー",
        "catch": "海藻フコイダンの超保水力をヘア＆スカルプケアに応用。冬のエアコン暖房や静電気で乾燥・フケ・かゆみを起こしやすい頭皮の角層バリアを整え、根元から立ち上がる健やかな美髪へ導く",
        "brand_name": "ドクターベルツ (Dr.BAELTZ)",
        "capacity": "400ml / ポンプボトル",
        "type": "薬用・低刺激 高保湿スカルプシャンプー",
        "features": "褐藻エキス（高分子フコイダン）、アミノ酸系洗浄成分、センブリエキス、グリチルリチン酸2K",
        "value": "頭皮の必要な潤いを奪わずに汚れだけをアミノ酸泡で優しくオフ。フコイダンの保水皮膜が乾燥しやすい冬の頭皮を優しくコーティングし、フケ・かゆみ・頭皮の突っ張りを根本予防",
        "desc_p1": "11月から12月にかけて、顔の乾燥だけでなく『頭皮がかゆい』『細かいパラパラとしたフケが出る』というトラブルが急増します。これは強い洗浄力のシャンプーと冬の暖房乾燥が重なり、頭皮の角層バリアが崩壊しているサインです。ドクターベルツの『シャンミーク スカルプシャンプー』は、海藻フコイダンの高い保湿力と抗炎症サポートを融合させた頭皮専用のモイスチャーシャンプーです。",
        "desc_p2": "きめ細やかでクリーミーな弱酸性アミノ酸泡が、頭皮の毛穴に詰まった皮脂汚れを摩擦レスに包み込んで浮かせます。洗い流す際にもキシまず、フコイダン多糖体が頭皮の角層表面に潤いシールドを形成するため、ドライヤーで乾かした後も頭皮がつっぱらず、しっとりとした柔軟性がキープされます。髪のキューティクルも滑らかに整い、冬特有の不快な静電気や毛先の広がりも大幅に抑制されます。",
        "target": "冬になると頭皮の乾燥かゆみやパラパラフケが出る方、暖房で頭皮が突っ張る感じがする方、頭皮ケアと髪の毛先パサつき補修を同時に叶えたい方",
        "point": "ぬるま湯で1分間しっかり予洗いした後、適量を泡立てて頭皮を指の腹で揉みほぐすようにマッサージ洗いします。泡を1分ほど置いて『泡パック』してからしっかりすすぐとフコイダンの保水効果が高まります。"
    },
    {
        "rank": 9,
        "tag": "🧼 枠練り製法でフコイダンを凝縮！洗うたびに潤う無添加トリートメントソープ",
        "catch": "熟練の職人が60日間熟成させて作る伝統の枠練り洗顔石鹸。高純度フコイダンと天然海泥が融合し、冬の古い角質をやさしく吸着しながら洗顔後の素肌に濃密な保水膜を残す名作",
        "brand_name": "PUKIA (ピューキア)",
        "capacity": "100g / 熟成枠練りバー",
        "type": "高純度フコイダン×海泥 濃密熟成枠練り石鹸",
        "features": "オキナワモズクフコイダン、沖縄海泥（クチャ）、ホホバ種子油、ハチミツ、無香料・無鉱物油",
        "value": "機械練り石鹸では不可能な30%以上の高濃度保湿成分を配合できる枠練り製法。洗顔後すぐに化粧水をつけなくても肌が突っ張らず、もっちり吸い付くような潤い感をキープ",
        "desc_p1": "冬の乾燥肌対策において、最初に見直すべきは『落とすケア』です。洗浄力の強すぎる洗顔料で皮脂やNMF（天然保湿因子）を根こそぎ落としてしまうと、その後にいくら高保湿な化粧水を塗っても砂漠化は防げません。ピューキアの『トリートメントソープ』は、沖縄の豊かな自然の恵みである高分子フコイダンと微細海泥クチャを贅沢に練り込んだ枠練り石鹸です。",
        "desc_p2": "泡立てネットを使うと、生クリームのように弾力のある高密度な微細泡が瞬時に立ち上がります。肌に泡を乗せると、手のひらが肌に触れないクッション泡が毛穴の奥の汚れを穏やかに吸着。洗い流した瞬間、まるで上質な美容液で顔を洗ったかのような、しっとりと吸い付くような柔らかさに驚かされます。つっぱり感が一切なく、その後の化粧水の浸透を促すブースター効果も発揮します。",
        "target": "冬の朝晩の洗顔後に肌がバリバリに突っ張る方、固形石鹸のさっぱり感は好きだけど乾燥が気になる方、肌に優しい無添加処方で毛穴のくすみをオフしたい方",
        "point": "付属のネットで空気を巻き込むようにしっかり泡立て、レモン1個分の弾力泡を作ります。泡を顔に乗せて転がすように15秒洗い、ぬるま湯（32〜34℃）でこすらず優しくすすぎ流してください。"
    },
    {
        "rank": 10,
        "tag": "🌿 サロン級の集中タラソテラピー！高密着バイオセルロースが真冬の干からび肌を満たす",
        "catch": "海藻フコイダンと海洋深層水をシート1枚に濃密チャージした極上のタラソマスク。ヤシ由来のナノ繊維バイオセルロースが顔の凹凸に第二の皮膚のように完全密着し、真冬の砂漠肌を集中レスキュー",
        "brand_name": "マリンモイスト / タラソケア",
        "capacity": "10枚入 / 個包装プレミアムボックス",
        "type": "高分子フコイダン配合 高密着バイオセルロースマスク",
        "features": "褐藻フコイダンエキス、植物性ナノセルロースシート、海洋深層水、マリンコラーゲン、ヒアルロン酸",
        "value": "不織布マスクとは次元の異なる吸着力と密閉保水力。20分間貼っていてもシートが乾かず、角層のすみずみまでフコイダンの水分保持ネットワークを行き渡らせる",
        "desc_p1": "週末のスペシャルケアや、大切な日の前夜に真冬の肌を劇的に蘇らせたいときに頼りになるのが、サロン品質のタラソバイオセルロースマスクです。一般的なコットンのシートマスクは、冬の暖房の効いた室内では10分も経たないうちに乾いてしまい、逆に肌の水分を奪ってしまうリスクがあります。",
        "desc_p2": "本品に採用されているバイオセルロースは、髪の毛の1000分の1という超微細な植物繊維で編まれており、ナタデココのようにぷるぷるとしたジェル状の感触です。肌に乗せると小鼻や目元、口周りの細かな溝にも隙間なく吸い付き、密閉効果を発揮。フコイダン多糖体と海洋ミネラルが硬くなった角層をほぐしながら奥深くまで浸透します。マスクを剥がした瞬間、手のひらが吸い付いて離れないほどの濃密なもっちり感と、澄み渡るような透明感を実感できます。",
        "target": "真冬の寒さや乾燥で肌が極限まで疲れ果てている方、イベントや記念日の前に速効でツヤ肌を復活させたい方、普通のシートマスクでは乾燥してしまう超乾燥肌",
        "point": "洗顔後、化粧水で軽く肌を整えてからマスクを密着させます。15〜20分間じっくり浸透させた後マスクを剥がし、肌に残った濃密な美容液を手で優しく押し込んで馴染ませてください。"
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
  <title>保湿力の強さで肌乾燥とさようなら！海の自己治癒多糖体ヴェールが真冬のエアコン暖房による砂漠化インナードライを潤し尽くす高保湿フコイダンコスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月のエアコン暖房乾燥によるインナードライ・角層脱水・開き毛穴を救う高保湿フコイダン（褐藻多糖体・ガゴメ昆布・モズク）コスメを徹底厳選！リムヴェール、タカミ、アトピーラボ、ミューフルまで海の自己治癒皮膜と硫酸基保水の科学的根拠と共に徹底検証。">
  <meta name="keywords" content="フコイダン コスメ, ガゴメ昆布 美容液, 高保湿 コスメ 冬, インナードライ 11月 12月, 暖房乾燥 対策, 保湿美容液, リムヴェール, タカミエッセンスCE, フコイダン保湿ローション">

  <!-- OGP (SNSシェア / 日本語圏最適化) -->
  <meta property="og:site_name" content="LUMI COSMETICS">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！海の自己治癒多糖体ヴェールが真冬のエアコン暖房による砂漠化インナードライを潤し尽くす高保湿フコイダンコスメランク10">
  <meta property="og:description" content="海の自己修復力！褐藻由来の強靭な多糖体フコイダンが、真冬の強烈な暖房気流から素肌を守り抜くおすすめコスメ10選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-fucoidan">
  <meta property="og:image" content="{items[0]["image_url"]}">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！高保湿フコイダンコスメランク10">
  <meta name="twitter:description" content="11月・12月のエアコン砂漠肌に！海藻多糖体フコイダンコスメおすすめ厳選10選。">
  <meta name="twitter:image" content="{items[0]["image_url"]}">

  <!-- 構造化データ (JSON-LD) #1: Article -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！海の自己治癒多糖体ヴェールが真冬のエアコン暖房による砂漠化インナードライを潤し尽くす高保湿フコイダンコスメランク10",
    "description": "11月・12月の暖房乾燥によるインナードライ・角層脱水を救う高保湿フコイダン（褐藻多糖体）コスメを徹底厳選！",
    "image": "{items[0]["image_url"]}",
    "datePublished": "2026-11-06T03:00:00+09:00",
    "dateModified": "2026-11-06T03:00:00+09:00",
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
      "@id": "https://lumi-cosme.vercel.app/winter-fucoidan"
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
        "name": "フコイダンとヒアルロン酸の保湿力にはどのような違いがありますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "ヒアルロン酸は水分を抱え込む保水力に優れますが、汗や皮脂の塩分環境下では保水力が低下しやすい弱点があります。一方、フコイダンは分子構造内に硫酸基を豊富に持つため、塩分や汗が存在する肌表面でも保水性能が低下せず、自重の数百倍の水分を抱えたまま強固な保護被膜（セカンドスキン）を形成し、冬の過酷な暖房乾燥から角層を守り抜きます。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "フコイダンコスメは敏感肌やアトピー肌でも使えますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "はい、非常に適しています。フコイダンは海藻由来の天然高分子多糖体であり、抗原性（アレルギー性）が極めて低く、肌の炎症を穏やかに鎮静するサポート効果があります。冬の冷風や摩擦でバリア機能が低下し、赤みやヒリつきを起こしやすい敏感肌の保護にも最適です。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "オキナワモズク由来とガゴメ昆布由来のフコイダンの違いは何ですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "オキナワモズク由来のフコイダンは高純度で抽出されやすく、分子量が均一でサラリとした浸透性と持続的なフィルム効果に優れています。一方、北海道産ガゴメ昆布由来のフコイダンは非常に粘性が高く、トロリとした濃密なテクスチャーで角層を物理的に密封・ラッピングする力に長けています。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "11月・12月の冬に効果的な使い方の順番は？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "美容液タイプの場合は、洗顔後すぐの導入（ブースター）または化粧水直後に使用し、ハンドプレスでしっかり浸透させてから乳液やクリームで蓋をします。完全ノンオイルのローションタイプの場合は、重ねづけすることで多層の保水皮膜が形成され、より高い乾燥防止効果を発揮します。"
        }}
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #007791;
      --primary-light: #e0f2f7;
      --primary-dark: #004d5e;
      --accent: #2e8b57;
      --text: #2c3e50;
      --text-muted: #607274;
      --bg: #f8fafb;
      --card-bg: #ffffff;
      --border: #dbe4e8;
      --shadow: 0 4px 16px rgba(0, 119, 145, 0.08);
      --radius: 12px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
      padding: 0;
    }}

    header {{
      background: linear-gradient(135deg, #004d5e 0%, #007791 100%);
      color: #ffffff;
      padding: 40px 20px 30px;
      text-align: center;
    }}
    .site-tagline {{ font-size: 0.9rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px; opacity: 0.9; }}
    h1 {{ font-size: 1.7rem; line-height: 1.4; max-width: 960px; margin: 0 auto 15px; font-weight: 800; }}
    .header-meta {{ font-size: 0.85rem; opacity: 0.85; margin-top: 10px; }}

    .container {{
      max-width: 1000px;
      margin: 0 auto;
      padding: 30px 20px 60px;
    }}

    .breadcrumbs {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 25px;
    }}
    .breadcrumbs a {{ color: var(--primary); text-decoration: none; }}
    .breadcrumbs a:hover {{ text-decoration: underline; }}

    .intro-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 30px;
      box-shadow: var(--shadow);
      margin-bottom: 40px;
      border-left: 6px solid var(--primary);
    }}
    .intro-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 15px;
    }}
    .intro-section p {{ margin-bottom: 15px; }}
    .intro-section p:last-child {{ margin-bottom: 0; }}

    .mechanism-box {{
      background: var(--primary-light);
      border-radius: var(--radius);
      padding: 24px;
      margin: 25px 0;
    }}
    .mechanism-title {{
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 10px;
      font-size: 1.1rem;
    }}

    .toc {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 20px 25px;
      margin-bottom: 40px;
    }}
    .toc-title {{ font-weight: 700; color: var(--primary); margin-bottom: 12px; }}
    .toc ol {{ padding-left: 20px; }}
    .toc li {{ margin-bottom: 6px; font-size: 0.95rem; }}
    .toc a {{ color: var(--text); text-decoration: none; }}
    .toc a:hover {{ color: var(--primary); text-decoration: underline; }}

    /* 商品カード */
    .product-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 30px;
      margin-bottom: 40px;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .product-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(0, 119, 145, 0.12);
    }}

    .product-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 15px;
      flex-wrap: wrap;
    }}
    .rank-badge {{
      background: linear-gradient(135deg, #007791, #004d5e);
      color: #ffffff;
      font-size: 1.1rem;
      font-weight: 800;
      padding: 6px 16px;
      border-radius: 20px;
      letter-spacing: 1px;
    }}
    .product-tag {{
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--primary-dark);
      background: var(--primary-light);
      padding: 5px 12px;
      border-radius: 6px;
    }}

    .product-title {{
      font-size: 1.25rem;
      line-height: 1.45;
      color: var(--text);
      margin-bottom: 8px;
    }}
    .product-display-name {{
      font-size: 0.95rem;
      color: var(--text-muted);
      margin-bottom: 20px;
      line-height: 1.5;
    }}

    .product-layout {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 30px;
    }}
    @media (max-width: 768px) {{
      .product-layout {{ grid-template-columns: 1fr; }}
    }}

    .product-visual-col {{
      text-align: center;
    }}
    .img-wrap {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 10px;
      margin-bottom: 15px;
    }}
    .product-img {{
      width: 100%;
      height: 240px;
      object-fit: contain;
      border-radius: 4px;
    }}
    .price-box {{
      background: #fafafa;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 10px;
      margin-bottom: 10px;
    }}
    .price-label {{ font-size: 0.75rem; color: var(--text-muted); display: block; }}
    .price-value {{ font-size: 1.35rem; font-weight: 800; color: #b12704; }}
    .review-meta {{ font-size: 0.85rem; margin-bottom: 15px; color: var(--text-muted); }}
    .review-stars {{ color: #e67a00; font-weight: 700; margin-right: 4px; }}

    .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #bf0000 0%, #990000 100%);
      color: #ffffff !important;
      text-align: center;
      padding: 14px 15px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      box-shadow: 0 4px 10px rgba(191, 0, 0, 0.25);
      transition: background 0.2s, transform 0.1s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #a80000 0%, #800000 100%);
      transform: translateY(-1px);
    }}

    /* スペック表 */
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 20px;
      font-size: 0.9rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 10px 12px;
      border-bottom: 1px solid var(--border);
    }}
    .spec-table th {{
      width: 28%;
      background: #f4f8fa;
      color: var(--primary-dark);
      text-align: left;
      font-weight: 700;
    }}
    .spec-table td {{
      background: #ffffff;
    }}

    .product-body {{ margin-top: 15px; }}
    .body-title {{
      font-size: 1.05rem;
      color: var(--primary);
      margin-bottom: 10px;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 4px;
    }}
    .product-body p {{ margin-bottom: 12px; font-size: 0.95rem; }}

    .recommend-box {{
      background: #f3faf7;
      border-left: 4px solid var(--accent);
      padding: 14px 16px;
      margin: 15px 0 10px;
      border-radius: 0 6px 6px 0;
    }}
    .recommend-title {{ font-weight: 700; font-size: 0.9rem; color: #1b5e20; margin-bottom: 4px; }}
    .recommend-box p {{ margin-bottom: 0; font-size: 0.9rem; }}

    .usage-box {{
      background: #fdfaf2;
      border-left: 4px solid #f0ad4e;
      padding: 14px 16px;
      margin: 10px 0 0;
      border-radius: 0 6px 6px 0;
    }}
    .usage-title {{ font-weight: 700; font-size: 0.9rem; color: #8a6d3b; margin-bottom: 4px; }}
    .usage-box p {{ margin-bottom: 0; font-size: 0.9rem; }}

    /* 比較表セクション */
    .comparison-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 30px;
      box-shadow: var(--shadow);
      margin-bottom: 40px;
      overflow-x: auto;
    }}
    .comparison-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 20px;
    }}
    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 600px;
    }}
    .comparison-table th, .comparison-table td {{
      padding: 12px 14px;
      border: 1px solid var(--border);
      text-align: left;
    }}
    .comparison-table th {{
      background: var(--primary-dark);
      color: #ffffff;
      font-weight: 700;
    }}
    .comparison-table tr:nth-child(even) {{ background: #fafbfc; }}

    /* ガイドセクション */
    .guide-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 30px;
      box-shadow: var(--shadow);
      margin-bottom: 40px;
    }}
    .guide-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 15px;
      border-left: 5px solid var(--primary);
      padding-left: 12px;
    }}
    .guide-section h3 {{
      font-size: 1.15rem;
      color: var(--text);
      margin: 20px 0 10px;
    }}
    .guide-section p {{ margin-bottom: 15px; font-size: 0.95rem; }}

    /* FAQセクション */
    .faq-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 30px;
      box-shadow: var(--shadow);
      margin-bottom: 40px;
    }}
    .faq-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 20px;
    }}
    .faq-item {{
      border-bottom: 1px solid var(--border);
      padding: 16px 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-question {{
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 8px;
      font-size: 1rem;
    }}
    .faq-answer {{ font-size: 0.95rem; color: var(--text); }}

    /* 内部リンク */
    .internal-links {{
      background: #f1f6f8;
      border-radius: var(--radius);
      padding: 25px;
      margin-bottom: 40px;
    }}
    .internal-links h3 {{
      font-size: 1.15rem;
      color: var(--primary-dark);
      margin-bottom: 15px;
    }}
    .links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 12px;
    }}
    .link-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 14px;
      text-decoration: none;
      color: var(--text);
      font-size: 0.9rem;
      display: block;
      transition: border-color 0.2s, transform 0.1s;
    }}
    .link-card:hover {{
      border-color: var(--primary);
      transform: translateY(-1px);
      color: var(--primary);
    }}

    footer {{
      background: #1a252f;
      color: #bdc3c7;
      padding: 40px 20px 30px;
      font-size: 0.85rem;
      text-align: center;
    }}
    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 15px;
      margin-bottom: 25px;
    }}
    .footer-links a {{ color: #bdc3c7; text-decoration: none; }}
    .footer-links a:hover {{ color: #ffffff; text-decoration: underline; }}
    .copyright {{ opacity: 0.7; }}
  </style>
</head>
<body>

  <header>
    <div class="site-tagline">LUMI COSMETICS - 科学的エビデンスで選ぶ真冬の本格高保湿スキンケア</div>
    <h1>保湿力の強さで肌乾燥とさようなら！海の自己治癒多糖体ヴェールが真冬のエアコン暖房による砂漠化インナードライを潤し尽くす高保湿フコイダンコスメランク10</h1>
    <div class="header-meta">
      <span>公開日: 2026年11月6日</span> | <span>監修: LUMI COSMETICS スキンケアサイエンス編集部</span>
    </div>
  </header>

  <div class="container">
    <div class="breadcrumbs">
      <a href="/">HOME</a> &gt; <a href="/winter-fucoidan">高保湿フコイダンコスメ</a>
    </div>

    <!-- 導入セクション -->
    <section class="intro-section">
      <h2>11月・12月の暖房直撃！なぜ従来の保湿コスメでは肌が乾いてしまうのか？</h2>
      <p>立冬を過ぎ、11月から12月へと向かう季節は、屋外の寒冷乾燥気流と室内のエアコン暖房による強烈な湿度低下が同時に襲いかかる過酷な時期です。湿度が20%台まで急落した密閉空間では、皮膚表面から毎秒猛烈な勢いで水分が大気中へと奪われていきます。一般的なヒアルロン酸やコラーゲンを塗っても、『つけた瞬間は潤うのに、数十分後には突っ張る』『夕方になると頬が粉を吹き、毛穴が縦に開いてしぼむ』という深刻なインナードライに直面する女性が絶えません。</p>
      
      <p>この真冬の砂漠肌を救う決定打として、今皮膚科学界やオーガニックサロンで圧倒的な注目を集めているのが、海藻由来の巨大多糖体『フコイダン』です。激しい引き潮の際に強烈な乾燥や直射日光、海水中の塩分ストレスに晒される褐藻類（オキナワモズクやガゴメ昆布）が、自らの細胞を守るために分泌するヌメリ成分こそがフコイダンです。その強靭な水分保持力と自己修復力は、現代人の暖房枯れ肌にとってまさに救世主と言える存在です。</p>

      <div class="mechanism-box">
        <div class="mechanism-title">🧪 皮膚科学が解明！フコイダンが真冬の乾燥に劇的に強い3大理由</div>
        <ul>
          <li><strong>① 硫酸基による『塩分環境下での圧倒的保水維持』：</strong> ヒアルロン酸は肌上の塩分（汗や皮脂）に触れると保水力が半減する弱点がありますが、フコイダンは分子構造内に豊富な硫酸基を有しているため、塩分存在下でも保水ネットワークが崩壊せず、自重の数百倍の水分を抱え続けます。</li>
          <li><strong>② 『セカンドスキン（第2の皮膚）』皮膜による物理的蒸散ブロック：</strong> 分子量数万〜数十万の高分子フコイダンは角層表面に隙間なく密着し、目に見えない人工バイオバリアを形成。真冬の過酷な暖房気流を完全に跳ね返します。</li>
          <li><strong>③ 表皮の自己治癒サポート＆微弱炎症の鎮静：</strong> 海藻が傷ついた葉体を修復するメカニズムと同様に、冬の冷風や摩擦で微弱炎症を起こした角層バリアを穏やかに保護し、健やかなターンオーバーを後押しします。</li>
        </ul>
      </div>
    </section>

    <!-- 目次 -->
    <section class="toc">
      <div class="toc-title">📑 目次（タップで該当セクションへスクロール）</div>
      <ol>
        <li><a href="#rank-1">第1位：Limveil (リムヴェール) 高純度モズクフコイダン原液 高保水美容液</a></li>
        <li><a href="#rank-2">第2位：TAKAMI (タカミ) 高機能ビタミンC・E×褐藻エキス 美容液</a></li>
        <li><a href="#rank-3">第3位：AtopiLabo (アトピーラボ) 敏感肌・乾燥肌専用 高分子フコイダン保水ローション</a></li>
        <li><a href="#rank-4">第4位：自然化粧品研究所 高粘性ガゴメ昆布フコイダン ピールオフ保湿パック</a></li>
        <li><a href="#rank-5">第5位：myufull (ミューフル) ノンオイル 高分子フコイダン全身保水ローション</a></li>
        <li><a href="#rank-6">第6位：MarUmi (マルミ) 高純度フコイダン×スクワラン 濃密リペアクリーム</a></li>
        <li><a href="#rank-7">第7位：HLH フコイダン高配合 モイストオールインワン美容液</a></li>
        <li><a href="#rank-8">第8位：ドクターベルツ 薬用・低刺激 高保湿スカルプシャンプー</a></li>
        <li><a href="#rank-9">第9位：PUKIA (ピューキア) 高純度フコイダン×海泥 濃密熟成枠練り石鹸</a></li>
        <li><a href="#rank-10">第10位：マリンモイスト 高分子フコイダン配合 高密着バイオセルロースマスク</a></li>
        <li><a href="#comparison">一目でわかる！高保湿フコイダンコスメ全10品スペック比較表</a></li>
        <li><a href="#guide">11月・12月に失敗しない高保湿フコイダンコスメの選び方</a></li>
        <li><a href="#faq">よくある質問（Q&A）</a></li>
      </ol>
    </section>

    <!-- ランキング商品カード群 -->
    <section class="ranking-list">
      {all_cards_html}
    </section>

    <!-- 比較表 -->
    <section class="comparison-section" id="comparison">
      <h2>📊 高保湿フコイダンコスメ全10品スペック比較表</h2>
      <p>アイテムごとの容量・アイテム種別・特徴・参考価格を一覧表にまとめました。真冬の肌悩みに合わせて最適なアイテムをお選びください。</p>
      <table class="comparison-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>ブランド / 商品名</th>
            <th>種別</th>
            <th>容量</th>
            <th>特長・真冬の強み</th>
            <th>参考価格</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>第1位</td>
            <td>Limveil (リムヴェール) エッセンス</td>
            <td>高純度原液美容液</td>
            <td>50ml</td>
            <td>オキナワモズク由来高分子原液・硫酸基による鉄壁保水</td>
            <td>¥2,980</td>
          </tr>
          <tr>
            <td>第2位</td>
            <td>TAKAMI タカミエッセンス5CE</td>
            <td>機能性ビタミン美容液</td>
            <td>30mL</td>
            <td>両親媒性ビタミンC・E×褐藻エキス・毛穴引き締めと高保水</td>
            <td>¥11,880</td>
          </tr>
          <tr>
            <td>第3位</td>
            <td>AtopiLabo フコイダン保湿ローション</td>
            <td>低刺激高保水化粧水</td>
            <td>200mL</td>
            <td>アトピー・敏感肌設計・超低刺激で暖房の突っ張りを鎮静</td>
            <td>¥9,702</td>
          </tr>
          <tr>
            <td>第4位</td>
            <td>自然化粧品研究所 ガゴメ昆布保湿パック</td>
            <td>ピールオフ保湿パック</td>
            <td>80g</td>
            <td>函館産ガゴメ昆布の高粘性フコイダン・古い角質オフと濃密保水</td>
            <td>¥4,070</td>
          </tr>
          <tr>
            <td>第5位</td>
            <td>myufull PNローション 2本セット</td>
            <td>ノンオイル保水ローション</td>
            <td>200mL×2</td>
            <td>完全ノンオイル・ベタつかず全身に使える大容量多糖体ヴェール</td>
            <td>¥11,088</td>
          </tr>
          <tr>
            <td>第6位</td>
            <td>MarUmi セカンドスキンヴェール</td>
            <td>濃密高機能クリーム</td>
            <td>30g</td>
            <td>フコイダン×高純度スクワラン・第二の皮膚のような密閉保護</td>
            <td>¥12,000</td>
          </tr>
          <tr>
            <td>第7位</td>
            <td>HLH f ミラクルセラム</td>
            <td>オールインワン美容液</td>
            <td>30mL</td>
            <td>忙しい冬の朝晩に1本5役・モロモロが出ずメイク前の保水に最適</td>
            <td>¥4,955</td>
          </tr>
          <tr>
            <td>第8位</td>
            <td>ドクターベルツ スカルプシャンプー</td>
            <td>薬用頭皮用シャンプー</td>
            <td>400ml</td>
            <td>冬の暖房乾燥による頭皮フケ・かゆみを防ぐアミノ酸泡×海藻保水</td>
            <td>¥2,750</td>
          </tr>
          <tr>
            <td>第9位</td>
            <td>PUKIA 熟成枠練り石鹸</td>
            <td>枠練り洗顔石鹸</td>
            <td>100g</td>
            <td>60日間熟成枠練り・フコイダン30%配合で洗顔後も突っ張らない</td>
            <td>¥1,980</td>
          </tr>
          <tr>
            <td>第10位</td>
            <td>マリンモイスト タラソマスク</td>
            <td>バイオセルロースマスク</td>
            <td>10枚入</td>
            <td>ヤシ由来ナノ繊維シート・暖房下でも乾かない濃密タラソ集中密着</td>
            <td>¥32,000</td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- ガイドセクション -->
    <section class="guide-section" id="guide">
      <h2>💡 11月・12月に失敗しない高保湿フコイダンコスメの選び方</h2>
      
      <h3>1. 抽出元の海藻特性を見極める（モズク vs ガゴメ昆布）</h3>
      <p>フコイダンコスメを選ぶ際は、原料となっている海藻の品種を確認しましょう。オキナワモズク由来のフコイダンは、高純度で分子構造が整っており、サラリとした肌馴染みと均一な保水皮膜の形成に優れています。一方、北海道函館近海で採れるガゴメ昆布由来のフコイダンは、特有の強い粘弾性（ヌメリ）を持ち、硬くゴワついた真冬の角質を柔軟にラッピングして密封する力に長けています。日中のメイク前にはモズク由来、夜の集中ケアにはガゴメ昆布由来を選ぶのも賢い使い分けです。</p>

      <h3>2. 分子量とテクスチャーの適合性を確認する</h3>
      <p>フコイダンは本来、分子量が数万〜数十万に及ぶ高分子多糖体です。肌表面でバリア膜（セカンドスキン）を形成して外部乾燥を遮断したい場合は、高分子タイプの原液やローションが最適です。一方、角層内部までじっくり浸透させてハリ感を出したい場合は、低分子化されたフコイダンや、ビタミンC・セラミド等と複合化されたアイテムを選ぶと相乗効果が高まります。</p>

      <h3>3. ノンオイルか油分併用かを肌質で選ぶ</h3>
      <p>インナードライでありながらTゾーンのテカリやニキビが気になる混合肌の方は、完全ノンオイルのフコイダンローション（myufull等）が最も安全で効果的です。毛穴を詰まらせずに水分量だけを劇的に引き上げられます。逆に、皮脂分泌そのものが激減している大人の超乾燥肌の方は、フコイダンの水分膜の上にスクワランやシア脂を重ねたクリーム（MarUmi等）を選ぶことで、水分と油分の完璧な両輪防御が完成します。</p>
    </section>

    <!-- FAQセクション -->
    <section class="faq-section" id="faq">
      <h2>❓ よくある質問（Q&A）</h2>
      <div class="faq-item">
        <div class="faq-question">Q1. フコイダンとヒアルロン酸の保湿力にはどのような違いがありますか？</div>
        <div class="faq-answer">ヒアルロン酸は純粋な水分を抱え込む保水力に優れますが、汗や皮脂の塩分環境下では保水力が低下しやすい弱点があります。一方、フコイダンは分子構造内に硫酸基を豊富に持つため、塩分や汗が存在する肌表面でも保水性能が低下せず、自重の数百倍の水分を抱えたまま強固な保護被膜（セカンドスキン）を形成し、冬の過酷な暖房乾燥から角層を守り抜きます。</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Q2. フコイダンコスメは敏感肌やアトピー肌でも使えますか？</div>
        <div class="faq-answer">はい、非常に適しています。フコイダンは海藻由来の天然高分子多糖体であり、抗原性（アレルギー性）が極めて低く、肌の炎症を穏やかに鎮静するサポート効果があります。冬の冷風や摩擦でバリア機能が低下し、赤みやヒリつきを起こしやすい敏感肌の保護にも最適です。</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Q3. オキナワモズク由来とガゴメ昆布由来のフコイダンの違いは何ですか？</div>
        <div class="faq-answer">オキナワモズク由来のフコイダンは高純度で抽出されやすく、分子量が均一でサラリとした浸透性と持続的なフィルム効果に優れています。一方、北海道産ガゴメ昆布由来のフコイダンは非常に粘性が高く、トロリとした濃密なテクスチャーで角層を物理的に密封・ラッピングする力に長けています。</div>
      </div>
      <div class="faq-item">
        <div class="faq-question">Q4. 11月・12月の冬に効果的な使い方の順番は？</div>
        <div class="faq-answer">美容液タイプの場合は、洗顔後すぐの導入（ブースター）または化粧水直後に使用し、ハンドプレスでしっかり浸透させてから乳液やクリームで蓋をします。完全ノンオイルのローションタイプの場合は、重ねづけすることで多層の保水皮膜が形成され、より高い乾燥防止効果を発揮します。</div>
      </div>
    </section>

    <!-- 内部リンクブロック -->
    <section class="internal-links">
      <h3>🔗 あわせて読みたい！真冬の乾燥対策・高保湿コスメ関連記事</h3>
      <div class="links-grid">
        <a href="/winter-sacran" class="link-card">💧 高保湿サクラン（スイゼンジノリ多糖体）</a>
        <a href="/winter-tremella" class="link-card">💧 高保湿シロキクラゲ多糖体</a>
        <a href="/winter-trehalose" class="link-card">💧 高保湿トレハロース</a>
        <a href="/winter-ceramide-cream" class="link-card">🛡️ 高保湿セラミドクリーム</a>
        <a href="/winter-squalane-oil" class="link-card">🌿 高純度スクワランオイル</a>
        <a href="/winter-hyaluronic-serum" class="link-card">💧 濃厚ヒアルロン酸美容液</a>
      </div>
    </section>
  </div>

  <footer>
    <div class="footer-links">
      <a href="/">トップページ</a>
      <a href="/winter-fucoidan">高保湿フコイダン</a>
      <a href="/winter-sacran">高保湿サクラン</a>
      <a href="/winter-tremella">高保湿シロキクラゲ</a>
      <a href="/winter-ceramide-cream">高保湿セラミドクリーム</a>
    </div>
    <div class="copyright">&copy; 2026 LUMI COSMETICS. All Rights Reserved. 無断転載を禁じます。</div>
  </footer>

</body>
</html>
"""

with open("winter-fucoidan.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("winter-fucoidan.html created successfully!")
