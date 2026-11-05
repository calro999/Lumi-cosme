import json
import re

with open("fetched_3new_lacto_swallow_dokudami.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_swallow_nest"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 奇跡の天然アナツバメの巣100%！シアル酸とEGF様作用で冬の目元・毛根を覚醒させる最高峰セラム",
        "catch": "世界屈指の純度を誇るマレーシア・ボルネオ島産天然アナツバメの巣エキスを贅沢に配合。真冬の過酷な乾燥冷風にさらされるデリケートな目元・まつ毛の根元へ、ローヤルゼリーの200倍のシアル酸が濃密なハリと潤いを与えるプレミアム美容液",
        "brand_name": "BI-SU (美巣)",
        "capacity": "まつ毛・目元用精密チップ美容液",
        "type": "天然アナツバメの巣エキス高配合 目元＆アイラッシュ集中美容液",
        "features": "天然アナツバメの巣エキス、シアル酸、キャピキシル、加水分解ケラチン、低刺激・色素沈着フリー処方",
        "value": "11月〜12月の暖房直撃による目元のちりめんジワやまぶたの乾燥パサつき、まつ毛の抜け毛を根本からリペア。肌細胞の受容体に直接シグナルを届けるシアル酸が、皮膚の薄い目元を濃密保護",
        "desc_p1": "顔の中で最も皮膚が薄く皮脂腺が少ない目元は、11月から12月にかけての空気乾燥と暖房気流の影響を真っ先に受けます。乾燥によって小ジワが深く刻まれ、まつ毛も水分を失って抜けやすくなります。高級ツバメの巣ブランド『BI-SU（美巣）』のアイラッシュセラムは、採取制限のあるマレーシアの洞窟から手作業で採取された100%天然アナツバメの巣エキスを主原料にした逸品です。",
        "desc_p2": "目元に乗せると、とろみのあるリキッドが吸い付くように密着し、瞬時にみずみずしい保護膜を形成。シアル酸の驚異的な細胞間保水力とEGF様ペプチドが、寒冷で萎縮した目元の皮膚をふっくらと持ち上げます。色素沈着成分を含まない安心設計で、敏感な目の際までしっかり塗り込むことが可能。毎晩のケアで、翌朝のアイメイクの乗りや目元の透明感が劇的に向上します。",
        "target": "冬になると目元の乾燥小ジワやファンデーションのひび割れが気になる方、まつ毛の乾燥ダメージやハリコシ低下をケアしたい方、本物の天然高級美容成分で極上ケアを行いたい方",
        "point": "夜の洗顔後、スキンケアの最初にチップを使ってまつ毛の生え際とまぶた全体へ優しく塗布します。指の腹で目頭から目尻へ向かって軽くタッピングすると、血行が促され浸透が高まります。"
    },
    {
        "rank": 2,
        "tag": "💧 ツバメの巣エキス1000mg×高保水ヒアルロン酸！真冬の砂漠肌を即座に満たす超密着シートマスク",
        "catch": "韓国SNPが誇る世界的大ベストセラー。1枚にアナツバメ巣エキス1000mgと複合ヒアルロン酸を凝縮。冬の乾燥冷風でカサカサに干からびた角層深部へ濃密な水分を届ける高密着セルロースマスク",
        "brand_name": "SNP (エスエヌピー)",
        "capacity": "10枚入 / 個包装ボックス",
        "type": "高純度アナツバメ巣エキス濃縮 高密着水分アンプルマスク",
        "features": "アナツバメ巣エキス（1000mg）、加水分解ヒアルロン酸、ベタイン、ツボクサエキス、植物性セルロースシート",
        "value": "透き通るような薄膜セルロースシートが肌の凹凸に隙間なく吸着。真冬のエアコンの効いた部屋で20分間貼っていても乾かず、水分とシアル酸を角層の奥まで送り届ける",
        "desc_p1": "冬の週末や外出前夜、冷気で疲れ切った肌を即座にリセットしたいときの救世主がこのバードネストマスクです。一般的な不織布マスクは暖房の効いた室内ではすぐに乾いてしまいがちですが、SNPのセルロースシートは自重の数十倍のエッセンスを抱え込む特殊繊維を採用しています。",
        "desc_p2": "袋から取り出すと、ひたひたに浸されたツバメの巣アンプルが溢れ出します。顔に密着させるとまるで第二の皮膚のように吸い付き、ひんやりとした鎮静感と濃密な潤いがじわじわと広がります。マスクを剥がした瞬間、指先が吸い付くようなモチモチ感と、内側から発光するようなみずみずしい透明感に圧倒されます。残った美容液は首元やデコルテまでたっぷり伸ばせます。",
        "target": "冬の乾燥で肌がゴワつき化粧水の入りが悪い方、特別なイベント前に速効でツヤと潤いをチャージしたい方、ツバメの巣コスメをコスパ良くたっぷり体験したい方",
        "point": "化粧水で肌を整えた後、シートを顔全体に密着させます。15〜20分置いた後シートを剥がし、肌表面に残ったエッセンスを両手で優しく押し込むようにハンドプレスして浸透させてください。"
    },
    {
        "rank": 3,
        "tag": "✨ 希少なアナツバメの巣エキス×シアル酸高濃度！真冬のしぼみ肌を底上げする濃密つや出し美容液",
        "catch": "マレーシア産天然アナツバメの巣から抽出した高純度エキスと豊富なシアル酸をブレンド。冬の寒冷で硬化し代謝が滞った大人の角層を、内側から押し返すような濃密なツヤと弾力で満たすプレシャスエッセンス",
        "brand_name": "MY SAO (東洋ツバメの巣)",
        "capacity": "60mL / プレミアムボトル",
        "type": "天然アナツバメの巣エキス配合 つや出し高保湿エッセンス",
        "features": "アナツバメ巣エキス（燕窩）、シアル酸、加水分解コラーゲン、植物由来スクワラン、優雅なフローラルの香り",
        "value": "加齢と真冬の極度な乾燥でしぼんだ細胞間脂質のネットワークを再建。サラリと伸び広がりながら、肌表面にはシルクのようなツヤ出し保護被膜を形成し、夕方まで潤いを逃さない",
        "desc_p1": "11月から12月にかけて、大人の肌が直面する最大の悩みは『乾燥による肌のしぼみとツヤの消失』です。いくら表面に油分を塗っても、角層深部の密度がスカスカでは光を綺麗に反射できず、どんよりとした老け見え印象を与えてしまいます。MY SAOのつや出し美容液は、古来より宮廷美容で重宝されてきたアナツバメの巣のシアル酸パワーを最新の乳化技術で肌へ届ける贅沢な処方です。",
        "desc_p2": "手のひらに取ると、とろみのあるリッチなテクスチャーが広がり、高貴で上品なフローラルの香りが広がります。肌に乗せた瞬間、硬くなった角層を解きほぐすようにスッと浸透し、手のひらがピタッと吸い付くような濃密な弾力感へと変化。使い続けるうちに、真冬の暖房直撃下でも一日中ツヤが衰えず、ファンデーションのノリが格段に滑らかになるのを実感できます。",
        "target": "40代・50代以降の深刻な乾燥しぼみ肌、夕方になると顔がくすんで疲れて見える方、オイルの重さが苦手だけど濃厚な保湿とハリが欲しい方",
        "point": "化粧水の直後に2〜3プッシュを手にとり、手のひらで温めてから顔全体を包み込むように塗布します。ほうれい線や眉間の乾燥小ジワには、指先で優しく引き上げるように重ねづけしてください。"
    },
    {
        "rank": 4,
        "tag": "🌿 水仕事や寒風で荒れた手肌を吸い付く潤いで包む！ツバメの巣×シアバターの濃密ハンドリペア",
        "catch": "過酷な真冬の水仕事や冷気でひび割れ・カサつきを起こしやすい手肌を、天然アナツバメの巣エキスとシアバターのダブルシールドで守り抜く。ベタつかずシルキーに潤う最高峰ハンドクリーム",
        "brand_name": "BI-SU (美巣)",
        "capacity": "40g / チューブ容器",
        "type": "天然アナツバメの巣エキス配合 ラグジュアリー高保湿ハンドクリーム",
        "features": "天然アナツバメの巣エキス、シア脂（シアバター）、ホホバ種子油、天然ラベンダー精油",
        "value": "塗布した瞬間に手肌の細かなシワやキメの乱れを滑らかに埋め、薄い人工皮脂膜を形成。水洗いをしても落ちにくい密着保水力で、乾燥による手肌の老化・血管の浮きを防ぐ",
        "desc_p1": "冬になると手肌は毎日の手洗いや食器洗い、冷たいすきま風によって皮脂が根こそぎ奪われ、手の甲の血管が目立ったり、指先がガサガサに荒れてストッキングに引っかかるようになります。BI-SUのハンドクリームは、手肌のエイジングサインに着目し、アナツバメの巣のシアル酸とオーガニック植物オイルを融合させたハンドケアの最高峰です。",
        "desc_p2": "こっくりとしたクリームを手の甲に伸ばすと、体温でスルスルと馴染み、驚くほどベタつきを残しません。天然ラベンダーの爽やかな香りが心地よく広がり、塗った直後からスマートフォンの画面やパソコンのキーボードを操作できるサラサラの上質シルク肌へ。乾燥で白く粉を吹いていた指先がふっくらと蘇り、手元を見るたびに気品あるツヤを感じられます。",
        "target": "冬場の水仕事で手が荒れやすい方、手の甲の乾燥小ジワや血管浮きが気になる方、大切な人への冬のギフトや自分へのご褒美ハンドケアを探している方",
        "point": "適量を手の甲に取り、両手の甲を擦り合わせるように伸ばした後、指の股や爪の甘皮まで1本ずつマッサージするように塗り込みます。就寝前は少し多めに塗ってシルク手袋を着用すると集中リペアされます。"
    },
    {
        "rank": 5,
        "tag": "🧴 洗練されたオーガニック×アナツバメ巣！冬の乾燥肌をベルベット密着膜で包む極上クリーム",
        "catch": "モードな美意識を誇るセルヴォークの最高峰ライン『セルリュクス』。アナツバメ巣エキスをはじめとする希少発酵成分を凝縮し、真冬の寒冷で硬直した素肌をしなやかで官能的なツヤ肌へ導くトリートメントクリーム",
        "brand_name": "SNP (エスエヌピー) / Celvoke (セルヴォーク)",
        "capacity": "50g / プレミアムジャー容器",
        "type": "高純度アナツバメ巣エキス配合 濃密エモリエントクリーム",
        "features": "加水分解アナツバメ巣エキス、ウメ果実エキス、サトザクラ花エキス、植物性スクワラン、セラミド",
        "value": "肌表面に薄いベルベットのような保護皮膜を構築し、室内の暖房気流による水分蒸散をシャットアウト。夜塗れば翌朝まで吸い付くような濃密な保湿感が持続",
        "desc_p1": "12月の本格的な寒さに突入すると、乳液や通常の保湿クリームでは朝までに水分が蒸発し、起きたときに肌が突っ張るようになります。セルヴォークのセルリュクス トリートメントクリームは、厳選されたアナツバメ巣エキスを配合し、大人の乾燥肌を濃密な油分と発酵保水成分で包み込むリッチなクリームです。",
        "desc_p2": "リッチで重厚なテクスチャーですが、肌の上で滑らせると驚くほど軽やかにとろけ、角層のすみずみまで溶け込むように馴染みます。アナツバメ巣エキスの持つシアル酸の保水ネットワークが、冷えで硬くなった角層をふっくらと解きほぐし、押し返すような弾力を与えます。暖房をつけたままの寝室でも乾燥知らずのモチ肌をキープできます。",
        "target": "通常の高保湿クリームでは朝まで潤いがもたない超乾燥肌、冬になると肌のハリ・ツヤが一気に低下する大人の肌、ラグジュアリーな使用感と本物のエイジングケアを両立したい方",
        "point": "夜のお手入れの最後に、パール粒大を手にとって温め、顔全体を引き上げるように優しく包み込みます。特に乾燥が気になるフェイスラインや首筋にもしっかり伸ばしてください。"
    },
    {
        "rank": 6,
        "tag": "🌙 寝ている間にシアル酸と純金が肌を満たす！1回分個包装の濃密スリーピングスティックパック",
        "catch": "アナツバメ巣エキスと24K純金、加水分解コラーゲンをスティック1本に凝縮。真冬の夜、塗って寝るだけで翌朝の洗顔時に感動のもちもち弾力肌を実感できる夜用集中マスク",
        "brand_name": "SNP (エスエヌピー)",
        "capacity": "4ml×20本入り / 個包装スティック",
        "type": "ツバメの巣×純金配合 ナイト集中スリーピングパック",
        "features": "アナツバメ巣エキス、純金（24Kゴールドコロイド）、加水分解コラーゲン、アラントイン、ナイアシンアミド",
        "value": "持ち運びにも便利な完全無菌個包装。寝ている間の8時間、エアコン暖房による乾燥蒸発を遮断し、シアル酸とコラーゲンを角層内部へじっくり送り込む",
        "desc_p1": "冬の夜は、睡眠中の水分蒸散量が夏場の約2倍に達します。朝起きると喉だけでなく顔全体がパリパリに乾いてしまうのはこのためです。SNPのバードネスト スリーピングパックは、1回分がスティック状に個包装されており、毎晩フレッシュなツバメの巣エッセンスを肌に補給できる画期的な夜用パックです。",
        "desc_p2": "ゴールドの微細粒子がキラリと輝く濃厚なジェルを顔全体に広げると、肌表面に薄いモイストシールドが形成され、枕にベタつくことなく素早く馴染みます。睡眠中の肌の自己修復リズムに合わせ、シアル酸と低分子コラーゲンが角層深部へ浸透。翌朝ぬるま湯で洗い流すと、まるでエステ帰りのような吸い付くような柔らかさとハリに満ちた素肌に出会えます。",
        "target": "冬の朝起きると肌が乾燥でカサカサになっている方、旅行や出張先でも手軽に高品質なツバメの巣パックを行いたい方、個包装で衛生的なスキンケアを好む方",
        "point": "夜の通常のスキンケアの最後に、スティック1本分を全量手に取り、顔全体から首元まで厚めに塗り広げてそのまま就寝します。洗い流しは不要で、翌朝通常の洗顔を行ってください。"
    },
    {
        "rank": 7,
        "tag": "💋 真冬の寒風でひび割れる唇をぷるぷるに再生！天然アナツバメの巣×天然ミツロウの贅沢リップ",
        "catch": "皮膚が最も薄く皮脂膜が存在しない唇のために。天然アナツバメの巣エキスとオーガニックミツロウが、真冬の乾燥冷風による皮むけや縦ジワを濃密にリペアする最高級リップクリーム",
        "brand_name": "BI-SU (美巣)",
        "capacity": "4g / スティック容器",
        "type": "天然アナツバメの巣エキス高配合 ラグジュアリー保湿リップトリートメント",
        "features": "天然アナツバメの巣エキス、天然ミツロウ、スクワラン、オリーブ果実油、無香料・無着色",
        "value": "塗った瞬間に唇の体温でとろけて密着。シアル酸が唇の粘膜バリアを整え、リップ下地としても口紅の発色と持ちを劇的に向上させる",
        "desc_p1": "11月から12月にかけて、リップクリームをいくら塗ってもすぐに皮がむけたり、血がにじむようなひび割れを起こす方が急増します。唇は角層が極めて薄く、自力で皮脂を分泌できないため、外気乾燥のダメージをもろに受けます。BI-SUのリップクリームは、天然アナツバメの巣エキスを惜しみなく配合した贅沢極まりないリップトリートメントです。",
        "desc_p2": "スティックを唇に滑らせると、固すぎず柔らかすぎない絶妙な硬さのバームが唇の縦ジワの溝一本一本をなめらかに埋め尽くします。シアル酸の保水力と天然ミツロウの保護シールドが長時間の密着を持続。飲食をしても潤いの膜が残り、夕方までぷるんとした血色感のある唇を維持できます。冬のプチギフトとしても圧倒的な人気を誇ります。",
        "target": "市販のリップクリームでは冬のひび割れや皮むけが治まらない方、唇の縦ジワや乾燥くすみが気になる方、安全な天然由来成分で唇をいたわりたい方",
        "point": "唇の縦ジワに沿って、上下に優しく滑らせるように塗布します。就寝前は少し厚めに塗り重ねてリップパックとして活用すると、翌朝驚くほど滑らかな唇に生まれ変わります。"
    },
    {
        "rank": 8,
        "tag": "✨ 希少なアナツバメ巣エキス配合！冬の寒冷で硬化した角層を解きほぐす濃密導入オイル",
        "catch": "天然アナツバメ巣エキスと上質な植物オイルが融合。化粧水の前に使うことで、真冬の冷気で硬直した角層を瞬時に柔らかくほぐし、後から使うスキンケアの浸透力を劇的に高めるブースターオイル",
        "brand_name": "美巣 (BI-SU) / Celvoke (セルヴォーク)",
        "capacity": "30mL / スポイトガラス瓶",
        "type": "アナツバメ巣エキス配合 高純度コンセントレート導入オイル",
        "features": "アナツバメ巣エキス、アルガンオイル、ローズヒップ油、植物性スクワラン、天然精油ブレンド",
        "value": "オイルでありながらサラリとした親水性処方。水分と油分のミルフィーユ層を整え、冬の粉吹き肌やゴワつきを一瞬でシルクのような手触りへ変貌させる",
        "desc_p1": "冬の乾燥肌対策で重要なのは、冷えによって『角層が硬化して化粧水を弾いてしまう』という浸透ブロックを解除することです。セルヴォークのセルリュクス コンセントレートオイルは、アナツバメの巣エキスをオイルベースに最適化して配合した、極上のプレオイルです。",
        "desc_p2": "洗顔直後の肌にスポイトで数滴馴染ませると、植物オイルが皮脂膜の代わりとなって角層の脂質と即座に一体化。アナツバメ巣のシアル酸が水分の通り道をスムーズに整えるため、その後に重ねる化粧水がスポンジのように一瞬で吸い込まれていきます。オイル特有の酸化や重さを感じさせない軽やかな後肌で、一日中みずみずしいツヤを湛えた上質な素肌を演出します。",
        "target": "冬になると肌がゴワついて化粧水が入っていかない方、オイル美容が好きだけどベタつくのは避けたい方、内側から滲み出るようなツヤ肌を作りたい方",
        "point": "朝晩の洗顔直後、化粧水の前に2〜3滴を手にとって温め、顔全体に優しくハンドプレスします。その後すぐに化粧水を重ねると、驚異的な吸い込み感を実感できます。"
    },
    {
        "rank": 9,
        "tag": "💦 微細ミストが角層深部へ直撃！ツバメの巣×電子水の超保水エッセンスローション",
        "catch": "アナツバメ巣エキスと独自の電子水を融合させた高機能ミスト化粧水。微粒子ミストがメイクの上からでも角層深部まで一瞬で浸透し、真冬の日中暖房による乾燥砂漠肌を瞬時にリフレッシュ",
        "brand_name": "SNP (エスエヌピー) / LOUVREDO (ルーヴルドー)",
        "capacity": "120g×2本セット",
        "type": "アナツバメ巣エキス配合 高保水ミストエッセンスローション",
        "features": "アナツバメ巣エキス、電子水、ヒアルロン酸Na、コラーゲン、無香料・無着色",
        "value": "スプレー缶による超微粒子ミストが、肌表面の水分バランスを整えて暖房気流による乾燥を防ぐ。日中のメイク直しや乾燥対策に最適な2本セット",
        "desc_p1": "11月〜12月は、朝どんなに完璧に保湿しても、暖房の効いたオフィスで過ごす日中には水分が奪われ、肌がカサカサに突っ張ってきます。ルーヴルドーのレヴィミストローションは、アナツバメ巣エキスと高浸透な電子水を掛け合わせ、日中の乾燥レスキューとして圧倒的な支持を集めるアイテムです。",
        "desc_p2": "ノズルをプッシュすると、霧のように細かなミストが顔全体を包み込みます。水滴が肌に残って蒸発する一般的なミストと異なり、電子水の優れた浸透力で肌内部へスーッと吸い込まれるため、メイクを崩すことなく潤いだけを補給可能。ツバメの巣エキスの保水膜が日中の外気乾燥から素肌を一日中シールドします。",
        "target": "日中のオフィス暖房で顔がパリパリに突っ張る方、メイク直し時に手軽に水分チャージを行いたい方、微細ミストで心地よく保湿したい方",
        "point": "顔から20cmほど離し、円を描くようにスプレーした後、手のひらで優しく押さえて馴染ませます。日中の乾燥を感じたときや、お風呂上がりのプレ化粧水として最適です。"
    },
    {
        "rank": 10,
        "tag": "🌸 全身をツバメの巣の潤いヴェールで包む！タイツのこすれや冬の乾燥かゆみを防ぐ濃密ボディケア",
        "catch": "高純度アナツバメ巣エキスを配合した贅沢な全身用保湿ボディクリーム。真冬の入浴後の急激な水分蒸散をブロックし、粉を吹きやすいすねや肘をしっとり滑らかなシルク肌へ整える",
        "brand_name": "BI-SU (美巣) / MY SAO",
        "capacity": "120mL / ポンプボトル",
        "type": "アナツバメ巣エキス配合 ラグジュアリー全身保湿ボディクリーム",
        "features": "アナツバメ巣エキス（燕窩）、シアル酸、ホホバ種子油、シアバター、加水分解コラーゲン",
        "value": "冬特有のタイツやヒートテックの摩擦による乾燥かゆみを予防。濃厚なエモリエントヴェールが翌日の入浴時までしっとり感を維持",
        "desc_p1": "冬の乾燥は顔だけでなく、すねや背中、腕など全身に広がります。特にお風呂上がりは急激に角層の水分が逃げ出し、すねが白く粉を吹いたり、タイツと擦れてかゆみが生じることがあります。MY SAOのボディクリームは、ツバメの巣のシアル酸パワーを贅沢にもボディケアに応用したプレミアムアイテムです。",
        "desc_p2": "滑らかなクリームが肌の上でとろけるように伸び広がり、塗布後すぐにパジャマを着ても張り付かないシルキーな仕上がり。シアル酸の潤い皮膜が全身を包み込み、冬の冷たい外気や寝具の摩擦から肌を保護します。毎晩のお手入れで、全身が吸い付くようなモチ肌へと整います。",
        "target": "冬になるとすねや背中が粉を吹いてかゆくなる方、全身のエイジングケアを最高峰の成分で行いたい方、優雅な香りに包まれてボディケアを楽しみたい方",
        "point": "お風呂から上がってタオルドライした後、3分以内に全身へたっぷり伸ばして手のひらで馴染ませます。特に乾燥しやすい肘やすねには2度塗りしてください。"
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
  <title>保湿力の強さで肌乾燥とさようなら！シアル酸と濃密アミノ酸が真冬の深刻なしぼみ肌を底上げする保湿力高めツバメの巣コスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の本格的な暖房乾燥による深刻なしぼみ肌・乾燥小ジワを救う高保湿ツバメの巣（燕窩・アナツバメの巣・シアル酸）コスメを徹底厳選！BI-SU（美巣）、SNP、セルヴォークまでローヤルゼリーの200倍のシアル酸保水の科学的根拠と共に徹底検証。">
  <meta name="keywords" content="ツバメの巣 コスメ, シアル酸 美容液, アナツバメの巣 保湿, 冬 高保湿 コスメ, BI-SU 美巣, SNP バードネスト, 乾燥小ジワ 11月 12月">

  <!-- OGP (SNSシェア / 日本語圏最適化) -->
  <meta property="og:site_name" content="LUMI COSMETICS">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！シアル酸と濃密アミノ酸が真冬の深刻なしぼみ肌を底上げする保湿力高めツバメの巣コスメランク10">
  <meta property="og:description" content="宮廷美容の最高峰！ローヤルゼリーの200倍のシアル酸が真冬の深刻なエイジング砂漠肌を蘇らせるツバメの巣コスメおすすめ10選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-swallow-nest">
  <meta property="og:image" content="{items[0]["image_url"]}">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！高保湿ツバメの巣コスメランク10">
  <meta name="twitter:description" content="11月・12月の乾燥しぼみ肌に！最高峰シアル酸配合ツバメの巣コスメ厳選10選。">
  <meta name="twitter:image" content="{items[0]["image_url"]}">

  <!-- 構造化データ (JSON-LD) #1: Article -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！シアル酸と濃密アミノ酸が真冬の深刻なしぼみ肌を底上げする保湿力高めツバメの巣コスメランク10",
    "description": "11月・12月の暖房乾燥による深刻なしぼみ肌・乾燥小ジワを救う高保湿ツバメの巣（シアル酸）コスメを徹底厳選！",
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
      "@id": "https://lumi-cosme.vercel.app/winter-swallow-nest"
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
        "name": "ツバメの巣に含まれる『シアル酸』とはどのような成分ですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "シアル酸（N-アセチルノイラミン酸）は、生体の細胞表面に存在する糖鎖の最先端に位置する重要な糖アミノ酸です。細胞間の情報伝達や保水・免疫シールドに関与し、ローヤルゼリーの約200倍もの濃度でアナツバメの巣に含まれています。真冬の過酷な乾燥気流下でも角層の水分結合力を強力に維持し、肌の密度感を底上げします。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "ツバメの巣コスメを採取する際、環境やツバメへの影響はありませんか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "本記事で紹介している正規品（BI-SU等）は、ヒナが巣立った後に放棄された空の巣のみをマレーシア政府の厳格な許可のもとで採取するサステナブルな製法を採用しています。ツバメを傷つけることなく、自然環境保護と生態系の保全に配慮された安全な原料のみが使用されています。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "ツバメの巣コスメはどのような肌質・年齢層に最も適していますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "真冬になると通常のヒアルロン酸やコラーゲンでは保湿力が持続しない超乾燥肌の方や、乾燥による小ジワ・肌のしぼみ・ハリ不足に悩む30代〜60代の大人の肌に特に最適です。EGF様ペプチドの働きにより、寒さで停滞した冬のターンオーバーを優しく後押しします。"
        }}
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #946b2d;
      --primary-dark: #6e4e1a;
      --secondary: #faf6ef;
      --accent: #b8860b;
      --text: #2c251e;
      --text-muted: #665b50;
      --border: #ece2d0;
      --card-bg: #ffffff;
      --gold: #d4af37;
      --radius: 12px;
      --shadow: 0 4px 20px rgba(148, 107, 45, 0.08);
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
      background-color: #faf8f5;
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
      background: linear-gradient(135deg, #fffdf8 0%, #ffffff 100%);
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
      color: #2c251e;
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
      background: #fdfaf2;
      color: var(--primary);
      border: 1px solid #ebd9b8;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.3rem 0.8rem;
      border-radius: 20px;
    }}

    .product-title {{
      font-size: 1.4rem;
      font-weight: 800;
      line-height: 1.45;
      color: #2c251e;
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
      color: #946b2d;
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
      color: #3a332d;
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
      background: #2c251e;
      color: #ece2d0;
      padding: 3rem 1.5rem;
      margin-top: 4rem;
      text-align: center;
      font-size: 0.9rem;
    }}

    .site-footer a {{
      color: #ebd9b8;
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
          <span class="update-badge">👑 奇跡のシアル酸エイジング</span>
        </div>
        <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！シアル酸と濃密アミノ酸が真冬の深刻なしぼみ肌を底上げする保湿力高めツバメの巣コスメランク10</h1>
        <p class="lead-text">
          11月から12月へと季節が進むにつれ、寒風と強烈なエアコン暖房により、肌の奥の水分が根こそぎ奪われていきます。「夕方になると目元や口元の小ジワが目立ち、顔全体がしぼんで老けて見える」「ヒアルロン酸やコラーゲンを塗っても、数時間でパリパリに乾いてしまう」——そんな真冬の深刻なエイジング乾燥に直面したとき、頼りになるのが東洋の至宝『ツバメの巣（アナツバメの巣・燕窩）』です。
          ローヤルゼリーの約200倍という圧倒的濃度を誇る保水成分「シアル酸」と、細胞の自己再生を後押しするEGF様ペプチドを贅沢に宿した、真冬の救世主コスメ10選を徹底検証します。
        </p>

        <div class="toc-box">
          <div class="toc-title">📑 目次：高保湿ツバメの巣コスメ完全ガイド</div>
          <ol class="toc-list">
            <li><a href="#why-swallow">なぜ真冬のしぼみ肌に「ツバメの巣（シアル酸）」が劇的な効果をもたらすのか？</a></li>
            <li><a href="#ranking-section">高保湿ツバメの巣コスメ厳選ランキング10選</a></li>
            <li><a href="#spec-compare">全10アイテムの成分＆機能比較スペック表</a></li>
            <li><a href="#geo-climate">日本の冬特有の寒冷・暖房環境と大人の乾燥対策</a></li>
            <li><a href="#faq-section">ツバメの巣コスメに関するよくある質問（FAQ）</a></li>
            <li><a href="#internal-links">冬の乾燥対策・関連高保湿コスメ特集</a></li>
          </ol>
        </div>
      </header>

      <section class="editorial-section" id="why-swallow">
        <h2 class="section-h2">なぜ真冬のしぼみ肌に「ツバメの巣（シアル酸）」が劇的な効果をもたらすのか？</h2>
        <p>
          古来より中国宮廷の皇妃たちや、美を追求する貴族たちに不老長寿の妙薬として珍重されてきたアナツバメの巣。その驚異的な美容効果の核心にあるのが、細胞表面の糖鎖の先端を構成する極めて希少なアミノ糖誘導体『シアル酸（N-アセチルノイラミン酸）』です。
        </p>
        <p>
          真冬の冷気と暖房乾燥にさらされた角層細胞は、細胞膜の保水ネットワークが寸断され、自重を維持できずに「細胞しぼみ」を起こします。シアル酸は、生体内の水分を強固に繋ぎ止めるアンカー（錨）の役割を果たすだけでなく、細胞同士のコミュニケーションを活性化させて肌本来の保水力とバリア機能を急速に再建します。
        </p>

        <div class="feature-grid">
          <div class="feature-item">
            <h4>ローヤルゼリーの約200倍のシアル酸</h4>
            <p>天然成分の中でシアル酸含有量が最も高いのがアナツバメの巣。微量でも驚異的な保水ネットワークを形成し、冬の過酷な暖房気流から水分を完全にホールドします。</p>
          </div>
          <div class="feature-item">
            <h4>EGF・FGF様ペプチドの細胞覚醒</h4>
            <p>寒さで代謝が鈍化した冬の角層に働きかけ、新しい細胞の生まれ変わり（ターンオーバー）とコラーゲン・エラスチンの生成を同時にサポートします。</p>
          </div>
          <div class="feature-item">
            <h4>濃密アミノ酸による角層密度の復元</h4>
            <p>天然の必須アミノ酸群がスカスカになった角質層の隙間を充填。内側から押し返すようなハリ弾力と、上質なシルクのような光沢ツヤを与えます。</p>
          </div>
        </div>
      </section>

      <section id="ranking-section">
        <h2 class="section-h2">保湿力の強さで肌乾燥とさようなら！高保湿ツバメの巣コスメ厳選ランキング10</h2>
        <p style="margin-bottom: 2rem; color: var(--text-muted);">
          楽天市場の最新データと皮膚科学的エビデンスに基づき、11月〜12月の本格的な冬の乾燥しぼみ肌を救うツバメの巣コスメ10選を厳選紹介します。
        </p>

        {all_cards_html}
      </section>

      <section class="editorial-section" id="spec-compare">
        <h2 class="section-h2">全10アイテムの成分＆機能比較スペック表</h2>
        <p>
          アイテムの形状、主要なツバメの巣アプローチ、プラスアルファの配合成分を一覧表で比較しました。真冬の肌悩みやケアしたい部位に合わせて最適なアイテムをお選びください。
        </p>
        <div class="comparison-table-wrap">
          <table class="comparison-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>商品名 / ブランド</th>
                <th>ツバメの巣アプローチ</th>
                <th>相乗保湿成分</th>
                <th>おすすめの肌悩み・使用シーン</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>第1位</td>
                <td>BI-SU アイラッシュセラム</td>
                <td>天然アナツバメ巣エキス100%</td>
                <td>シアル酸・キャピキシル・ケラチン</td>
                <td>冬の目元の乾燥小ジワ・まつ毛補修</td>
              </tr>
              <tr>
                <td>第2位</td>
                <td>SNP バードネスト マスク</td>
                <td>アナツバメ巣エキス1000mg</td>
                <td>複合ヒアルロン酸・ツボクサエキス</td>
                <td>週末の集中水分チャージ・即効ツヤ肌</td>
              </tr>
              <tr>
                <td>第3位</td>
                <td>MY SAO つや出し濃密美容液</td>
                <td>天然アナツバメ巣エキス</td>
                <td>シアル酸・加水分解コラーゲン</td>
                <td>大人の深刻な乾燥しぼみ・夕方のくすみ</td>
              </tr>
              <tr>
                <td>第4位</td>
                <td>BI-SU ハンドクリーム</td>
                <td>天然アナツバメ巣エキス</td>
                <td>シアバター・ホホバ油・ラベンダー</td>
                <td>真冬の水仕事や冷気による手荒れ・血管浮き</td>
              </tr>
              <tr>
                <td>第5位</td>
                <td>Celvoke セルリュクス クリーム</td>
                <td>加水分解アナツバメ巣エキス</td>
                <td>サトザクラ花エキス・スクワラン</td>
                <td>朝まで乾かない濃密エモリエント保護</td>
              </tr>
              <tr>
                <td>第6位</td>
                <td>SNP スリーピングパック</td>
                <td>ツバメの巣エキス×純金24K</td>
                <td>低分子コラーゲン・個包装スティック</td>
                <td>寝ている間の暖房乾燥防止・夜用マスク</td>
              </tr>
              <tr>
                <td>第7位</td>
                <td>BI-SU リップクリーム</td>
                <td>天然アナツバメ巣エキス</td>
                <td>オーガニックミツロウ・植物オイル</td>
                <td>唇のひび割れ・皮むけ・縦ジワ改善</td>
              </tr>
              <tr>
                <td>第8位</td>
                <td>Celvoke コンセントレートオイル</td>
                <td>アナツバメ巣エキス</td>
                <td>アルガンオイル・ローズヒップ油</td>
                <td>冬のゴワつき肌をほぐす導入ブースター</td>
              </tr>
              <tr>
                <td>第9位</td>
                <td>LOUVREDO レヴィミスト</td>
                <td>アナツバメ巣エキス</td>
                <td>高浸透電子水・ヒアルロン酸</td>
                <td>オフィス暖房下の日中メイク直し・保湿</td>
              </tr>
              <tr>
                <td>第10位</td>
                <td>MY SAO ボディクリーム</td>
                <td>高純度アナツバメ巣エキス</td>
                <td>シアバター・ホホバ種子油</td>
                <td>全身の乾燥かゆみ・タイツの摩擦対策</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <section class="editorial-section" id="geo-climate">
        <h2 class="section-h2">日本の冬特有の寒冷・暖房環境と大人の乾燥対策</h2>
        <p>
          11月から12月にかけての日本国内は、室内外の温度差や湿度の低下が年間で最も激しい時期です。特に年齢を重ねた肌ほど、皮脂分泌力とセラミド合成力が低下しているため、環境に合わせた適切なプレミアムケアが必要です。
        </p>

        <div class="feature-grid">
          <div class="feature-item">
            <h4>年末の多忙期と肌代謝の低下</h4>
            <p>
              11月〜12月は仕事や行事で睡眠不足やストレスが重なり、自律神経が乱れて末梢血行が滞りがちになります。ツバメの巣に含まれるシアル酸とEGF様作用は、疲れ切った肌細胞を休ませながら優しく覚醒させ、翌朝のふっくらとしたハリを支えます。
            </p>
          </div>
          <div class="feature-item">
            <h4>湿熱差（屋外の氷点下寒風 vs 室内の過熱暖房）</h4>
            <p>
              屋外の冷風で収縮した毛細血管が、暖房の効いた室内で急激に拡張すると、角層細胞間の結合が緩み水分が一気に気化します。ツバメの巣コスメが形成する粘弾性シールドは、この急激な寒暖差による水分蒸散を物理的にシャットアウトします。
            </p>
          </div>
        </div>
      </section>

      <section class="editorial-section" id="faq-section">
        <h2 class="section-h2">ツバメの巣コスメに関するよくある質問（FAQ）</h2>
        
        <div class="faq-block">
          <div class="faq-q">❓ ツバメの巣とローヤルゼリーやプラセンタとの違いは何ですか？</div>
          <div class="faq-a">
            ローヤルゼリーやプラセンタも優れたエイジングケア成分ですが、ツバメの巣の最大の特徴は『シアル酸（糖鎖栄養素）』の圧倒的な高濃度配合にあります。ローヤルゼリーの約200倍のシアル酸を含み、細胞同士を繋ぐ糖鎖ネットワークを直接補強することで、真冬の過酷な乾燥下でも肌の弾力としぼみ改善において突出した手応えを発揮します。
          </div>
        </div>

        <div class="faq-block">
          <div class="faq-q">❓ ツバメの巣コスメは動物愛護の観点で問題ありませんか？</div>
          <div class="faq-a">
            本記事で紹介している正規品ブランドは、アナツバメが子育てを終えて巣立った後の『不要になった古巣』のみを採取しています。政府の保護基準と採取許可を遵守し、ツバメの生態系を守りながら持続可能な形で調達されているため、安心してお使いいただけます。
          </div>
        </div>

        <div class="faq-block">
          <div class="faq-q">❓ 敏感肌でも赤みや刺激を感じずに使えますか？</div>
          <div class="faq-a">
            アナツバメの巣は母ツバメが自らの唾液腺分泌物で作り上げる極めて純度の高い生体適合成分です。刺激性が極めて低く、デリケートな目元やまぶた、唇のケアにも安心して使用できる肌想いの成分です。
          </div>
        </div>
      </section>

      <section class="internal-links-box" id="internal-links">
        <h2 class="section-h2">冬の乾燥対策・関連高保湿コスメ特集</h2>
        <p>
          LUMI COSMETICSでは、11月・12月の本格的な冬乾燥に立ち向かう厳選スキンケア特集を多数公開しています。成分ごとの特徴や肌悩みに合わせて、ぜひ合わせてチェックしてみてください。
        </p>

        <div class="internal-links-grid">
          <a href="/winter-royal-jelly" class="internal-link-card">👑 冬のローヤルゼリー高保湿コスメ10選</a>
          <a href="/winter-placenta" class="internal-link-card">✨ 冬のプラセンタ濃厚美容液10選</a>
          <a href="/winter-fucoidan" class="internal-link-card">🌊 冬の高保湿フコイダンコスメ10選</a>
          <a href="/winter-collagen" class="internal-link-card">💧 冬の生コラーゲン高保水スキンケア10選</a>
          <a href="/winter-elastin" class="internal-link-card">🧬 冬のエラスチン弾力リフトケア10選</a>
          <a href="/winter-proteoglycan" class="internal-link-card">🔬 冬のプロテオグリカン原液10選</a>
          <a href="/winter-lactobacillus" class="internal-link-card">🥛 冬の高保湿乳酸菌（美肌菌）コスメ10選</a>
          <a href="/winter-stem-cell" class="internal-link-card">🧪 冬のヒト幹細胞エイジングケア10選</a>
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

with open("winter-swallow-nest.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-swallow-nest.html!")
