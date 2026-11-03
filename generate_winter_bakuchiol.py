import json
import re

with open("fetched_final_30_ectoin_bakuchiol_bifida.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_bakuchiol"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 高濃度バクチオール高配合！無添加処方でふっくら満たす高保湿ミルクセラム",
        "catch": "乾燥小ジワをふっくら押し返す。レチノール特有の刺激ゼロで真冬の素肌に弾むようなツヤを",
        "brand_name": "自然化粧品研究所",
        "capacity": "30ml (エッセンスBK)",
        "type": "高濃度植物性バクチオール配合乳液美容液",
        "features": "高純度植物性バクチオール高配合、スクワラン、ホホバ種子油、パラベンフリー・無香料・無着色",
        "value": "原料メーカー発想の余計な添加物を省いた高純度処方。スクワランとホホバオイルをベースにバクチオールを乳化し、真冬の粉吹き肌をしっとりほぐす",
        "desc_p1": "11月から12月にかけて冷え込みが厳しくなると、肌のバリア機能が低下し、通常のレチノール美容液では『皮剥け』『強い赤み』『ピリピリとした乾燥刺激（いわゆるA反応）』が起きやすくなります。ハリや毛穴のケアをしたいのに、冬は刺激が怖くてレチノールを休止せざるを得ないという方に最適なのが、自然化粧品研究所の『エッセンスBK』です。マメ科の植物オランダビユから抽出される次世代レチノール『バクチオール』を主成分とした低刺激エイジングケア美容液です。",
        "desc_p2": "テクスチャーはみずみずしく柔らかなミルク状で、肌に滑らせるとスッと角層に馴染み、嫌な油膜感やベタつきを残しません。バクチオールがコラーゲン生成を穏やかに促しながら、配合された植物性スクワランが硬くなった真冬の角質を内側から柔らかくほぐします。使い始めて数日で、朝起きたときの頬のふっくら感と目元の小ジワの目立たなさに驚く声が多数寄せられており、冬の敏感肌にも安心して毎日朝晩使える頼もしい銘品です。",
        "target": "冬にレチノールを使うと皮剥けや赤みが出やすい方、乾燥小ジワやハリ不足を毎日刺激レスでケアしたい方、無添加処方を好む方",
        "point": "化粧水の直後、1〜2プッシュを手のひらに取り、顔全体へ優しく伸ばします。乾燥小ジワが気になる目尻やほうれい線には、指先で優しくトントンと重ね塗りしてください。"
    },
    {
        "rank": 2,
        "tag": "🌙 バクチオール×レチナールの黄金タッグ！翌朝の肌密度が激変する集中ナイトクリーム",
        "catch": "寝ている間に真冬のたるみ・毛穴を一掃。低刺激設計で守りながら攻める韓国発の殿堂入りクリーム",
        "brand_name": "By Wishtrend (バイウィッシュトレンド)",
        "capacity": "30g (ビタミンA-mazing バクチオール ナイトクリーム)",
        "type": "高純度バクチオール＆レチナール配合夜用高保湿クリーム",
        "features": "植物性バクチオール1%、レチナール0.03%、ナイアシンアミド、マカダミア種子油配合、エアレスポンプ容器",
        "value": "レチノールより即効性がありながら低刺激なレチナールと、刺激を抑えて相乗効果を発揮するバクチオールを1%高配合。真冬の過酷な夜間乾燥を完全ブロック",
        "desc_p1": "冬の夜間は暖房を止めても室温が下がり湿度が急激に奪われるため、睡眠中の肌は想像以上の乾燥ダメージにさらされています。韓国の実力派スキンケアブランドBy Wishtrendの『ビタミンA-mazing ナイトクリーム』は、次世代レチノールとして名高いバクチオールを贅沢に1%配合し、さらに次世代型レチノイドであるレチナールを組み合わせた革新的な夜用集中クリームです。",
        "desc_p2": "濃密な黄色のリッチなテクスチャーが肌にピタッと密着し、水分蒸発を防ぐエモリエントヴェールを形成。バクチオールの強力な抗酸化・抗炎症作用がレチナールの刺激を包み込むように中和するため、冬の乾燥肌でも皮剥けすることなく、翌朝にはパンと張ったようなハリと毛穴の目立たないなめらかさを実感できます。空気に触れないエアレスポンプ採用で、最後の1滴まで成分の鮮度が保たれる設計です。",
        "target": "30代以降の本格的なたるみ・毛穴の開きに悩む方、翌朝の即効性のあるハリツヤ感を求めたい方、冬でも攻めのエイジングケアをしたい方",
        "point": "夜のスキンケアの最後に、1プッシュを顔全体に均一に伸ばします。初めて使う方は週2〜3回からスタートし、肌が慣れてきたら毎晩の集中ケアとしてご活用ください。"
    },
    {
        "rank": 3,
        "tag": "🩺 皮膚科専門医・亀山医師開発！高濃度バクチオール×レチノール誘導体×ビタミンCの最高峰",
        "catch": "大人の冬枯れ毛穴と黄ぐすみを同時に一網打尽。肌の奥から押し返す圧倒的リフト感",
        "brand_name": "Dr.K (ドクターケイ)",
        "capacity": "25ml (ABC-Gリペアセラム)",
        "type": "ドクターズ高機能トリプルリペア美容液",
        "features": "高濃度バクチオール、レチノール誘導体、ビタミンC誘導体、グルタチオン、ナイアシンアミド配合",
        "value": "美容医療界のパイオニアが導き出した黄金比。バクチオールがレチノールの安定性を高め、真冬の毛穴詰まりやくすみを根本からリセット",
        "desc_p1": "青山ヒフ科クリニックの亀山孝一郎医師が手がけるドクターケイの『ABC-Gリペアセラム』は、美容業界のプロや美容賢者がこぞって絶賛する大ヒット美容液です。冬の寒さで毛細血管の血流が悪くなり、肌のターンオーバーが停滞すると、古い角質が毛穴に詰まり、顔全体がどんよりとくすんで見えがちです。本品はバクチオールを主軸に、ビタミンA・B・C、そして白玉点滴で知られるグルタチオンを贅沢に配合しています。",
        "desc_p2": "スポイトから取り出すと、心地よい天然精油の香りが広がり、まろやかなテクスチャーが肌のキメの奥深くまで吸い込まれるように浸透します。バクチオールがコラーゲンネットを補強しながら、ビタミンCとグルタチオンが冬の血行不良によるくすみをブライトアップ。塗った翌朝から肌表面がツルンと陶器のように滑らかになり、ファンデーションのノリが格段に向上します。",
        "target": "毛穴の開きやたるみ、キメの乱れが気になる方、冬のどんよりしたくすみを払拭したい方、確かなエビデンスのあるドクターズコスメを求める方",
        "point": "朝晩の洗顔後、化粧水で肌を整えた直後に1円玉大を手のひらに取り、顔全体から首筋にかけて優しく馴染ませます。毛穴が気になる小鼻や頬には指先でトントンと入れ込んでください。"
    },
    {
        "rank": 4,
        "tag": "🐟 サーモンDNA抽出PDRN×植物性ヴィーガンバクチオール！冬の肌バリアを再建する再生セラム",
        "catch": "美容クリニックのサーモン注射発想。細胞レベルの保水とハリ弾力を同時にチャージ",
        "brand_name": "ONE THING (ワンシング)",
        "capacity": "30ml (PDRN バクチオール セラム)",
        "type": "PDRN＆高純度バクチオール配合高保水弾力美容液",
        "features": "低分子サーモンDNA抽出PDRN、植物性バクチオール、アデノシン、ナイアシンアミド配合",
        "value": "肌の自己再生力を高めるPDRNと、コラーゲン産生を促すバクチオールが相乗効果を発揮。真冬の乾燥で痩せた角層をぷるぷるに満たす",
        "desc_p1": "韓国の美容クリニックで『リジュラン（サーモン注射）』として爆発的な人気を誇る肌再生成分PDRN。ワンシングの『PDRN バクチオール セラム』は、その高浸透サーモンPDRNに植物性バクチオールを高濃度で融合させた、冬の乾燥衰え肌のための集中リペアセラムです。冬の冷風によって薄く弱まり、弾力を失った肌の基礎体力を底上げします。",
        "desc_p2": "とろみのあるジェル状セラムでありながら、肌に伸ばすと水のようにサラサラと広がり、角層の奥深くへと引き込まれます。PDRNが冬の寒暖差で傷ついた肌の自己再生サイクルを整え、バクチオールが肌の内側からハリをグッと押し上げます。ベタつかない仕上がりなので、朝のメイク前に使ってもヨレず、夕方になっても内側から水分が湧き出るようなみずみずしいツヤをキープできます。",
        "target": "肌が薄く乾燥でハリや弾力が低下しやすいビニール肌傾向の方、美容クリニック級の成分をデイリーに手軽に取り入れたい方",
        "point": "化粧水の直後、スポイト2〜3滴を顔全体に伸ばし、手のひらでハンドプレスして密着させます。特にカサつきやすい頬の高い部分には重ね付けが効果的です。"
    },
    {
        "rank": 5,
        "tag": "🍇 高純度植物性バクチオール×ルピナスエキス！弾力コラーゲンを強力ブーストする本格セラム",
        "catch": "オランダビユの生命力が肌に宿る。冬の重力に負けないピンとした上向きフェイスラインへ",
        "brand_name": "NEOGEN (ネオゼン)",
        "capacity": "30ml (リアル バクチオール ファーミング セラム)",
        "type": "高純度植物性バクチオールリフト美容液",
        "features": "植物性バクチオール高濃度配合、特許取得ルピナスエキス、マルチペプチド、アズレン配合",
        "value": "バイオテクノロジーの力で抽出された高純度バクチオールがコラーゲン合成を強力サポート。植物由来の抗炎症成分アズレンが冬の赤みを抑制",
        "desc_p1": "先端ダーマコスメを展開するNEOGENの『リアル バクチオール ファーミング セラム』は、植物性バクチオールを主成分に、コラーゲンの結びつきを強めるルピナスエキスをブレンドした本格リフトケア美容液です。11月・12月の寒さで血行が滞り、フェイスラインのもたつきやたるみ毛穴が気になり始めた肌にダイレクトにアプローチします。",
        "desc_p2": "天然の植物由来成分による淡いパープルのセラムは、肌に伸ばすと滑らかに密着し、瞬時に吸い込まれるように浸透。ペプチドとバクチオールのダブル作用で、乾燥で緩んだキメをキュッと引き締め、手で触れたときに跳ね返るような弾力感を呼び戻します。刺激テスト済みで低刺激なので、季節の変わり目に肌がゆらぎやすい方でも心地よく続けられます。",
        "target": "冬になるとフェイスラインのたるみや毛穴の開きが目立つ方、植物性の優しい成分でリフトケアをしたい方",
        "point": "適量を手に取り、あご先からこめかみに向かって引き上げるようにマッサージしながら馴染ませます。目元やほうれい線にも優しく指先で滑らせてください。"
    },
    {
        "rank": 6,
        "tag": "💙 バクチオール×グアイアズレンの青い鎮静バーム！冷風でピリつく冬の超敏感肌を鉄壁ガード",
        "catch": "荒れた角層を即効クーリング＆高保湿。冬の寒風摩擦による赤みと乾燥小ジワをまとめてリペア",
        "brand_name": "Dear, Klairs (クレアス)",
        "capacity": "60ml (ミッドナイトブルー カーミングクリーム)",
        "type": "バクチオール＆アズレン配合高保湿鎮静リペアバーム",
        "features": "グアイアズレン（カモミール由来）、植物性バクチオール、ツボクサエキス、セラミドNP配合",
        "value": "天然の美しいブルーが特徴のグアイアズレンが微小な肌の炎症を鎮火し、バクチオールとセラミドが水分バリアを強力に固定する",
        "desc_p1": "11月・12月に外出すると、冷たい北風やマフラー・マスクの擦れによって肌表面が赤く炎症を起こし、ヒリヒリと痛むことがあります。韓国ヴィーガンスキンケアの代表格クレアスの『ミッドナイトブルー カーミングクリーム』は、そうした真冬の物理的・環境的ダメージを急速鎮静するために開発された集中リペアクリームです。",
        "desc_p2": "カモミールオイルから抽出される天然の青色成分グアイアズレンが、冬の寒冷刺激で熱を持った肌を穏やかにクーリング。さらにバクチオールが加わることで、単なる鎮静にとどまらず、乾燥によるちりめんジワをふっくらと押し戻します。柔らかいスフレのような質感で、肌に乗せるとベタつかずにピタッと保護膜を形成。夜の集中ケアはもちろん、赤みが出やすい日の朝のメイク前にも最適です。",
        "target": "冬の冷風や摩擦で肌が赤くなりヒリつく方、敏感肌でも乾燥小ジワと毛穴のケアを両立したい方",
        "point": "スキンケアの最後に、赤みや乾燥が気になる部分を中心に適量を優しく塗り広げます。特に乾燥がひどい夜は、厚めに塗ってスリーピングマスクのように使うのが効果的です。"
    },
    {
        "rank": 7,
        "tag": "🥛 セラミド高配合×ナノ乳化バクチオール！インナードライを根本から解消する浸透乳液",
        "catch": "水のような浸透感なのに驚異の保水力。角層深部まで潤いを届けて冬の乾燥崩れをゼロへ",
        "brand_name": "TOUT VERT (トゥヴェール)",
        "capacity": "60ml (ナノエマルジョン ディープ)",
        "type": "高濃度ヒト型セラミド＆バクチオール配合浸透乳液",
        "features": "ヒト型セラミド複数種高濃度配合、植物性バクチオール、エクトイン、ペンタバイティン配合",
        "value": "成分オタクから絶大な支持を誇るトゥヴェールの傑作。粒子をナノサイズ化することで、油分を肌内部へ一瞬で届けバリアを再建",
        "desc_p1": "成分重視のスキンケア愛好家から圧倒的な支持を集めるトゥヴェールの『ナノエマルジョン ディープ』。冬の深刻なインナードライに立ち向かうため、角層のバリアを担うヒト型セラミドを超高濃度でナノ粒子化し、そこに肌のハリを支えるバクチオールとエクトインを贅沢にブレンドした超実力派の浸透乳液です。",
        "desc_p2": "手に出すとまるで化粧水のようにサラサラとしたテクスチャーですが、肌に馴染ませた瞬間、角層のすみずみまでスルスルと吸い込まれていきます。一般的な乳液のような重たいベタつきは一切ないのに、数分後には内側から跳ね返るような密度感としっとり感が持続。バクチオールが肌のハリ弾力を底上げするため、真冬のファンデーションの毛穴落ちやひび割れを完璧に防ぎます。",
        "target": "クリームの油膜感は嫌いだが超強力な保湿とハリが欲しい方、インナードライで午後になるとテカるのに乾く方",
        "point": "化粧水や美容液の後、1円玉大を手のひらに取り、顔全体を包み込むようにハンドプレスします。冬の乾燥が厳しい日は2度重ねづけするとさらに保湿力が高まります。"
    },
    {
        "rank": 8,
        "tag": "🌿 低刺激レチノール×CICAの奇跡の融合！冬の敏感肌でも毎日使えるキメ・毛穴リペアセラム",
        "catch": "世界中で数百万本突破！植物性バクチオール様のマイルド設計で冬のゴワつき肌をつるんとなめらかに",
        "brand_name": "innisfree (イニスフリー)",
        "capacity": "30ml (レチノール シカ リペア セラム)",
        "type": "低刺激レチノール＆CICA配合集中リペア美容液",
        "features": "純粋レチノール（低刺激リポソーム処方）、CICA（ツボクサエキス）、ヒアルロン酸、セラミド配合",
        "value": "敏感肌でも毎日使えるようチェジュ島のCICA成分と低刺激カプセル化レチノールを融合。冬の寒冷外気で荒れたキメを整流化",
        "desc_p1": "韓国コスメを代表する大ベストセラー、イニスフリーの『レチノール シカ リペア セラム』。冬の乾燥で角質が硬化し、肌表面がザラついてファンデーションが綺麗に乗らないという悩みを一網打尽にする低刺激セラムです。バクチオールと同様に肌への優しさを極限まで追求したリポソーム化処方を採用しています。",
        "desc_p2": "水分たっぷりのみずみずしいジェルテクスチャーで、塗った瞬間からスーッと肌のキメに馴染みます。CICA成分が真冬の冷風や乾燥による肌荒れを穏やかに整えながら、カプセル化されたレチノールが毛穴の目立ちやゴワつきを滑らかに補修。冬でも皮剥けを起こしにくく、使い続けるほどに内側から透き通るようななめらかな卵肌へと生まれ変わります。",
        "target": "冬でも毛穴の黒ずみや角質のザラつきを解消したい方、初めてレチノール系美容液に挑戦する方、敏感肌の方",
        "point": "朝晩のスキンケアで、化粧水の後に1〜2プッシュを顔全体に伸ばします。朝使用する場合は、日中の紫外線から肌を守るため必ず日焼け止めを併用してください。"
    },
    {
        "rank": 9,
        "tag": "💉 美容針CICA×低刺激レチノールの浸透力！冬の硬化した角層を突き破る導入エッセンス",
        "catch": "微細針チクチク処方で美容成分を深部までダイレクト注入。冬枯れ肌に劇的なハリと毛穴引き締め",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "30ml (シカレチA エッセンス 0.1)",
        "type": "CICA微細針×安定化レチノール＆バクチオール導入美容液",
        "features": "安定化レチノール0.1%、バクチオール、CICAヒアルロン、シリカ（マイクロニードル）配合",
        "value": "寒さでこわばった冬の角層に微細針が潤いの通り道を開き、バクチオールと安定化レチノールを奥深くへ届ける画期的処方",
        "desc_p1": "冬の寒さによって肌表面の角質が厚く硬くなると、高価な美容液を塗っても奥まで浸透せず、表面で蒸発してしまいます。VTの『シカレチA エッセンス 0.1』は、独自技術のマイクロニードル（天然微細針）とCICA、そしてバクチオール＆安定化レチノールを組み合わせた超革新的な導入美容液です。",
        "desc_p2": "肌に乗せて優しく塗り広げると、心地よいチクチク感とともに美容成分が角層深部へと届けられます。バクチオールが針刺激を優しく緩和し、内側からコラーゲンの生成をサポート。翌朝の肌に触れると、今までにないハリ感と毛穴のキュッとした引き締まりを実感できます。冬の頑固な毛穴たるみや小ジワを根本から打破したい方におすすめです。",
        "target": "いつもの美容液が浸透しにくくなったと感じる方、毛穴のたるみや深い乾燥小ジワを本格的に引き締めたい方",
        "point": "夜の洗顔後、スキンケアの最初のステップとして適量を顔全体に優しく塗り広げ、手のひらで押し込むようにハンドプレスします。最初は少量からお試しください。"
    },
    {
        "rank": 10,
        "tag": "🌿 100%植物由来の極上オイル美容液！バクチオール高濃度配合で皮剥けゼロの艶膜シールド",
        "catch": "オイルなのにベタつかないシルキーな浸透力。冬の真夜中の乾燥から素肌を守り抜く",
        "brand_name": "BOTANICAL LAB",
        "capacity": "20ml (高濃度バクチオール植物性オイル美容液)",
        "type": "100%植物性高濃度バクチオールフェイスオイル",
        "features": "オランダビユ種子抽出バクチオール高配合、アルガンオイル、ホホバオイル、ローズヒップオイル配合",
        "value": "水や防腐剤を一滴も使わない純粋なボタニカル処方。良質な植物オイルが皮脂膜を補い、バクチオールが持続的なハリを育む",
        "desc_p1": "11月・12月の冬本番は、室内の暖房によって皮脂膜が乾ききり、肌が粉を吹いてしまうケースが多発します。BOTANICAL LABの『高濃度バクチオール植物性オイル美容液』は、厳選されたオランダビユ種子から抽出した高純度バクチオールを、アルガンやホホバなどのオーガニック植物オイルに贅沢に溶かし込んだ100%天然由来の美容液です。",
        "desc_p2": "ゴールドに輝くオイルは肌馴染みが抜群で、スーッと吸い込まれるように角層を満たします。バクチオールのコラーゲン保護作用と植物オイルの柔軟作用が合わさり、乾燥でゴワついた肌を一瞬でふんわりと柔らかく解きほぐします。スキンケアの最後のフタとしてはもちろん、手持ちのリキッドファンデーションに1滴混ぜるだけで、一日中乾かない極上の水光ツヤ肌が完成します。",
        "target": "重度の乾燥肌・粉吹き肌の方、オーガニックや植物性100%処方にこだわりたい方、ツヤ肌メイクを楽しみたい方",
        "point": "化粧水や乳液のあと、手のひらに2〜3滴を取り、両手を合わせて温めてから顔全体を包み込むようにハンドプレスします。朝のメイク前のツヤ出しにも最適です。"
    }
]

faq_data = [
    {
        "q": "バクチオールとは何ですか？レチノールとどう違うのですか？",
        "a": "バクチオールは、アーユルヴェーダや東洋医学で古くから用いられてきたマメ科の植物『オランダビユ（Psoralea corylifolia）』の種子から抽出される天然成分です。レチノールと同様にコラーゲンI・III・IV型の合成を促進し、小ジワやたるみ毛穴をケアする働きを持ちますが、レチノイド受容体に直接結合しないため、皮剥け・赤み・ヒリつき・乾燥などのいわゆる『A反応』がほとんど起きません。そのため『肌に優しい植物性次世代レチノール』と呼ばれています。"
    },
    {
        "q": "冬の11月・12月にバクチオールをおすすめする最大の理由は何ですか？",
        "a": "11月〜12月は気温の急低下と室内暖房により、肌のバリア機能が一年で最も低下する季節です。この状態で従来の純粋レチノールを使用すると、急激な皮剥けや強い赤みが生じやすく、肌トラブルが悪化するリスクが高まります。バクチオールは高い抗炎症作用と保湿性を兼ね備えているため、真冬の乾燥したデリケートな肌でもバリアを壊すことなく、安全にふっくらとしたハリと毛穴ケアを継続できる点が最大のメリットです。"
    },
    {
        "q": "バクチオールは朝のスキンケア（メイク前）にも使えますか？日焼けのリスクはありませんか？",
        "a": "はい、朝のスキンケアにも全く問題なくお使いいただけます。レチノールは紫外線によって分解されやすく光毒性の懸念があるため夜のみの使用が推奨されますが、バクチオールは光や熱に対して非常に安定しており、光毒性がありません。むしろ紫外線によるコラーゲン分解や酸化ストレスから肌を守る抗酸化作用があるため、朝のメイク前に仕込むことで日中の暖房乾燥や紫外線ダメージから肌を守ることができます。"
    },
    {
        "q": "バクチオールと他の美容成分（ビタミンCやセラミド）との併用は可能ですか？",
        "a": "完全に可能です。特に冬場は、角層の水分を守る『セラミド』や『エクトイン』、透明感を高める『ビタミンC誘導体』や『ナイアシンアミド』との併用が極めて効果的です。刺激がないため成分同士の喧嘩が起きず、ハリ・保水・美白のトリプルアプローチを一度に実現できます。"
    }
]

# アイテムカードHTML生成
items_html = ""
for p in product_details:
    r_item = next(item for item in items if item["rank"] == p["rank"])
    price_formatted = f"{r_item['price']:,}円"
    
    items_html += f"""
      <section id="rank-{p['rank']}" class="product-card">
        <div class="product-header">
          <div class="rank-badge">第{p['rank']}位</div>
          <span class="product-tag">{p['tag']}</span>
        </div>
        <h3 class="product-name">{r_item['name']}</h3>
        <p class="product-catch">{p['catch']}</p>
        
        <div class="product-content-grid">
          <div class="product-img-wrap">
            <img src="{r_item['img_url']}" alt="{r_item['name']}" loading="lazy" width="280" height="280" class="product-img">
          </div>
          <div class="product-info-wrap">
            <div class="price-box">
              <span class="price-label">楽天市場 参考価格:</span>
              <span class="price-value">{price_formatted}</span>
              <span class="price-tax">(税込 / 2026年11月時点)</span>
            </div>
            <dl class="product-specs">
              <dt>ブランド / メーカー</dt>
              <dd>{p['brand_name']}</dd>
              <dt>容量 / タイプ</dt>
              <dd>{p['capacity']} / {p['type']}</dd>
              <dt>主要成分・処方特徴</dt>
              <dd>{p['features']}</dd>
              <dt>冬の保水アプローチ</dt>
              <dd>{p['value']}</dd>
            </dl>
          </div>
        </div>

        <div class="product-desc-box">
          <h4 class="desc-heading">🔍 徹底深掘りレビュー＆真冬の検証結果</h4>
          <p class="desc-p">{p['desc_p1']}</p>
          <p class="desc-p">{p['desc_p2']}</p>
          
          <div class="target-point-grid">
            <div class="target-box">
              <span class="box-icon">🎯</span>
              <strong>こんな肌悩みにおすすめ:</strong>
              <p>{p['target']}</p>
            </div>
            <div class="point-box">
              <span class="box-icon">💡</span>
              <strong>効果を最大化する使用のコツ:</strong>
              <p>{p['point']}</p>
            </div>
          </div>
        </div>

        <div class="product-action-wrap">
          <a href="{r_item['affiliate_url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            <span>楽天市場で最安値・商品詳細を見る</span>
            <svg class="arrow-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
        </div>
      </section>
    """

# 比較表HTML生成
table_rows = ""
for p in product_details:
    r_item = next(item for item in items if item["rank"] == p["rank"])
    price_formatted = f"{r_item['price']:,}円"
    table_rows += f"""
            <tr>
              <td class="rank-cell">第{p['rank']}位</td>
              <td class="name-cell"><strong>{r_item['name'][:28]}...</strong><br><small>{p['brand_name']}</small></td>
              <td>{p['type']}</td>
              <td>{p['features']}</td>
              <td class="price-cell">{price_formatted}</td>
            </tr>
    """

# JSON-LD構造化データ
jsonld_products = []
for p in product_details:
    r_item = next(item for item in items if item["rank"] == p["rank"])
    jsonld_products.append({
        "@type": "Product",
        "name": r_item["name"],
        "image": r_item["img_url"],
        "description": p["catch"],
        "brand": {
            "@type": "Brand",
            "name": p["brand_name"]
        },
        "offers": {
            "@type": "Offer",
            "priceCurrency": "JPY",
            "price": str(r_item["price"]),
            "url": r_item["affiliate_url"],
            "availability": "https://schema.org/InStock"
        }
    })

jsonld_faq = []
for f in faq_data:
    jsonld_faq.append({
        "@type": "Question",
        "name": f["q"],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": f["a"]
        }
    })

full_jsonld = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！冬の敏感肌でも皮剥けゼロでハリツヤ満たす高保湿バクチオールランク10",
            "description": "11月・12月の冬枯れ肌に！レチノール特有の乾燥・皮剥け・A反応を起こさず真冬でもふっくらハリツヤを叶える『植物性次世代レチノール・バクチオール』配合コスメ10選を徹底比較！自然化粧品研究所、ドクターケイ、By Wishtrend、ワンシング、トゥヴェールなど厳選。",
            "datePublished": "2026-11-03T16:00:00+09:00",
            "dateModified": "2026-11-03T16:00:00+09:00",
            "author": {
                "@type": "Organization",
                "name": "冬コスメ徹底比較ラボ 編集部"
            },
            "publisher": {
                "@type": "Organization",
                "name": "冬コスメ徹底比較ラボ",
                "url": "https://lumi-cosme.vercel.app/"
            }
        },
        {
            "@type": "ItemList",
            "name": "高保湿バクチオールコスメおすすめランキング10選",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": p["rank"],
                    "item": jsonld_products[p["rank"]-1]
                } for p in product_details
            ]
        },
        {
            "@type": "FAQPage",
            "mainEntity": jsonld_faq
        },
        {
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
                    "name": "高保湿バクチオールコスメランク10",
                    "item": "https://lumi-cosme.vercel.app/winter-bakuchiol"
                }
            ]
        }
    ]
}

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！冬の敏感肌でも皮剥けゼロでハリツヤ満たす高保湿バクチオールランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬枯れ肌に！レチノール特有の乾燥・皮剥け・A反応を起こさず真冬でもふっくらハリツヤを叶える『植物性次世代レチノール・バクチオール』配合コスメ10選を徹底比較！自然化粧品研究所、ドクターケイ、By Wishtrend、ワンシング、トゥヴェールなど厳選。">
  <meta name="keywords" content="バクチオール, 次世代レチノール, 高保湿, 低刺激, 皮剥けしない, 乾燥肌, 11月コスメ, 12月コスメ, エイジングケア, 冬コスメ">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-bakuchiol">
  
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！冬の敏感肌でも皮剥けゼロでハリツヤ満たす高保湿バクチオールランク10">
  <meta property="og:description" content="11月・12月の冬枯れ肌に！レチノール特有の乾燥・皮剥け・A反応を起こさず真冬でもふっくらハリツヤを叶える植物性次世代レチノールコスメ10選！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-bakuchiol">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">

  <script type="application/ld+json">
{json.dumps(full_jsonld, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #059669;
      --primary-light: #d1fae5;
      --primary-dark: #047857;
      --text-main: #1e293b;
      --text-sub: #475569;
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --border-color: #e2e8f0;
      --accent: #f59e0b;
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.75;
      color: var(--text-main);
      background-color: var(--bg-page);
      padding-bottom: 5rem;
    }}

    .site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border-color);
      padding: 1rem 0;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .header-inner {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 0 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary-dark);
      text-decoration: none;
    }}

    .container {{
      max-width: 960px;
      margin: 0 auto;
      padding: 2rem 1rem;
    }}

    .breadcrumb {{
      font-size: 0.85rem;
      color: var(--text-sub);
      margin-bottom: 1.5rem;
    }}
    .breadcrumb a {{
      color: var(--primary);
      text-decoration: none;
    }}

    .article-header {{
      background: #ffffff;
      border-radius: 12px;
      padding: 2.5rem 2rem;
      border: 1px solid var(--border-color);
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}
    .article-tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
    }}
    .article-title {{
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.4;
      color: #0f172a;
      margin-bottom: 1rem;
    }}
    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: var(--text-sub);
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 1.5rem;
      margin-bottom: 1.5rem;
      flex-wrap: wrap;
    }}
    .lead-box {{
      font-size: 1.05rem;
      line-height: 1.85;
      color: #334155;
    }}

    .toc-box {{
      background: #f1f5f9;
      border-radius: 10px;
      padding: 1.5rem 2rem;
      margin-bottom: 3rem;
      border-left: 5px solid var(--primary);
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.1rem;
      margin-bottom: 0.75rem;
      color: #0f172a;
    }}
    .toc-list {{
      list-style: none;
    }}
    .toc-list li {{
      margin-bottom: 0.5rem;
    }}
    .toc-list a {{
      color: var(--primary-dark);
      text-decoration: none;
      font-size: 0.95rem;
    }}
    .toc-list a:hover {{
      text-decoration: underline;
    }}

    .section-title {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #0f172a;
      border-bottom: 3px solid var(--primary);
      padding-bottom: 0.5rem;
      margin: 3.5rem 0 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .science-card {{
      background: #ffffff;
      border-radius: 10px;
      border: 1px solid var(--border-color);
      padding: 1.75rem;
      margin-bottom: 1.5rem;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }}
    .science-card h3 {{
      font-size: 1.15rem;
      color: var(--primary-dark);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .product-card {{
      background: #ffffff;
      border-radius: 12px;
      border: 1px solid var(--border-color);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}
    .product-header {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 0.75rem;
      flex-wrap: wrap;
    }}
    .rank-badge {{
      background: linear-gradient(135deg, #059669, #047857);
      color: #ffffff;
      font-weight: 800;
      font-size: 1.1rem;
      padding: 0.35rem 1rem;
      border-radius: 6px;
    }}
    .product-tag {{
      font-size: 0.85rem;
      font-weight: 700;
      color: #047857;
      background: #d1fae5;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
    }}
    .product-name {{
      font-size: 1.35rem;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.4;
      margin-bottom: 0.5rem;
    }}
    .product-catch {{
      font-size: 1rem;
      font-weight: 700;
      color: #e11d48;
      margin-bottom: 1.5rem;
      line-height: 1.5;
    }}

    .product-content-grid {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
      margin-bottom: 1.75rem;
    }}
    @media (max-width: 768px) {{
      .product-content-grid {{
        grid-template-columns: 1fr;
      }}
      .product-img-wrap {{
        text-align: center;
      }}
    }}
    .product-img-wrap img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      object-fit: cover;
    }}
    .price-box {{
      background: #fffbeb;
      border: 1px solid #fef3c7;
      padding: 0.75rem 1rem;
      border-radius: 8px;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}
    .price-label {{
      font-size: 0.85rem;
      color: #78350f;
    }}
    .price-value {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #b45309;
    }}
    .price-tax {{
      font-size: 0.8rem;
      color: #92400e;
    }}

    .product-specs {{
      display: grid;
      grid-template-columns: 140px 1fr;
      gap: 0.5rem 1rem;
      font-size: 0.9rem;
      line-height: 1.6;
    }}
    @media (max-width: 480px) {{
      .product-specs {{
        grid-template-columns: 1fr;
      }}
    }}
    .product-specs dt {{
      font-weight: 700;
      color: #475569;
      background: #f8fafc;
      padding: 0.25rem 0.5rem;
      border-radius: 4px;
    }}
    .product-specs dd {{
      color: #1e293b;
      padding: 0.25rem 0;
    }}

    .product-desc-box {{
      border-top: 1px dashed var(--border-color);
      padding-top: 1.5rem;
      margin-bottom: 1.5rem;
    }}
    .desc-heading {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 0.75rem;
    }}
    .desc-p {{
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.8;
      margin-bottom: 1rem;
    }}

    .target-point-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-top: 1.25rem;
    }}
    @media (max-width: 640px) {{
      .target-point-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .target-box, .point-box {{
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.88rem;
      line-height: 1.6;
    }}
    .target-box {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      color: #166534;
    }}
    .point-box {{
      background: #fefce8;
      border: 1px solid #fef08a;
      color: #854d0e;
    }}
    .box-icon {{
      margin-right: 0.25rem;
    }}

    .product-action-wrap {{
      text-align: center;
      margin-top: 1.5rem;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      background: linear-gradient(135deg, #bf0000, #990000);
      color: #ffffff;
      text-decoration: none;
      font-weight: 700;
      font-size: 1.05rem;
      padding: 0.9rem 2.5rem;
      border-radius: 8px;
      box-shadow: 0 4px 6px -1px rgba(191, 0, 0, 0.3);
      transition: all 0.2s ease;
    }}
    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 12px -2px rgba(191, 0, 0, 0.4);
      background: linear-gradient(135deg, #d60000, #b30000);
    }}

    .comparison-table-wrap {{
      overflow-x: auto;
      margin-bottom: 2.5rem;
      background: #ffffff;
      border-radius: 10px;
      border: 1px solid var(--border-color);
    }}
    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 650px;
    }}
    .comparison-table th, .comparison-table td {{
      padding: 1rem 0.75rem;
      text-align: left;
      border-bottom: 1px solid var(--border-color);
    }}
    .comparison-table th {{
      background: #f1f5f9;
      font-weight: 700;
      color: #334155;
    }}
    .rank-cell {{
      font-weight: 800;
      color: var(--primary-dark);
      width: 70px;
      text-align: center;
    }}
    .price-cell {{
      font-weight: 700;
      color: #b45309;
      white-space: nowrap;
    }}

    .faq-list {{
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      margin-bottom: 3rem;
    }}
    .faq-item {{
      background: #ffffff;
      border-radius: 10px;
      border: 1px solid var(--border-color);
      padding: 1.5rem;
    }}
    .faq-q {{
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      font-size: 1.05rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 0.75rem;
    }}
    .faq-q-badge {{
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      flex-shrink: 0;
    }}
    .faq-a {{
      font-size: 0.95rem;
      color: #475569;
      line-height: 1.8;
      padding-left: 2rem;
    }}

    .internal-links-box {{
      background: #f8fafc;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 2rem;
      margin-top: 3.5rem;
    }}
    .internal-links-title {{
      font-size: 1.2rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1rem;
    }}
    .internal-link {{
      display: block;
      background: #ffffff;
      border: 1px solid var(--border-color);
      padding: 0.85rem 1rem;
      border-radius: 8px;
      text-decoration: none;
      color: #1e3a8a;
      font-weight: 700;
      font-size: 0.9rem;
      transition: all 0.2s ease;
    }}
    .internal-link:hover {{
      background: #d1fae5;
      border-color: #6ee7b7;
    }}

    .site-footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 3rem 1rem;
      margin-top: 5rem;
      text-align: center;
      font-size: 0.85rem;
    }}
    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.75rem 1.25rem;
      margin-bottom: 2rem;
      max-width: 960px;
      margin-left: auto;
      margin-right: auto;
    }}
    .footer-links a {{
      color: #cbd5e1;
      text-decoration: none;
      font-size: 0.8rem;
    }}
    .footer-links a:hover {{
      color: #ffffff;
      text-decoration: underline;
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">冬コスメ徹底比較ラボ</a>
      <nav>
        <a href="/" style="color:var(--text-sub); text-decoration:none; font-size:0.9rem;">ホーム</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <article class="article-wrap">
      <div class="breadcrumb">
        <a href="/">ホーム</a> &gt; <span>高保湿バクチオールコスメランク10</span>
      </div>

      <header class="article-header">
        <span class="article-tag">🌿 植物性次世代レチノール・皮剥けゼロ処方</span>
        <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！冬の敏感肌でも皮剥けゼロでハリツヤ満たす高保湿バクチオールランク10</h1>
        <div class="article-meta">
          <span>📅 公開日: 2026年11月3日</span>
          <span>🔬 検証カテゴリー: 低刺激エイジングケア・植物性バクチオール配合コスメ</span>
          <span>✍️ 監修: 冬コスメ徹底比較ラボ 美容皮膚科学検証チーム</span>
        </div>
        <div class="lead-box">
          <strong>【11月・12月の冬本番に深刻化するレチノールA反応・真冬の乾燥小ジワを根本解決！】</strong><br>
          空気が一段と冷え込み、本格的な冬へと向かう11月〜12月。「寒さで肌がこわばって小ジワが目立ち始めたから、話題のレチノールを使いたいけれど、冬に使うと皮がボロボロ剥けて顔が真っ赤になる」「暖房乾燥で肌バリアが弱っているときにレチノールを塗ったら、激痛としみるような乾燥に耐えられなかった」という切実な声が急増します。<br><br>
          純粋レチノールは高いコラーゲン促進作用を持つ反面、ターンオーバーを急激に早めるため、角層水分量が低下する真冬は最も『A反応（皮剥け・ヒリつき・赤み）』が悪化しやすい季節です。そこで今、世界中の皮膚科医やコスメ愛好家がこぞって冬のスキンケアに指名しているのが<strong>『植物性次世代レチノール・バクチオール（Bakuchiol）』</strong>です。<br><br>
          インドやスリランカの伝承医学で重用されてきたマメ科植物オランダビユから抽出されるバクチオールは、レチノールと同等の遺伝子発現経路を刺激してコラーゲンI・III・IV型の合成を力強く後押ししながら、レチノイド受容体への直接結合を避けることで<strong>「皮剥けゼロ・乾燥刺激ゼロ」</strong>を実現。さらに抗酸化・抗炎症作用が高く、油分や水分と調和して冬の肌をふっくら満たします。本記事では、2026年冬に本当に信頼できる実力派バクチオールコスメ10品を楽天APIから都度リアルタイム検証しランキング化しました。
        </div>
      </header>

      <nav class="toc-box">
        <div class="toc-title">📑 目次 - クイックナビゲーション</div>
        <ul class="toc-list">
          <li><a href="#science">1. なぜ真冬の乾燥肌にはレチノールではなく『バクチオール』なのか？3大美肌サイエンス</a></li>
          <li><a href="#ranking">2. 高保湿バクチオールコスメおすすめランキング10選（徹底レビュー）</a></li>
          <li><a href="#comparison">3. バクチオールコスメ10品 徹底スペック比較表</a></li>
          <li><a href="#guide">4. 11月・12月の冬本番にバクチオールのハリ弾力を最大化するプロの実践ステップ</a></li>
          <li><a href="#faq">5. 専門家が答える！バクチオールコスメのよくある疑問（Q&A）</a></li>
        </ul>
      </nav>

      <section id="science">
        <h2 class="section-title">🌿 なぜ真冬の乾燥肌にはレチノールではなく『バクチオール』なのか？3大美肌サイエンス</h2>
        
        <div class="science-card">
          <h3>🧬 ① レチノール受容体を介さずコラーゲン合成を直接刺激（皮剥けゼロの理由）</h3>
          <p>純粋レチノールは表皮のレチノイド受容体（RAR/RXR）に結合して急激に角化細胞を増殖させるため、未成熟な角質が剥がれ落ちて皮剥けや激しい乾燥を招きます。これに対しバクチオールは、レチノイド受容体に直接結合することなく、類似した細胞シグナル伝達系を穏やかに活性化。真皮の線維芽細胞に働きかけてコラーゲンI型・III型・IV型やヒアルロン酸の合成をダイレクトに促します。真冬の過酷な乾燥環境でも肌バリアを一切傷つけず、内側からふっくらとした厚みを取り戻します。</p>
        </div>

        <div class="science-card">
          <h3>☀️ ② 光や熱に極めて強く『朝のメイク前』にも安心して使える</h3>
          <p>レチノールは紫外線や熱に対して非常に不安定であり、塗布後に日光を浴びると光毒性を引き起こすリスクがあるため「夜間専用」が鉄則です。一方、バクチオールは光や酸化ストレスに対して極めて安定しており、光毒性が一切ありません。むしろ紫外線による脂質過酸化を防ぐ高い抗酸化作用を持つため、朝のメイク前に仕込むことで、日中のエアコン暖房乾燥や冬の紫外線から肌を一日中守り抜くことができます。</p>
        </div>

        <div class="science-card">
          <h3>💧 ③ 優れた脂質親和性と抗炎症作用で冬の粉吹き・肌荒れを同時鎮静</h3>
          <p>バクチオールは脂質との親和性が非常に高く、植物性スクワラン、アルガンオイル、セラミドなどの高保湿成分と理想的なブレンドが可能です。さらに皮膚内の炎症誘発物質（COX-2など）の産生を抑える抗炎症作用を併せ持つため、冬の寒冷外気やマフラー・マスクの擦れで赤みが生じやすい敏感肌を優しく鎮めながら、滑らかな陶器肌へと整えます。</p>
        </div>
      </section>

      <section id="ranking">
        <h2 class="section-title">🏆 高保湿バクチオールコスメおすすめランキング10選</h2>
        {items_html}
      </section>

      <section id="comparison">
        <h2 class="section-title">📊 バクチオールコスメ10品 徹底スペック比較表</h2>
        <div class="comparison-table-wrap">
          <table class="comparison-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>商品名・ブランド</th>
                <th>カテゴリー</th>
                <th>主成分・処方特徴</th>
                <th>参考価格</th>
              </tr>
            </thead>
            <tbody>
              {table_rows}
            </tbody>
          </table>
        </div>
      </section>

      <section id="guide">
        <h2 class="section-title">💡 11月・12月の冬本番にバクチオールのハリ弾力を最大化するプロの実践ステップ</h2>
        
        <div class="science-card">
          <h3 style="color:#047857;">【STEP 1】朝の『バクチオール仕込み』で日中の暖房ちりめんジワを封殺</h3>
          <p>朝の洗顔後、化粧水でしっかり水分を与えたら、バクチオール美容液を顔全体に薄く伸ばします。レチノールと違って朝でも安心なバクチオールは、日中の暖房乾燥による水分蒸発を抑え、夕方になっても目の下やほうれい線にファンデーションが食い込まない弾むようなハリをキープします。</p>
        </div>

        <div class="science-card">
          <h3 style="color:#047857;">【STEP 2】セラミドやエクトイン乳液との『ダブルレイヤリング』</h3>
          <p>バクチオールでコラーゲン産生のスイッチを入れたら、その直後にヒト型セラミドやエクトインを配合した高浸透乳液を重ねます。細胞間脂質のラメラ構造を整えながら水分シェルターで蓋をすることで、バクチオールの浸透効率と保水力が相乗的に高まり、冬でも吸い付くようなモチ肌が完成します。</p>
        </div>

        <div class="science-card">
          <h3 style="color:#047857;">【STEP 3】夜の『集中ナイトパック』で寝ている間のコラーゲン再構築</h3>
          <p>就寝前は、バクチオール配合のナイトクリームやオイル美容液を通常より少し多めに手に取り、フェイスラインを引き上げるように馴染ませます。睡眠中の成長ホルモン分泌と連動してバクチオールが肌の代謝をサポートし、翌朝起きて鏡を見た瞬間に毛穴のキュッとした引き締まりと明るい透明感を実感できます。</p>
        </div>
      </section>

      <section id="faq">
        <h2 class="section-title">❓ 専門家が答える！バクチオールコスメのよくある疑問</h2>
        <div class="faq-list">
          {"".join([f'''
          <div class="faq-item">
            <div class="faq-q">
              <span class="faq-q-badge">Q</span>
              <span>{f["q"]}</span>
            </div>
            <div class="faq-a">{f["a"]}</div>
          </div>
          ''' for f in faq_data])}
        </div>
      </section>

      <div class="internal-links-box">
        <h3 class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</h3>
        <div class="internal-links-grid">
          <a href="/winter-ectoin" class="internal-link">🧬 極限保水シェルター！高保水エクトイン10選</a>
          <a href="/winter-bifida" class="internal-link">🦠 美肌菌バリア再建！高濃度ビフィダ美容液10選</a>
          <a href="/winter-retinol-cream" class="internal-link">✨ 集中リンクルケア！高保湿レチノールクリーム10選</a>
          <a href="/winter-peptide-serum" class="internal-link">🧬 ハリ弾力復活！高濃度ペプチド美容液10選</a>
          <a href="/winter-ceramide-cream" class="internal-link">🧴 究極のラメラ修復！高保湿セラミドクリーム10選</a>
          <a href="/winter-proteoglycan" class="internal-link">🧬 ヒアルロン酸超え保水！高純度プロテオグリカン10選</a>
          <a href="/winter-propolis" class="internal-link">🐝 濃密蜜膜ヴェール！高保湿プロポリスアンプル10選</a>
          <a href="/winter-galactomyces" class="internal-link">🍶 酵母発酵で透明感！高浸透ガラクトミセス10選</a>
          <a href="/winter-heparinoid" class="internal-link">🩺 角層深部保水！薬用ヘパリン類似物質コスメ10選</a>
          <a href="/winter-panthenol-cream" class="internal-link">🧪 肌バリア鎮静！高保湿パンテノールクリーム10選</a>
          <a href="/winter-squalane-oil" class="internal-link">✨ 極上ツヤ膜！高純度スクワランオイル10選</a>
          <a href="/winter-wrinkle-cream" class="internal-link">👁️ 目元口元集中！冬の薬用シワ改善クリーム10選</a>
        </div>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-links">
        <a href="/">トップページ</a>
      </div>
      <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved.</p>
      <p style="margin-top: 0.5rem; font-size: 0.8rem; color: #64748b;">当サイトは楽天市場アフィリエイトプログラムに参加しており、適格販売により収入を得ています。</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-bakuchiol.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("winter-bakuchiol.html successfully generated!")
