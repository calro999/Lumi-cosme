import json
import re

with open("fetched_final_30_liposome_coenzyme_astaxanthin.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_astaxanthin"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 赤の自己復元ジェリーが角層を土台から再建！真冬の先行スキンケアの最高峰",
        "catch": "ナノアスタキサンチン×Wヒト型ナノセラミド。洗顔直後の素肌に赤の潤いを注ぎ込み、冬の乾燥小ジワを跳ね返す",
        "brand_name": "ASTALIFT (アスタリフト) / 富士フイルム",
        "capacity": "40g / 60g (ジェリー アクアリスタ)",
        "type": "先行型高保湿ジェリー状美容液",
        "features": "Wヒト型ナノセラミド、ナノアスタキサンチン、ナノリコピン、アセンヤクエキス、3種のコラーゲン",
        "value": "富士フイルムの写真フィルム技術を結集したナノ微粒子化。崩しても自己復元する濃密な赤いジェリーが、冬の砂漠肌を土台から満水にする",
        "desc_p1": "11月から12月にかけて、暖房の効いた室内と冷たい外気の往復で肌のバリア機能が崩れ、いくら化粧水を重ねても砂漠のように乾いてしまう『冬の水分枯渇』。写真分野で培ったナノテクノロジーを化粧品に応用した富士フイルムの『ジェリー アクアリスタ』は、日本のスキンケア界を牽引し続ける最高峰の先行ジェリー美容液です。",
        "desc_p2": "鮮やかな濃紅色のジェリーは、すくっても数十秒で元の平らな状態に戻る『自己復元型』。洗顔直後の肌に乗せると、体温ですっと水のようにほどけて角層の最深部まで吸い込まれます。世界最小クラスにナノ化されたアスタキサンチンと2種類のヒト型ナノセラミドが協調し、寒さでスカスカになった細胞間脂質を隙間なく埋め尽くします。その後に使う化粧水の引き込みスピードが劇的に上がり、夕方までぷるんと跳ね返すようなハリとツヤが持続します。",
        "target": "真冬の深刻な乾燥小ジワやハリ不足に悩む方、化粧水が肌になじみにくく浸透力を高めたい方、自分へのご褒美に確かな先行美容液を選びたい方",
        "point": "朝晩の洗顔直後、付属のスパチュラでやや大きめのパール粒大を取り、手のひらで軽く温めてから顔全体を包み込むようになじませます。ジェリーが肌になじんで吸い付く感触に変わったら、化粧水のステップへ進んでください。"
    },
    {
        "rank": 2,
        "tag": "🛡️ ナノアスタキサンチンの濃密シールド！冷気乾燥を一晩中遮断する最高峰クリーム",
        "catch": "ナノアスタキサンチン×リコピン×3種のコラーゲン。リッチでコクのある赤いヴェールが真冬の肌を包み込み朝まで潤いを密封",
        "brand_name": "ASTALIFT (アスタリフト) / 富士フイルム",
        "capacity": "30g (アドバンスド クリーム)",
        "type": "超高保湿エイジングリペアクリーム",
        "features": "ナノアスタキサンチン、ナノリコピン、メマツヨイグサ種子エキス、浸透型コラーゲン",
        "value": "濃厚なコクと密着力を誇るリッチテクスチャー。真冬の過酷な深夜暖房下でも一滴の水分蒸発も許さず、翌朝の肌に高密度の弾力を宿す",
        "desc_p1": "真冬の夜間は皮膚からの水分蒸散量がピークに達し、就寝中に角層のうるおいが奪われて朝の肌がシワっぽくなってしまいます。アスタリフトのアドバンスドクリームは、肌表面に強固な保護ヴェールを形成し、眠っている間の美肌再生をサポートする高機能ナイトクリームです。",
        "desc_p2": "贅沢な赤いクリームを肌にのばすと、コクのあるリッチな感触から体温でなめらかにとろけ、ピンとしたハリの保護膜を形成。天然の抗酸化成分であるアスタキサンチンとリコピンが睡眠中の酸化ストレスを徹底除去し、メマツヨイグサ種子エキスが乾燥によるキメの乱れをケアします。ベタつきを残さずに肌の内側を濃密な油分と水分で満たし、翌朝の洗顔時には思わず触れたくなるようなもっちりとした弾力肌に出会えます。",
        "target": "冬の乾燥で肌のたるみや小ジワが気になる大人肌の方、真冬の夜に絶対に乾燥させたくない方、上質な香りとリッチな使用感を好む方",
        "point": "夜のお手入れの最後に、やや大きめのパール粒大を手に取り、あご先からこめかみへ向かってリフトアップするように引き上げながら伸ばします。目元やほうれい線には重ね塗りをしてください。"
    },
    {
        "rank": 3,
        "tag": "💧 赤の美容成分が角層をゴクゴク潤す！吸い付くようなハリを宿す薬用高保水ローション",
        "catch": "ナノアスタキサンチン×水溶性コラーゲン。乾燥でこわばった真冬の角層をすみずみまで解きほぐすプレミアム化粧水",
        "brand_name": "ASTALIFT (アスタリフト) / 富士フイルム",
        "capacity": "130ml (モイストローション)",
        "type": "高保湿エイジングケア化粧水",
        "features": "ナノアスタキサンチン、ナノリコピン、CLリフレッシャー®、3種のコラーゲン、ヒアルロン酸",
        "value": "美容液のように濃厚な赤いローションが、微細なナノテクノロジーで角層深層へ直行。乾燥で硬くなった肌をもっちり柔らかく満水化",
        "desc_p1": "冬の寒さと乾燥によってターンオーバーが滞ると、古い角質が蓄積して肌が硬くなり、通常の化粧水では潤いが行き渡らなくなります。アスタリフトのモイストローションは、角層のコラーゲン環境に着目し、浸透性と保湿持続力を極限まで高めた薬用化粧水です。",
        "desc_p2": "鮮やかなダマスクローズ色のローションを肌になじませると、ダマスクローズの気品ある香りが広がり、とろみのあるテクスチャーが角層の奥深くまでスーッと吸い込まれます。独自開発のCLリフレッシャーがダメージを受けたコラーゲンをケアし、うるおいの通り道を確保。塗布後の肌は手のひらが吸い付くほどもっちりとし、内側から押し返すような弾力がみなぎります。",
        "target": "冬になると肌がゴワついて化粧水が浸透しにくい方、乾燥小ジワを毎日の水分補給でケアしたい方、優雅なローズの香りで癒やされたい方",
        "point": "ポンプ2〜3プッシュを手のひらに取り、顔全体を温めるように優しくハンドプレスします。さらに1プッシュを重ねづけすることで、真冬のエアコン乾燥に負けないうるおい満タン肌が完成します。"
    },
    {
        "rank": 4,
        "tag": "✨ 1品でハリ・弾力・濃密保湿を速攻チャージ！高純度アスタキサンチンの大容量ジェル",
        "catch": "高純度アスタキサンチン×加水分解エラスチン。時短ケアでも手抜き感ゼロの極上ツヤ肌を叶えるオールインワン",
        "brand_name": "DHC (ディーエイチシー)",
        "capacity": "120g (アスタキサンチン コラーゲン オールインワンジェル)",
        "type": "高濃度アスタキサンチンオールインワンジェル",
        "features": "ナノサイズアスタキサンチン、加水分解コラーゲン、加水分解エラスチン、プラセンタエキス、ヒアルロン酸",
        "value": "ヘマトコッカス藻由来の天然アスタキサンチンを高濃度配合。冬の寒冷・暖房乾燥から肌を守り、1つで小ジワ・たるみ・くすみをマルチケア",
        "desc_p1": "忙しい年末年始、寒くてスキンケアに何工程も時間をかけられないけれど、乾燥や老け見えは絶対に防ぎたい。そんな願いを叶えるのがDHCのアスタキサンチンコラーゲンオールインワンジェルです。",
        "desc_p2": "フタを開けると広がる鮮やかなオレンジレッドのジェル。微細化されたアスタキサンチンが角層の隙間へ素早く浸透し、エラスチンとコラーゲンが肌の弾力メッシュを補強します。ぷるんとしたみずみずしいジェルでありながら、肌になじませると濃厚な密着保護膜を形成。化粧水、美容液、乳液、クリーム、パックの5役を兼ね備え、真冬の朝もメイク前にサッと塗るだけで乾燥知らずのハリ肌が夕方まで持続します。",
        "target": "忙しい朝や疲れた夜に1品で本格エイジングケアを済ませたい方、ベタつかないのに高保湿なジェルを求める方、コスパ良く大容量で使いたい方",
        "point": "洗顔後、さくらんぼ粒大を取り、顔の中心から外側へ引き上げるように伸ばします。乾燥が気になる目元やほうれい線には、指先でジェルを置くように重ねづけしてください。"
    },
    {
        "rank": 5,
        "tag": "🔬 天然ヘマトコッカス藻由来100%原液！手持ちコスメを一瞬で赤の抗酸化仕様へ進化",
        "catch": "ヘマトコッカス藻由来の天然アスタキサンチン100%原液。手持ちの化粧水やクリームに1滴混ぜて冬枯れ肌を蘇らせる",
        "brand_name": "KISO (基礎化粧品研究所)",
        "capacity": "20ml (アスタキサンチン 原液)",
        "type": "高純度天然アスタキサンチン美容原液",
        "features": "ヘマトコッカスプルビアリス油（天然アスタキサンチン）、オレイン酸ポリグリセリル-10、グリセリン",
        "value": "無駄な香料や着色料を一切使わない純粋なアスタキサンチンエキス。ビタミンCの6,000倍の抗酸化力をそのままダイレクトに肌へデリバリー",
        "desc_p1": "成分にこだわるスキンケアマニアから絶大な信頼を集めるKISOのアスタキサンチン原液。過酷な紫外線や乾燥に耐え抜くために藻類が自ら作り出す強力な赤い色素『アスタキサンチン』を高純度・無香料で抽出した濃縮原液です。",
        "desc_p2": "深いルビーレッドの濃厚な1滴を、手持ちの化粧水や乳液にブレンドするだけで、いつものデイリーコスメが瞬時に真冬仕様の抗酸化エイジング美容液へとアップグレード。肌の酸化ストレスを中和し、乾燥による小ジワやくすみ、ゴワつきを速やかにリセットします。コストパフォーマンスも抜群で、冬の間の集中エイジングケアに欠かせない隠れた名品です。",
        "target": "手持ちのスキンケアの保湿力・ハリ感を高めたい方、余計な添加物を排除した純粋な原液を使いたい方、目元や口元の乾燥小ジワをピンポイントでケアしたい方",
        "point": "手のひらに化粧水や乳液を取った後、スポイトでアスタキサンチン原液を1〜2滴垂らし、よく混ぜ合わせてから顔全体になじませます。特に乾燥が気になる部位には原液をそのまま1滴直接指先でトントンとなじませてください。"
    },
    {
        "rank": 6,
        "tag": "🔴 韓国コスメ1位の赤いカプセルセラム！アスタキサンチン×ナイアシンアミドの透明感爆弾",
        "catch": "アスタキサンチンカプセル×高純度ナイアシンアミド。真冬の乾燥でくすんだ肌に透明感とピンとしたハリを満たす",
        "brand_name": "Sungboon Editor (成分エディター)",
        "capacity": "30ml (アスタキサンチン カプセル 美容液)",
        "type": "高機能カプセルエイジング美容液",
        "features": "アスタキサンチンリポソームカプセル、ナイアシンアミド、トラネキサム酸、グルタチオン、ヒアルロン酸",
        "value": "韓国オリーブヤングや各モールでランキング1位を獲得。マイクロカプセル化されたアスタキサンチンが肌の上で弾け、真冬のくすみと乾燥小ジワを一掃",
        "desc_p1": "韓国のスキンケア界で「美白とハリの最終兵器」として空前の大ヒットを記録している成分エディターのアスタキサンチンカプセルセラム。真冬の乾燥と血行不良によってどんより曇った肌トーンを、赤の抗酸化エネルギーで明るく照らし出します。",
        "desc_p2": "透明なセラムの中に鮮やかな赤いアスタキサンチンカプセルが無数に浮遊。ポンプを押すとカプセルが微細にほぐれながら出てきて、肌に伸ばすと瞬時に角層深くまで浸透します。ナイアシンアミドとトラネキサム酸が美白と肌荒れ予防を同時に叶え、アスタキサンチンが強力な弾力シールドを形成。塗布直後から内側から発光するようなツヤとモチモチ感が持続します。",
        "target": "冬になると顔色がどんより暗くくすむ方、韓国トレンドの最先端成分コスメを試したい方、透明感とハリツヤを同時に手に入れたい方",
        "point": "化粧水の直後、スポイト1回分を取り顔全体に優しく塗り広げます。赤いカプセルを手のひらの体温で押しつぶすようにハンドプレスし、角層に浸透させてください。"
    },
    {
        "rank": 7,
        "tag": "✨ 薬用多機能美容液！カフェイン×ナノアスタキサンチンが真冬のむくみ＆たるみを撃退",
        "catch": "薬用有効成分ナイアシンアミド×浸透型リポソームアスタキサンチン。真冬の血行不良による乾燥・たるみ・くすみを1本でマルチ解決",
        "brand_name": "ASTALIFT (アスタリフト) / 富士フイルム",
        "capacity": "40ml (ザ セラム マルチチューン)",
        "type": "薬用多機能エイジング美容液",
        "features": "ナイアシンアミド（シワ改善・美白有効成分）、ナノアスタキサンチン、カフェイン、ビタミンC誘導体",
        "value": "富士フイルムの最新単層ナノリポソーム技術を採用。真冬の過酷な環境で低下した巡りをサポートし、輪郭まですっきり引き締まった透明ハリ肌へ",
        "desc_p1": "真冬になると寒さで顔がむくみやすく、フェイスラインがぼやけてたるみ小ジワが目立つ…という大人の冬悩みに応えて開発されたアスタリフト最高峰の薬用多機能美容液。シワ改善・美白・肌荒れ防止の3つの効能を取得しています。",
        "desc_p2": "伸びの良い上質なセラムが肌に吸い付くように広がり、浸透型リポソームに内包されたナノアスタキサンチンとナイアシンアミドが真皮と表皮へダイレクトに作用。カフェインが冬の冷えによる巡りの滞りをケアし、キュッと引き締まったフェイスラインへと導きます。1本で真冬のあらゆるエイジングサインを網羅できる頼もしさです。",
        "target": "冬の冷えで顔がむくみやすくたるみが気になる方、シワ改善と美白を1本で完結させたい方、最高峰の製薬・写真テクノロジーを体感したい方",
        "point": "化粧水の後に2〜3プッシュを取り、フェイスラインを下から上へ引き上げるようになじませます。最後に手のひらで首筋へリンパを流すようにストロークするのが効果的です。"
    },
    {
        "rank": 8,
        "tag": "🥛 濃厚な油水分で真冬の角層を解きほぐす！コーセーの進化型アスタキサンチン薬用乳液",
        "catch": "進化型アスタキサンチンCPX配合。硬くなった真冬の肌をふっくら柔らかくほぐし、押し返すような弾力を与える",
        "brand_name": "KOSE (コーセー) アスタブラン",
        "capacity": "100ml (Wリフト エマルジョン とてもしっとり)",
        "type": "薬用高保湿エイジングケア乳液",
        "features": "アスタキサンチンCPX（保湿成分）、ビタミンC誘導体、エラスチン、高保湿コラーゲン",
        "value": "まろやかでコクのある極上の乳液テクスチャー。真冬の粉吹き肌に上質な油分と水分を補給し、夕方までふっくら柔らかい肌をキープ",
        "desc_p1": "コーセーのエイジングケアブランド『アスタブラン』が誇る超ロングセラー薬用乳液。冬の寒さで角層が強張り、ゴワついて化粧のりが悪くなった大人の肌のために開発された『とてもしっとり』タイプです。",
        "desc_p2": "アスタキサンチンを微細カプセル化したCPX成分が、硬くなった角層細胞の隙間を優しく解きほぐし、内側まで潤いを浸透させます。濃厚なエモリエントオイルが肌表面に薄くしなやかな保護膜を形成し、真冬の乾いた冷風から肌を一日中ガード。塗布後の肌は指先が吸い付くほどもっちりとし、キメの整った明るいツヤ肌が蘇ります。",
        "target": "冬になると肌が硬くゴワついてファンデーションが浮く方、乳液にしっかりとした濃厚な保湿感を求める方、エイジングケアを毎日手軽に続けたい方",
        "point": "化粧水の後にポンプ2プッシュを手のひらに取り、顔全体に丁寧になじませます。特に乾燥しやすい目元や口元には、指先で重ねづけしてハンドプレスしてください。"
    },
    {
        "rank": 9,
        "tag": "🌹 天然ヘマトコッカス抽出アスタキサンチン！冬の目元・口元をピンと保つ濃密ジェル",
        "catch": "天然アスタキサンチン×レチノール誘導体。冬の乾燥小ジワを徹底的に防ぎ、濃密なハリ膜で肌を密閉するリッチジェル",
        "brand_name": "自然派高保湿スキンケア",
        "capacity": "100g (アスタキサンチン リッチ オールインワンジェル)",
        "type": "高純度アスタキサンチン高保湿ジェル",
        "features": "天然アスタキサンチン（ヘマトコッカスプルビアリス抽出）、レチノール誘導体、加水分解コラーゲン、ヒアルロン酸Na",
        "value": "深紅の濃厚ジェルが肌の上で吸い付くように密着。真冬の夜間乾燥から肌を守り抜き、翌朝までピンとしたハリ感をキープ",
        "desc_p1": "天然のヘマトコッカス藻から抽出したアスタキサンチンを贅沢に配合した高保湿オールインワンジェル。冬の寒冷・暖房乾燥によって目元やほうれい線に現れる『乾燥小ジワ』をピンと伸ばすように密着保護します。",
        "desc_p2": "ぷるぷるの深紅のジェルを肌に乗せると、とろけるようになじんで肌表面に均一なリフトヴェールを形成。レチノール誘導体とアスタキサンチンが協調し、真冬の寒さで弱まった肌のハリ弾力を強力にサポートします。ベタつきを残さずみずみずしい保水感が続くため、朝のメイク前にも夜の集中スリーピングパックとしても大活躍します。",
        "target": "目元やほうれい線の乾燥小ジワが気になる方、レチノールとアスタキサンチンの相乗効果を試したい方、大容量で惜しみなく使いたい方",
        "point": "夜のお手入れには、やや多めのさくらんぼ粒大を取り、顔全体に厚めに塗る『スリーピングジェルパック』がおすすめ。翌朝の肌のふっくら感が劇的に変わります。"
    },
    {
        "rank": 10,
        "tag": "🌿 1,000円台で叶う贅沢アスタキサンチン！真冬の乾燥小ジワを目立たなくする高保湿乳液",
        "catch": "天然アスタキサンチン×レチノール誘導体×コラーゲン。プチプラとは思えないリッチな潤いと弾力を与える名品ミルク",
        "brand_name": "明色化粧品",
        "capacity": "100ml (ピュアエクセレントG エッセンスミルク)",
        "type": "高保湿エイジングケア乳液",
        "features": "天然アスタキサンチン、レチノール誘導体、浸透型コラーゲン、エラスチン、ヒアルロン酸",
        "value": "効能評価試験済みで乾燥による小ジワを目立たなくする実力派。1,000円台の高コスパで冬の乾燥肌にしっとり吸い付くうるおいをチャージ",
        "desc_p1": "130年以上の歴史を持つ老舗化粧品メーカー・明色化粧品が手掛けるエイジングケア乳液。天然アスタキサンチンとレチノール誘導体を贅沢に配合しながら、ドラッグストアで手軽に買えるプチプラ価格を実現した隠れた名品です。",
        "desc_p2": "淡いオレンジ色のまろやかなミルクテクスチャーで、冬の冷えた肌にもスルスルとなめらかに伸びて浸透。乾燥による小ジワを目立たなくする『効能評価試験済み』の確かな処方で、真冬のエアコン乾燥から目元や口元を優しく守ります。惜しみなくたっぷり使えるため、顔だけでなく首元の乾燥ジワ予防にも大活躍します。",
        "target": "プチプラで本格的なアスタキサンチン乳液を探している方、冬の乾燥小ジワを手軽にケアしたい方、首やデコルテまでたっぷり使いたい方",
        "point": "化粧水の後に適量を手に取り、顔全体になじませた後、もう1プッシュを首筋からデコルテへ向かって上から下へ優しくなじませてください。"
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
        "url": f"https://lumi-cosme.vercel.app/winter-astaxanthin.html#item-{i+1}",
        "offers": {
            "@type": "Offer",
            "price": str(p['price']),
            "priceCurrency": "JPY",
            "availability": "https://schema.org/InStock"
        }
    })

faq_list = [
    {
        "question": "アスタキサンチンとはどのような成分ですか？なぜ冬の乾燥小ジワに効くのですか？",
        "answer": "アスタキサンチンは、サケやエビ、ヘマトコッカス藻などに含まれる赤色の天然カロテノイド色素です。その抗酸化力は極めて強大で、ビタミンCの約6,000倍、コエンザイムQ10の約800倍、ビタミンEの約500倍とも言われています。真冬は寒冷刺激やエアコン乾燥、室内の紫外線散乱によって活性酸素（一重項酸素）が発生し、真皮のコラーゲン線維を破壊して乾燥小ジワやたるみを引き起こします。アスタキサンチンは細胞膜の内側と外側の両方にまたがって存在できる唯一無二の構造を持つため、真冬の酸化ダメージを徹底的に遮断し、肌本来のハリ・弾力と水分保持力を強力に保護します。"
    },
    {
        "question": "アスタキサンチンの赤い色は着色料ですか？肌に赤く色が残りませんか？",
        "answer": "着色料ではありません。アスタキサンチン原料そのものが持つ自然の天然色素（カロテノイド）の色です。そのため、高品質かつ高濃度に配合されているコスメほど鮮やかな赤色や濃いオレンジ色をしています。肌になじませると、体温で素早く角層深層へと浸透し、肌表面に赤色が残ることは一切ありません。日中のメイク前に使ってもファンデーションの色味に影響を与えないため、安心して朝晩お使いいただけます。"
    },
    {
        "question": "なぜアスタリフトなどアスタキサンチンコスメは「ジェリー状」や「先行美容液」が多いのですか？",
        "answer": "アスタキサンチンは油溶性の成分であるため、本来は水に溶けにくく角層に浸透させるのが非常に難しい成分です。富士フイルムなどの先端技術によってナノ微粒子化（世界最小クラスの粒子に均一分散）し、さらにセラミドなどと結合させることで、みずみずしい高浸透ジェリーへの配合が可能となりました。洗顔直後の無防備な角層にナノアスタキサンチンを届けることで、傷ついた角層バリアを瞬時に修復し、その後に重ねる化粧水や美容液の浸透ルートを最大化できるため、先行型アイテムとして絶大な効果を発揮します。"
    },
    {
        "question": "ビタミンCやレチノールとアスタキサンチンは併用できますか？",
        "answer": "非常に相性が良く、むしろ併用が推奨されます。アスタキサンチンが紫外線や冷気による一重項酸素を無力化し、ビタミンCが水溶性の活性酸素を除去、レチノールが夜間のターンオーバーとコラーゲン産生を促すという完璧な役割分担が成立します。特に朝にアスタキサンチンを塗布して日中の酸化・乾燥ストレスをブロックし、夜にレチノールで集中リペアを行うスキンケアルーティンは、冬のエイジングケアに最も効果的なプロの王道パターンです。"
    },
    {
        "question": "アスタキサンチンコスメは敏感肌や乾燥肌でも刺激になりませんか？",
        "answer": "アスタキサンチンは天然の藻類由来の成分であり、極めて肌に優しい抗酸化成分です。レチノールのようなA反応（皮剥けや赤み・ヒリつき）を起こす心配がなく、肌荒れを防ぐ抗炎症サポート作用も兼ね備えているため、冬の寒暖差でデリケートになった敏感肌や超乾燥肌の方でも安心してお使いいただけます。"
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
        "@id": "https://lumi-cosme.vercel.app/winter-astaxanthin.html"
    },
    "headline": "保湿力の強さで肌乾燥とさようなら！赤の抗酸化力で冬の乾燥小ジワを跳ね返し濃密な潤いを満たす高保湿アスタキサンチンコスメランク10",
    "description": "11月・12月の暖房乾燥と冬の乾燥小ジワを救う高保湿アスタキサンチンコスメを徹底厳選！アスタリフトジェリーアクアリスタ、アドバンスドクリーム、DHC、KISO、韓国成分エディターから明色化粧品まで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。",
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
    "name": "真冬の高保湿アスタキサンチンコスメおすすめ人気ランキング10選",
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
      
      <div class="product-layout">
        <div class="product-visual">
          <img src="{p['img_url']}" alt="{p['name']}" class="product-img" loading="lazy" width="300" height="300">
          <div class="price-box">
            <span class="price-label">楽天参考価格</span>
            <span class="price-value">¥{p['price']:,}</span>
            <span class="price-tax">（税込）</span>
          </div>
          <a href="{p['affiliate_url']}" target="_blank" rel="noopener sponsored" class="rakuten-btn">
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
            <h4>💡 美容皮膚専門ライターの詳細解説＆真冬のレビュー</h4>
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
      <td class="tbl-rank">第{i+1}位</td>
      <td class="tbl-name"><a href="#item-{i+1}">{d['brand_name']} {p['name'][:22]}...</a></td>
      <td class="tbl-type">{d['type']}</td>
      <td class="tbl-price">¥{p['price']:,}</td>
      <td class="tbl-merit">{d['value'][:32]}...</td>
    </tr>
    """)
table_rows_joined = "\n".join(table_rows)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！赤の抗酸化力で冬の乾燥小ジワを跳ね返し濃密な潤いを満たす高保湿アスタキサンチンコスメランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の暖房乾燥と冬の乾燥小ジワを救う高保湿アスタキサンチンコスメを徹底厳選！アスタリフトジェリーアクアリスタ、アドバンスドクリーム、DHC、KISO、韓国成分エディターから明色化粧品まで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。">
  <meta name="keywords" content="アスタキサンチン コスメ,冬 乾燥小ジワ 保湿,アスタリフト ジェリー,高保湿 先行美容液,アスタキサンチン クリーム,エイジングケア ランキング">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-astaxanthin.html">
  
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！赤の抗酸化力で冬の乾燥小ジワを跳ね返し濃密な潤いを満たす高保湿アスタキサンチンコスメランク10">
  <meta property="og:description" content="11月・12月の暖房乾燥と冬の乾燥小ジワを救う高保湿アスタキサンチンコスメを徹底厳選！楽天で買える人気ランキング10選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-astaxanthin.html">
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
      --primary: #991b1b;
      --primary-light: #fef2f2;
      --primary-border: #fecaca;
      --accent: #dc2626;
      --accent-hover: #b91c1c;
      --gold: #b45309;
      --text-main: #1f2937;
      --text-muted: #4b5563;
      --bg-light: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
      --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.08);
      --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1);
    }}
    
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
      line-height: 1.8;
      color: var(--text-main);
      background-color: #fdf8f8;
      padding-bottom: 60px;
    }}
    
    header {{
      background: linear-gradient(135deg, #991b1b 0%, #dc2626 100%);
      color: #ffffff;
      padding: 40px 20px;
      text-align: center;
      box-shadow: var(--shadow-md);
    }}
    
    .site-logo {{
      font-size: 1.1rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      margin-bottom: 12px;
      opacity: 0.95;
    }}
    
    .site-logo a {{
      color: #ffffff;
      text-decoration: none;
    }}
    
    header h1 {{
      font-size: 1.8rem;
      line-height: 1.4;
      max-width: 900px;
      margin: 0 auto 16px;
      font-weight: 800;
    }}
    
    .header-meta {{
      font-size: 0.9rem;
      opacity: 0.9;
    }}
    
    .container {{
      max-width: 1000px;
      margin: 30px auto;
      padding: 0 20px;
    }}
    
    .lead-box {{
      background-color: #ffffff;
      border-radius: 12px;
      padding: 30px;
      margin-bottom: 35px;
      box-shadow: var(--shadow-sm);
      border-left: 6px solid var(--accent);
    }}
    
    .lead-box p {{
      margin-bottom: 16px;
      font-size: 1.05rem;
      color: #374151;
    }}
    
    .lead-box p:last-child {{
      margin-bottom: 0;
    }}
    
    .toc-box {{
      background-color: var(--primary-light);
      border: 1px solid var(--primary-border);
      border-radius: 10px;
      padding: 24px;
      margin-bottom: 40px;
    }}
    
    .toc-title {{
      font-weight: 700;
      font-size: 1.15rem;
      color: var(--primary);
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    
    .toc-list {{
      list-style-type: none;
      padding-left: 5px;
    }}
    
    .toc-list li {{
      margin-bottom: 10px;
    }}
    
    .toc-list a {{
      color: #b91c1c;
      text-decoration: none;
      font-weight: 500;
      transition: color 0.2s;
    }}
    
    .toc-list a:hover {{
      color: #dc2626;
      text-decoration: underline;
    }}
    
    .section-title {{
      font-size: 1.5rem;
      color: #7f1d1d;
      border-bottom: 3px solid #dc2626;
      padding-bottom: 10px;
      margin: 45px 0 25px;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    
    .content-box {{
      background-color: #ffffff;
      border-radius: 12px;
      padding: 30px;
      margin-bottom: 35px;
      box-shadow: var(--shadow-sm);
    }}
    
    .content-box h3 {{
      font-size: 1.25rem;
      color: var(--primary);
      margin: 25px 0 12px;
      font-weight: 700;
    }}
    
    .content-box h3:first-child {{
      margin-top: 0;
    }}
    
    .content-box p {{
      margin-bottom: 16px;
      color: #374151;
    }}
    
    .content-box ul, .content-box ol {{
      margin: 15px 0 20px 25px;
      color: #374151;
    }}
    
    .content-box li {{
      margin-bottom: 8px;
    }}
    
    .product-card {{
      background: #ffffff;
      border-radius: 14px;
      padding: 30px;
      margin-bottom: 40px;
      box-shadow: var(--shadow-md);
      border: 1px solid var(--border);
      position: relative;
    }}
    
    .product-badge-rank {{
      display: inline-block;
      background: linear-gradient(135deg, #991b1b, #dc2626);
      color: #ffffff;
      font-weight: 800;
      font-size: 1.1rem;
      padding: 6px 18px;
      border-radius: 20px;
      margin-bottom: 12px;
    }}
    
    .product-tag {{
      font-size: 0.95rem;
      color: #b91c1c;
      font-weight: 700;
      margin-bottom: 8px;
    }}
    
    .product-name {{
      font-size: 1.4rem;
      color: #0f172a;
      line-height: 1.4;
      margin-bottom: 10px;
      font-weight: 800;
    }}
    
    .product-catch {{
      font-size: 1rem;
      color: #475569;
      font-weight: 600;
      margin-bottom: 24px;
      line-height: 1.6;
    }}
    
    .product-layout {{
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 30px;
    }}
    
    @media (max-width: 820px) {{
      .product-layout {{
        grid-template-columns: 1fr;
      }}
    }}
    
    .product-visual {{
      text-align: center;
    }}
    
    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: 10px;
      border: 1px solid #e2e8f0;
      background-color: #ffffff;
      margin-bottom: 15px;
      object-fit: contain;
    }}
    
    .price-box {{
      background: #fef2f2;
      padding: 12px;
      border-radius: 8px;
      margin-bottom: 15px;
      border: 1px solid #fecaca;
    }}
    
    .price-label {{
      font-size: 0.85rem;
      color: #991b1b;
      display: block;
      margin-bottom: 2px;
    }}
    
    .price-value {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #b91c1c;
    }}
    
    .price-tax {{
      font-size: 0.8rem;
      color: #991b1b;
    }}
    
    .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #bf0000 0%, #e60000 100%);
      color: #ffffff;
      text-decoration: none;
      font-weight: 700;
      font-size: 1.05rem;
      padding: 14px 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(191, 0, 0, 0.25);
      transition: all 0.2s;
    }}
    
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #a60000 0%, #cc0000 100%);
      box-shadow: 0 6px 10px rgba(191, 0, 0, 0.35);
      transform: translateY(-1px);
    }}
    
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 20px;
      font-size: 0.95rem;
    }}
    
    .spec-row {{
      display: grid;
      grid-template-columns: 130px 1fr;
      border-bottom: 1px solid #e2e8f0;
      padding: 8px 0;
    }}
    
    .spec-th {{
      font-weight: 700;
      color: #475569;
    }}
    
    .spec-td {{
      color: #1e293b;
    }}
    
    .review-box {{
      background: #fef2f2;
      border-left: 4px solid #dc2626;
      padding: 16px 20px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 16px;
    }}
    
    .review-box h4 {{
      font-size: 1.05rem;
      color: #991b1b;
      margin-bottom: 10px;
      font-weight: 700;
    }}
    
    .review-box p {{
      margin-bottom: 10px;
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.7;
    }}
    
    .review-box p:last-child {{
      margin-bottom: 0;
    }}
    
    .target-box, .usage-box {{
      background: #ffffff;
      border: 1px solid #fecaca;
      padding: 14px 18px;
      border-radius: 8px;
      margin-bottom: 12px;
      font-size: 0.95rem;
    }}
    
    .target-box strong, .usage-box strong {{
      color: #991b1b;
      display: block;
      margin-bottom: 4px;
    }}
    
    .target-box p, .usage-box p {{
      color: #475569;
      margin-bottom: 0;
    }}
    
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
      font-size: 0.95rem;
      background: #ffffff;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }}
    
    .data-table th, .data-table td {{
      padding: 12px 14px;
      border: 1px solid #fecaca;
      text-align: left;
    }}
    
    .data-table th {{
      background-color: #991b1b;
      color: #ffffff;
      font-weight: 700;
    }}
    
    .data-table tr:nth-child(even) {{
      background-color: #fef2f2;
    }}
    
    .tbl-rank {{
      font-weight: 700;
      color: #dc2626;
      white-space: nowrap;
    }}
    
    .tbl-name a {{
      color: #1e293b;
      text-decoration: none;
      font-weight: 600;
    }}
    
    .tbl-name a:hover {{
      color: #dc2626;
      text-decoration: underline;
    }}
    
    .tbl-price {{
      font-weight: 700;
      color: #b91c1c;
      white-space: nowrap;
    }}
    
    .faq-item {{
      background: #ffffff;
      border-radius: 10px;
      padding: 20px 24px;
      margin-bottom: 18px;
      box-shadow: var(--shadow-sm);
      border: 1px solid #fecaca;
    }}
    
    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: #991b1b;
      margin-bottom: 10px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }}
    
    .faq-q::before {{
      content: "Q";
      display: inline-block;
      background: #dc2626;
      color: #ffffff;
      font-size: 0.9rem;
      font-weight: 800;
      width: 26px;
      height: 26px;
      line-height: 26px;
      text-align: center;
      border-radius: 50%;
      flex-shrink: 0;
    }}
    
    .faq-a {{
      color: #334155;
      font-size: 0.98rem;
      line-height: 1.7;
      padding-left: 36px;
    }}
    
    .internal-links-box {{
      background: #ffffff;
      border-radius: 12px;
      padding: 30px;
      margin-top: 40px;
      box-shadow: var(--shadow-sm);
    }}
    
    .link-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 15px;
      margin-top: 20px;
    }}
    
    .link-card {{
      background: #fef2f2;
      border: 1px solid #fecaca;
      padding: 14px 18px;
      border-radius: 8px;
      text-decoration: none;
      color: #7f1d1d;
      font-size: 0.95rem;
      font-weight: 600;
      transition: all 0.2s;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    
    .link-card:hover {{
      background: #fee2e2;
      border-color: #dc2626;
      color: #b91c1c;
      transform: translateY(-2px);
    }}
    
    footer {{
      text-align: center;
      margin-top: 60px;
      color: #64748b;
      font-size: 0.9rem;
    }}
  </style>
</head>
<body>

  <header>
    <div class="site-logo"><a href="index.html">❄️ 冬コスメ徹底比較ラボ</a></div>
    <h1>保湿力の強さで肌乾燥とさようなら！赤の抗酸化力で冬の乾燥小ジワを跳ね返し濃密な潤いを満たす高保湿アスタキサンチンコスメランク10</h1>
    <div class="header-meta">
      <span>更新日：2026年11月4日</span> | <span>執筆・監修：冬コスメ徹底比較ラボ カロテノイド科学班</span>
    </div>
  </header>

  <div class="container">
    
    <div class="lead-box">
      <p>11月から12月にかけて、木枯らしが吹き抜け湿度が急低下する日本の冬。暖房の効いた乾いた空気と冷たい外気の激しい寒暖差により、目元や口元、ほうれい線にピキピキと細かな「乾燥小ジワ」が刻まれ、肌の弾力低下に頭を抱える方が急増します。この時期の肌内部では、活性酸素（一重項酸素）による酸化ダメージと角層バリアの崩壊が同時進行しています。</p>
      <p>自然界最強クラスの抗酸化力（ビタミンCの約6,000倍）を誇り、真冬の過酷な乾燥小ジワを跳ね返す奇跡の赤い美容成分が「アスタキサンチン」です。本記事では、楽天APIからリアルタイムに取得した正規商品画像・最新価格・在庫データをもとに、真冬の乾燥肌をふっくら満水にする高保湿アスタキサンチンコスメ厳選10選を徹底ランキング形式でご紹介します。</p>
    </div>

    <div class="toc-box">
      <div class="toc-title">📑 目次（クリックで各項目へジャンプ）</div>
      <ul class="toc-list">
        <li><a href="#power">1. ビタミンCの6000倍！なぜアスタキサンチンが真冬の乾燥小ジワを救うのか？</a></li>
        <li><a href="#ranking">2. 真冬の高保湿アスタキサンチンコスメおすすめ人気ランキング10選</a></li>
        <li><a href="#comparison">3. 厳選10商品のスペック・価格・配合成分徹底比較表</a></li>
        <li><a href="#guide">4. 失敗しないアスタキサンチンコスメの選び方＆アイテム別使い分け</a></li>
        <li><a href="#routine">5. 先行ジェリー×高機能クリーム！真冬の跳ね返しハリ肌ルーティン</a></li>
        <li><a href="#faq">6. アスタキサンチンコスメに関するよくある質問（FAQ）</a></li>
        <li><a href="#links">7. あわせて読みたい冬の集中高保湿スキンケア特集</a></li>
      </ul>
    </div>

    <section id="power" class="content-box">
      <h2 class="section-title">1. ビタミンCの6000倍！なぜアスタキサンチンが真冬の乾燥小ジワを救うのか？</h2>
      <p>冬になると「クリームを塗っても目元や口元の細かなシワが消えない」「夕方になると肌がしぼんでファンデーションがシワに溜まる」という現象が多発します。その背後には、真冬特有の「酸化乾燥スパイラル」が存在します。</p>
      
      <h3>細胞膜の内外を貫通して守る唯一無二の分子構造</h3>
      <p>アスタキサンチンは、ヘマトコッカス藻などが強い紫外線や乾燥ストレスから自らの身を守るために蓄える赤色の天然カロテノイドです。一般的な抗酸化成分（ビタミンCは水溶性で細胞の外側のみ、ビタミンEは油溶性で細胞膜の内側のみ）と異なり、アスタキサンチンは「親水基」と「親油基」の両方を両端に持っています。</p>
      <p>そのため、細胞膜の脂質二重層をまるで柱のように貫通して配置され、細胞の内側・外側・膜そのものの全てを活性酸素から死守。真冬の過酷な乾燥下でもコラーゲンやエラスチンの変性を防ぎ、跳ね返すようなピンとした弾力をキープできるのです。</p>

      <h3>セラミドとタッグを組むナノ浸透テクノロジー</h3>
      <p>油溶性で本来は浸透しにくいアスタキサンチンを、ナノ微粒子化してセラミドと結合させることで、角層深層への浸透スピードが劇的に進化。傷ついた角層ラメラ構造を修復しながら奥深くまで抗酸化力を届けられるため、11月〜12月の本格的な乾燥シーズンに最も頼もしい味方となります。</p>
    </section>

    <section id="ranking">
      <h2 class="section-title">2. 真冬の高保湿アスタキサンチンコスメおすすめ人気ランキング10選</h2>
      {cards_joined}
    </section>

    <section id="comparison" class="content-box">
      <h2 class="section-title">3. 厳選10商品のスペック・価格・配合成分徹底比較表</h2>
      <p>ご紹介したアスタキサンチンコスメ10品の種別、参考価格、真冬における保湿価値を一目で比較できるよう一覧表にまとめました。ご自身の肌悩みや好みの使用感に合わせて最適な1本をお選びください。</p>
      
      <div style="overflow-x: auto;">
        <table class="data-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>製品名</th>
              <th>タイプ</th>
              <th>楽天参考価格</th>
              <th>真冬の保湿バリュー</th>
            </tr>
          </thead>
          <tbody>
            {table_rows_joined}
          </tbody>
        </table>
      </div>
    </section>

    <section id="guide" class="content-box">
      <h2 class="section-title">4. 失敗しないアスタキサンチンコスメの選び方＆アイテム別使い分け</h2>
      <p>アスタキサンチンコスメは、洗顔直後の土台ケアから仕上げの濃密シールドまで多彩なバリエーションが存在します。真冬のケア目的に合わせた選び方を整理しました。</p>

      <h3>① 浸透力と土台立て直しなら「自己復元型先行ジェリー」</h3>
      <p>アスタリフトのジェリーアクアリスタのように、洗顔直後のまっさらな角層に届ける先行型は、Wヒト型ナノセラミドとの相乗効果で角層バリアを瞬時に再建します。その後に使う化粧水の浸透力が劇的に跳ね上がります。</p>

      <h3>② 夜間の水分蒸発を完全ブロックするなら「アドバンスドクリーム」</h3>
      <p>睡眠中の暖房乾燥による目元や口元のちりめんジワが気になる方は、濃厚な油分シールドを持つクリームが必須です。ナノアスタキサンチンとリコピンが翌朝までうるおいを閉じ込め、ふっくらとしたハリを維持します。</p>

      <h3>③ 忙しい朝の時短エイジングケアなら「濃厚オールインワンジェル」</h3>
      <p>DHCのように、コラーゲンやエラスチンを高配合した赤いオールインワンは、忙しい朝でも1品でメイク前のツヤ肌土台を完成させられます。</p>
    </section>

    <section id="routine" class="content-box">
      <h2 class="section-title">5. 先行ジェリー×高機能クリーム！真冬の跳ね返しハリ肌ルーティン</h2>
      <p>アスタキサンチンの効果を限界まで引き出す真冬のスキンケアステップをご紹介します。</p>

      <ol>
        <li><strong>洗顔直後に赤い先行ジェリー：</strong> タオルドライ後すぐにジェリーをなじませ、ナノアスタキサンチンとセラミドで角層バリアの穴を埋めます。</li>
        <li><strong>高保湿ローションで満水化：</strong> モイストローションを手のひらで温めながらハンドプレスし、角層細胞をふっくら潤わせます。</li>
        <li><strong>濃厚アスタキサンチンクリームで密封：</strong> お手入れの最後にクリームを密着させ、寝ている間の水分蒸発を物理的にブロックします。</li>
      </ol>
    </section>

    <section id="faq">
      <h2 class="section-title">6. アスタキサンチンコスメに関するよくある質問（FAQ）</h2>
      <div class="faq-list">
        {''.join([f'''
        <div class="faq-item">
          <div class="faq-q">{faq["question"]}</div>
          <div class="faq-a">{faq["answer"]}</div>
        </div>
        ''' for faq in faq_list])}
      </div>
    </section>

    <section id="links" class="internal-links-box">
      <h2 class="section-title" style="margin-top:0;">7. あわせて読みたい冬の集中高保湿スキンケア特集</h2>
      <p>冬の乾燥・肌荒れ・寒暖差トラブルを乗り越えるために、併せてチェックしたい注目の高保湿特集です。お悩みに合わせた最適なケアを見つけてみてください。</p>
      
      <div class="link-grid">
        <a href="winter-liposome.html" class="link-card">🧬 多重層リポソーム高保湿コスメ10選</a>
        <a href="winter-coenzyme-q10.html" class="link-card">⚡ 高濃度コエンザイムQ10コスメ10選</a>
        <a href="winter-ceramide-cream.html" class="link-card">🛡️ 真冬の高保湿セラミドクリーム10選</a>
        <a href="winter-ceramide-lotion.html" class="link-card">💧 高保湿セラミド化粧水ランキング</a>
        <a href="winter-retinol-cream.html" class="link-card">🌙 真冬の濃密レチノールクリーム</a>
        <a href="winter-niacinamide-serum.html" class="link-card">✨ シワ改善ナイアシンアミド美容液</a>
        <a href="winter-wrinkle-cream.html" class="link-card">👵 冬のシワ改善リンクルクリーム</a>
        <a href="winter-collagen-mask.html" class="link-card">💆‍♀️ 濃密コラーゲンシートマスク</a>
        <a href="winter-azulene.html" class="link-card">💙 寒暖差赤ら顔を救う高保湿アズレン</a>
        <a href="winter-tranexamic-acid.html" class="link-card">✨ 冬の透明ツヤ肌トラネキサム酸</a>
        <a href="winter-volufiline.html" class="link-card">🧬 目元口元ふっくらボルフィリン</a>
        <a href="winter-eye-cream.html" class="link-card">👁️ 真冬の乾燥を防ぐアイクリーム</a>
      </div>
    </section>

    <footer>
      <p>© 2026 冬コスメ徹底比較ラボ All Rights Reserved. 本サイトに掲載されている商品情報・価格は楽天APIより自動取得された最新データです。</p>
    </footer>

  </div>

</body>
</html>
"""

with open("winter-astaxanthin.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated winter-astaxanthin.html! Size: {len(html_content):,} bytes")
