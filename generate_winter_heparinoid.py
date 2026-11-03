import json
import re

with open("fetched_3new_nov_dec_heparinoid_vaseline_placenta_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_heparinoid"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 コーセー×マルホ共同開発の金字塔！医薬部外品ヘパリン類似物質HD配合の高浸透化粧水",
        "catch": "角層ラメラ構造を根本から整える。冬の過酷な乾燥でも夕方までみずみずしさが持続する王道ローション",
        "brand_name": "Carte (カルテHD / コーセーマルホ)",
        "capacity": "150ml (モイスチュア ローション)",
        "type": "医薬部外品・高保湿薬用化粧水",
        "features": "保水有効成分ヘパリン類似物質HD、肌あれ防止有効成分グリチルリチン酸ジカリウム、うるおいバリアCPX（セラミド類似ポリマー・アミノ酸・スクワラン）",
        "value": "皮膚科領域のトップ製薬企業マルホとコーセーの先進製剤技術が融合。角層の水分保持能を根本からサポートし、乾燥を繰り返す肌に鉄壁の潤いバリアを再建する",
        "desc_p1": "11月から12月にかけて外気温が10度を下回り、暖房の稼働によって湿度が20%近くまで急落すると、肌の角層ラメラ構造が乱れて内部の水分が急速に蒸発します。カルテHDのモイスチュア ローションは、医療用保湿剤ヒルドイドの主成分として知られるマルホの保水有効成分『ヘパリン類似物質HD』を贅沢に配合した医薬部外品化粧水です。",
        "desc_p2": "とろみのあるエッセンスのようなまろやかな感触でありながら、肌の上に広げるとスルスルと角層深部へ吸い込まれるように浸透。肌あれ防止成分のグリチルリチン酸ジカリウムと、セラミド類似ポリマーを含む独自複合成分『うるおいバリアCPX』が相乗効果を発揮します。塗布した瞬間から肌がしっとりと柔らかく解きほぐされ、真冬のエアコン風にさらされても肌の内側からうるおいが湧き出るようなモチモチ感が持続します。",
        "target": "どれだけ化粧水を重ねても数時間で肌が乾燥する方、粉吹きやカサつきを繰り返す敏感肌・インナードライ肌の方、低刺激で高機能な冬用化粧水を求める方",
        "point": "洗顔後、手のひらに500円玉大を取り、手の体温で温めてから優しく包み込むようにハンドプレスします。目元や口元など乾燥しやすい部分には少量を重ねづけすると保水力がさらに高まります。"
    },
    {
        "rank": 2,
        "tag": "🥛 まるで美容液のような濃密まろやか質感！水分と油分を黄金バランスで届ける高保湿乳液",
        "catch": "肌をほぐしながら潤いを長時間閉じ込める。ゴワつく冬の角層をふっくら滑らかに満たす乳液",
        "brand_name": "Carte (カルテHD / コーセーマルホ)",
        "capacity": "120ml (モイスチュア エマルジョン)",
        "type": "医薬部外品・高保湿薬用乳液",
        "features": "保水有効成分ヘパリン類似物質HD、グリチルリチン酸ジカリウム、浸透型エモリエントオイル、無香料・無着色・アルコールフリー",
        "value": "水分を保持するヘパリン類似物質HDと、肌を柔らかく整える良質な油分を理想的なバランスで乳化。角層を柔軟化しながら潤いの持続膜を形成する",
        "desc_p1": "冬の寒さによって皮脂の分泌量が大幅に減少すると、肌表面の柔軟性が失われ、硬くゴワついた状態に陥ります。カルテHDのモイスチュア エマルジョンは、角層の水分を保持するヘパリン類似物質HDに加え、選び抜かれたエモリエントオイルを高濃度に配合した薬用乳液です。",
        "desc_p2": "コクのあるリッチなテクスチャーながら、肌になじませると驚くほど軽やかにのび広がり、ベタつきを残さずピタッと密着します。細胞間脂質を補うように浸透し、硬くなった角層を内側からふっくらと持ち上げます。化粧水で補給した水分を逃さず長時間密封するため、翌朝の洗顔時まで吸い付くようなモチ肌を保つことができます。メイク前の保湿乳液としてもヨレにくく非常に優秀です。",
        "target": "冬になると肌が硬くゴワつく方、乳液特有の油膜感やベタつきが苦手だが乾燥を防ぎたい方、キメを整えてメイクノリを改善したい方",
        "point": "化粧水の直後、手のひらに1円玉大を出し、両頬・額・鼻・あごの順に優しく伸ばします。手のひら全体でフェイスラインを引き上げるようにハンドプレスすると浸透と密着感が向上します。"
    },
    {
        "rank": 3,
        "tag": "🛡️ 濃密ヴェールで冷気と暖房を完全遮断！肌荒れループを断ち切る薬用高保湿クリーム",
        "catch": "ヘパリン類似物質HDと上質ワセリンの濃密シールド。真冬の粉吹き・ヒリつき肌を包み込み修復",
        "brand_name": "Carte (カルテHD / コーセーマルホ)",
        "capacity": "40g (モイスチュア クリーム)",
        "type": "医薬部外品・薬用高保湿クリーム",
        "features": "保水有効成分ヘパリン類似物質HD、抗炎症成分グリチルリチン酸ジカリウム、高純度ワセリン配合、弱酸性・低刺激処方",
        "value": "ヘパリン類似物質による角層深部保水と、高純度ワセリンによる肌表面の物理的シールドを両立。真冬の乾燥ダメージから肌を保護し抜く最上級のフタ",
        "desc_p1": "12月の真冬の冷風に晒されると、頬や口周りの皮膚がヒリヒリと痛み、粉を吹いて赤みを帯びることがあります。カルテHD モイスチュア クリームは、ヘパリン類似物質HDによる角層深部の保水作用と、保護効果の高い油性成分を贅沢にブレンドした濃厚クリームです。",
        "desc_p2": "指に取るとこっくりとした濃密な質感ですが、肌の温度でとろけるように伸び、保護ヴェールを肌表面に形成します。水分蒸散を物理的に抑え込みながら、内部ではヘパリン類似物質HDが乱れたラメラ構造を整え続けます。就寝前にたっぷり塗ることで、夜間の暖房乾燥から素肌を守り、朝起きたときの肌のしっとり感と弾力感に圧倒的な違いをもたらします。",
        "target": "目元や口元が粉を吹いて白くなる方、冷風やマスク摩擦で頬がヒリつく方、超乾燥肌で通常の乳液やジェルでは物足りない方",
        "point": "スキンケアの最終ステップとして、パール粒大を手に取り、乾燥が気になる部位を中心にスタンプを押すように優しく密着させます。擦らずに手のひらの体温で押し込むのが肌に負担をかけないコツです。"
    },
    {
        "rank": 4,
        "tag": "✨ 大正製薬の皮膚科学が凝縮！ヘパリン類似物質×水溶性プラセンタエキスの薬用W有効成分",
        "catch": "乾燥対策とシミ・くすみ対策を1本で。透明感と深い潤いを同時に手に入れる先進エイジング化粧水",
        "brand_name": "AdryS (大正製薬 アドライズ)",
        "capacity": "120ml (アクティブローション ディープモイスト)",
        "type": "医薬部外品・薬用美白＆高保湿化粧水",
        "features": "保湿有効成分ヘパリン類似物質、美白有効成分プラセンタエキス、セラミド、アミノ酸、シロキクラゲ多糖体",
        "value": "大正製薬が長年の医薬品研究から生み出した『保湿×美白』のハイブリッド設計。冬の乾燥枯れ肌を潤しながら、メラニン生成を抑えて透明美肌へ導く",
        "desc_p1": "冬は乾燥だけでなく、寒さによる血行不良や角層の乱れから肌の透明感が失われ、くすんで見えがちです。製薬大手・大正製薬が開発したアドライズ アクティブローション ディープモイストは、ヘパリン類似物質と水溶性プラセンタエキスという2つの有効成分を同時配合した革新的な薬用化粧水です。",
        "desc_p2": "ヘパリン類似物質が乱れた角層深部を潤し、シロキクラゲエキスなどの植物性高保水成分が水分を抱え込みます。さらにプラセンタエキスがメラニンの生成を抑制し、冬の乾燥くすみを一掃。濃厚でとろみのあるテクスチャーでありながら、肌に浸透した後はベタつかず、内側から発光するような自然なツヤとハリが宿ります。乾燥小ジワとくすみを同時にケアしたい大人の肌に最適な1本です。",
        "target": "冬になると肌のトーンが沈んでくすむ方、保湿だけでなくシミ・エイジングケアも同時に行いたい方、製薬会社の確かなエビデンスを重視する方",
        "point": "洗顔後、適量（500円玉大）を手のひらに取り、顔全体になじませます。くすみやすい目元や頬骨のあたりには、指の腹でトントンと優しく押し込むように重ねづけしてください。"
    },
    {
        "rank": 5,
        "tag": "🩺 マツキヨ発の大ヒット医薬品！ヘパリン類似物質0.3%配合の濃厚油性バリアクリーム",
        "catch": "乾燥肌治療の医療用成分をそのまま配合。ガサガサ・粉ふき・ひび割れを集中治療する実力派",
        "brand_name": "matsukiyo (マツキヨ)",
        "capacity": "80g (ヒルメナイド油性クリーム)",
        "type": "第2類医薬品・ヘパリン類似物質外用薬",
        "features": "有効成分ヘパリン類似物質0.3%配合、白色ワセリンベース、無香料・無着色・ステロイドフリー・エタノールフリー",
        "value": "ドラッグストア大手のマツキヨが一般用医薬品として開発。皮脂枯れや角化症が深刻な冬の重度乾燥肌を、高濃度ヘパリン類似物質と油性基剤で根本修復する",
        "desc_p1": "『ヒルドイドと同じ成分を市販で手軽に購入したい』という多くの乾燥肌の悩みに応えて誕生したマツキヨのプライベートブランド医薬品『ヒルメナイド油性クリーム』。医療用保湿剤と同等のヘパリン類似物質0.3%を配合した第2類医薬品です。",
        "desc_p2": "白色ワセリンをベースにした油性クリーム設計となっており、非常に高い密閉力と持続性を誇ります。塗布した部位にとどまり、外気の乾燥刺激を完全にシャットアウトしながら、ヘパリン類似物質が角層内部の血行を促進し、保水力を根本から再生します。顔のひどい乾燥スポットはもちろん、冬場にひび割れやすいかかと、ひじ、すねの粉吹きまで、家族全員で使える頼もしい大容量80gチューブです。",
        "target": "一般的な化粧品では乾燥が治まらない重度の乾燥肌の方、皮が剥けるほどの粉ふきに悩む方、医薬品としての確かな治療効果を求める方",
        "point": "患部を清潔にした後、1日数回、適量を優しくすり込むように塗布してください。夜の洗顔後、いつものスキンケアの一番最後に乾燥がひどい部位にピンポイントで重ねるナイトパック使いも効果的です。"
    },
    {
        "rank": 6,
        "tag": "🌿 ロート製薬のワセリンベース乳液！マイクロワセリン×ヘパリン類似物質で乾かない肌へ",
        "catch": "皮脂膜の働きを疑似再現。粉吹きやカサつきが気になる顔全体にスッと伸びる高保水ローション",
        "brand_name": "ロート製薬 (ヘパソフト)",
        "capacity": "100g (ヘパソフト 薬用 顔ローション)",
        "type": "医薬部外品・薬用高保湿顔用乳液",
        "features": "保水有効成分ヘパリン類似物質、抗炎症成分グリチルリチン酸ジカリウム、アラントイン、高圧乳化マイクロワセリン配合",
        "value": "ロート製薬独自の高圧乳化技術でワセリンを微粒子化。ベタつかない快適な使用感でありながら、ワセリンの保護膜とヘパリンの保水力を同時に届ける",
        "desc_p1": "顔の皮膚は薄く外気の影響を受けやすいため、冬の乾燥によって皮脂膜が薄れると一気に粉吹きやヒリつきが起こります。ロート製薬のヘパソフト薬用顔ローションは、乾燥肌の根本原因である『角層保水力の低下』と『皮脂膜の不足』に着目した顔用薬用ローションです。",
        "desc_p2": "微細化したマイクロワセリンが肌表面を優しく覆い、ヘパリン類似物質が角層深部へ浸透。さらにアラントインとグリチルリチン酸ジカリウムのW抗炎症成分が、乾燥によって生じた目に見えない微細な肌荒れを鎮めます。乳液のような滑らかな質感で白浮きせず、素早く肌になじむため、冬の朝のメイク前ケアにも最適。日中の乾燥崩れを劇的に防ぎます。",
        "target": "冬になると頬や眉間が粉を吹いてファンデーションが浮く方、ワセリンのベタつきが苦手だが保護力は欲しい方、男性の髭剃り後乾燥ケアにもおすすめ",
        "point": "朝晩の洗顔後、化粧水の後に1円玉大を手のひらに取り、顔全体に優しくなじませます。特に乾燥しやすい頬や口角周辺には、指先で重ねるように押さえると効果的です。"
    },
    {
        "rank": 7,
        "tag": "🧴 医薬部外品認可の全身高保湿ミルク！100mlでたっぷり使えるコスパ最強のヘパリン乳液",
        "catch": "さらっと伸びて角層の水分量を爆上げ。乾燥性敏感肌を健やかなふっくら肌へと整える",
        "brand_name": "StayFree (ステイフリー)",
        "capacity": "100ml (ヒルドプレミアム ミルクローション)",
        "type": "医薬部外品・薬用高保湿ミルクローション",
        "features": "有効成分ヘパリン類似物質、グリチルリチン酸ジカリウム、スクワラン、ヒアルロン酸、大容量100ml",
        "value": "薬用有効成分ヘパリン類似物質を配合しながら、日常使いしやすい価格と大容量を実現。顔だけでなくデコルテや首元の冬乾燥も惜しみなく集中ケア",
        "desc_p1": "顔のスキンケアだけでなく、冬場は首筋やデコルテ、腕などの乾燥も深刻化します。ステイフリーのヒルドプレミアム ミルクローションは、ヘパリン類似物質とグリチルリチン酸ジカリウムを配合した医薬部外品の高保湿ミルクです。",
        "desc_p2": "みずみずしいテクスチャーで伸びが良く、肌になじませるとスーッと浸透してベタつきを残しません。スクワランやヒアルロン酸が肌表面のうるおい膜をサポートし、しっとりとした柔らかな感触が続きます。無香料・無着色で肌に優しく、お風呂上がりの急激な乾燥を防ぐ全身用ミルクとしても非常に高い人気とリピート率を誇ります。",
        "target": "毎日たっぷり惜しみなく使えるヘパリンコスメを探している方、顔から首・デコルテまで一気に保湿したい方、軽やかな浸透感を好む方",
        "point": "入浴後や洗顔後、適量を手に取り、乾燥が気になる部分に優しく伸ばしてください。乾燥が激しい冬場は、化粧水の後に本品を重ね、さらに気になる箇所にクリームを塗るステップがおすすめです。"
    },
    {
        "rank": 8,
        "tag": "⚡ これ1つで化粧水・美容液・乳液・クリームが完了！ヘパリン類似物質配合の時短オールインワン",
        "catch": "忙しい朝や疲れた夜でも角層深部まで保水チャージ。みずみずしいプルプルゲルが肌を密封",
        "brand_name": "StayFree (ステイフリー)",
        "capacity": "100g (ヒルドプレミアム オールインワンゲル)",
        "type": "医薬部外品・薬用高保湿オールインワンゲル",
        "features": "有効成分ヘパリン類似物質、グリチルリチン酸ジカリウム、コラーゲン、ヒアルロン酸、高保水ポリマーゲル",
        "value": "ヘパリン類似物質の本格的な保水力をワンステップで実感できる高機能ゲル。冬の時短スキンケアでありながら手抜き感ゼロの濃密保湿を実現",
        "desc_p1": "冬のスキンケアは化粧水、美容液、乳液、クリームとステップが多くなりがちですが、仕事や家事で忙しい毎日では時間をかけられないこともあります。ヒルドプレミアム オールインワンゲルは、保水有効成分ヘパリン類似物質を贅沢に配合した薬用高機能ゲルです。",
        "desc_p2": "ぷるんとした弾力のあるジェルが、肌に伸ばすとみずみずしく崩れて角層深くまでうるおいを届けます。高保水ポリマーが肌表面に薄いヴェールを作り、水分を逃さずしっかり閉じ込めます。油分による重たさがないため、メイク前のスキンケアとしても相性抜群。夜はたっぷり塗ってスリーピングジェルパックとしても活用できます。",
        "target": "冬の乾燥ケアを1ステップで素早く済ませたい方、ベタつくクリームが苦手な脂性乾燥肌の方、夜の時短スキンケアを重視する方",
        "point": "洗顔後、さくらんぼ粒大を手に取り、顔全体に広げて優しくハンドプレスします。冬の夜は少し多めの量を顔全体に厚めに塗り、パックのようにして就寝すると翌朝驚くほどもっちりします。"
    },
    {
        "rank": 9,
        "tag": "💧 日医工が誇る高純度ヘパリン類似物質0.3%！サラサラなのに圧倒的に潤う医薬品ローション",
        "catch": "医療用保湿ローションと同じ浸透設計。浸透力が高く頭皮や背中などのカサつきにも自在に届く",
        "brand_name": "日医工 (ピアソンHP)",
        "capacity": "50g (ピアソンHP ローション)",
        "type": "第2類医薬品・ヘパリン類似物質ローション",
        "features": "有効成分ヘパリン類似物質0.3%（100g中0.3g含有）、グリセリン、ポリオキシエチレン硬化ヒマシ油、無香料・無着色",
        "value": "ジェネリック医薬品大手の製薬技術。乳白色のサラッとしたローションが、硬くなった角質層へ瞬時に浸透し、肌の水分保持能を改善・血行促進",
        "desc_p1": "クリームやバームのこってりした使用感が苦手な方や、ベタつきを嫌う部位の保湿に最適なのが、日医工の『ピアソンHPローション』です。ヘパリン類似物質0.3%を配合した第2類医薬品で、医療機関で処方されるローション剤と極めて近い使用感を実現しています。",
        "desc_p2": "乳白色のさらりとした液体で、肌にのせると素早く浸透し、表面に一切のベタつきを残しません。それでいて数分後には内側から肌がしっとりと柔らかく整い、乾燥によるつっぱり感が解消されます。顔はもちろん、冬場に乾燥してかゆみが出やすい頭皮の生え際や首の後ろ、背中など、全身の広範囲のケアにもストレスなく使えます。",
        "target": "ベタつくテクスチャーが一切苦手な方、医薬品基準の確実なヘパリン類似物質を取り入れたい方、頭皮や首筋など毛髪周辺の乾燥にも使いたい方",
        "point": "1日数回、適量を手のひらに取り、患部に優しくなじませてください。容器の口が細いため、手のひらに少量ずつ出して押し込むように塗布するのがこぼさず綺麗に塗るポイントです。"
    },
    {
        "rank": 10,
        "tag": "🎯 目元・口元の深刻な乾燥小ジワをピンポイント密封！持ち歩ける超高密着ヘパリンバーム",
        "catch": "体温でとろけてピタッと密着。日中の暖房乾燥やメイク直しのレスキューにも大活躍",
        "brand_name": "Carte (カルテHD / コーセーマルホ)",
        "capacity": "15g (モイスチュア バーム)",
        "type": "医薬部外品・薬用高密着バーム",
        "features": "保水有効成分ヘパリン類似物質HD、抗炎症成分グリチルリチン酸ジカリウム、高純度ワセリンを高密度配合、スリムチューブ容器",
        "value": "外出先やオフィスでの急激な乾燥に対応できる部分用高保湿バーム。メイクの上からでもヨレずに使え、真冬の乾燥小ジワを瞬時にカバー＆密封",
        "desc_p1": "朝にしっかり保湿しても、暖房が効いたオフィスや屋外の冷風にさらされると、夕方には目元や口元のファンデーションがひび割れることがあります。カルテHD モイスチュア バームは、いつでもどこでもヘパリン類似物質HDを補給できる部分用の高密着薬用バームです。",
        "desc_p2": "チューブから出したときはしっかりとした固さがありますが、指の体温で温めると瞬時にとろけて密着オイルへと変化。高純度ワセリンとヘパリン類似物質HDが、激しく動く目元や口元にもぴったりフィットし、表情の動きでヨレることなく潤いを保護し続けます。ポーチに入るスリムサイズで、真冬のお守りコスメとして手放せない逸品です。",
        "target": "日中オフィスで目元や口周りの乾燥が気になる方、メイクの上から保湿できるバームを探している方、ポーチに入れて持ち歩きたい方",
        "point": "米粒半分ほどの少量を指先に取り、体温で温めてから、乾燥が気になる目尻や口角、ほうれい線周辺にトントンと優しく置くようになじませます。擦らないのがメイクを崩さない秘訣です。"
    }
]

# JSON-LD構造化データ作成
faq_data = [
    {
        "q": "ヘパリン類似物質とはどのような成分ですか？ヒアルロン酸やセラミドとの違いは何ですか？",
        "a": "ヘパリン類似物質は、体内のヘパリンという糖類に似た構造を持つ保水成分です。一般的なヒアルロン酸が『水分を抱え込む』、セラミドが『細胞間の隙間を埋めて水分の蒸発を防ぐ』のに対し、ヘパリン類似物質は『角層深部に浸透して乱れたラメラ構造を整え、肌内部の保水能を立て直す』とともに、血行促進作用と抗炎症作用を併せ持つ点が大きな違いです。11月・12月の冷えと過酷な乾燥で機能低下した冬の肌に最も根本的なアプローチができます。"
    },
    {
        "q": "医薬品（第2類医薬品）と医薬部外品（薬用コスメ）のヘパリン類似物質はどう使い分けるべきですか？",
        "a": "『皮が剥けて赤みがある、ひび割れて痛むなどの重度な症状がある時』は、治療を目的とした第2類医薬品（ヒルメナイドやピアソンHPなど）を患部に集中的に使用するのが適しています。一方、『毎日の朝晩スキンケアとして顔全体を潤し、キメを整え美肌を維持したい時』は、美容保湿成分やテクスチャーが美肌用に最適化された医薬部外品コスメ（カルテHDやアドライズなど）を使用するのが理想的です。"
    },
    {
        "q": "ヘパリン類似物質コスメを使うと血行促進で顔が赤くなることはありますか？",
        "a": "ヘパリン類似物質には血行促進作用があるため、塗布後にほんのり温かみを感じたり血色が良くなることがあります。ただし、目に見えて赤みが引かない場合や痒み・刺激がある場合は使用を中止し皮膚科専門医にご相談ください。敏感肌の方は、まず腕の内側などでパッチテストを行ってから顔に使用することをおすすめします。"
    },
    {
        "q": "ビタミンC美容液やレチノールなど、他のエイジングケア成分と一緒に使っても大丈夫ですか？",
        "a": "併用して全く問題ありません。むしろヘパリン類似物質が角層の水分量を大幅に底上げしバリア機能を強固に整えるため、レチノールや高濃度ビタミンCによる乾燥や刺激感を和らげるクッション役として非常に相性が良いです。使用順序としては、化粧水（ヘパリン類似物質）→ビタミンC/レチノール美容液→乳液・クリームの順がおすすめです。"
    },
    {
        "q": "11月〜12月の冬本番にヘパリン類似物質コスメを取り入れる最適なステップは？",
        "a": "朝晩の洗顔直後の化粧水、または乳液ステップでの導入が最も効果的です。角層が乾燥で硬化している冬場は、まずカルテHDなどのヘパリン類似物質化粧水で水分を角層深部へ引き込み、乳液やクリームで油分ヴェールを重ねることで、暖房直撃の過酷な室内環境でも一日中乾燥知らずのうるおい肌をキープできます。"
    }
]

schema_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！角層深部の保水構造を立て直す薬用ヘパリン類似物質コスメランク10",
    "description": "11月・12月の真冬乾燥に！角層深部から水分保持能を立て直す薬用ヘパリン類似物質コスメ10選を徹底比較。カルテHD、アドライズ、ヒルメナイド、ヘパソフト、ピアソンHPなど厳選。",
    "image": items[0]["img_url"],
    "datePublished": "2026-11-03T10:00:00+09:00",
    "dateModified": "2026-11-03T10:00:00+09:00",
    "author": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ 編集部",
        "url": "https://lumi-cosme.vercel.app/"
    },
    "publisher": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ",
        "logo": {
            "@type": "ImageObject",
            "url": "https://lumi-cosme.vercel.app/favicon.jpg"
        }
    },
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://lumi-cosme.vercel.app/winter-heparinoid"
    }
}

schema_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": it["rank"],
            "name": it["name"],
            "item": {
                "@type": "Product",
                "name": it["name"],
                "image": it["img_url"],
                "offers": {
                    "@type": "Offer",
                    "priceCurrency": "JPY",
                    "price": str(it["price"]),
                    "availability": "https://schema.org/InStock",
                    "url": it["affiliate_url"]
                }
            }
        } for it in items
    ]
}

schema_faq = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": f["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f["a"]
            }
        } for f in faq_data
    ]
}

schema_breadcrumb = {
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
            "name": "薬用ヘパリン類似物質コスメランク10",
            "item": "https://lumi-cosme.vercel.app/winter-heparinoid"
        }
    ]
}

# HTML構築
items_html = ""
for idx, p in enumerate(product_details):
    it = items[idx]
    price_str = f"¥{it['price']:,}" if it['price'] > 0 else "オープン価格"
    
    items_html += f"""
    <!-- Rank {p['rank']} -->
    <div class="product-card" id="rank-{p['rank']}">
      <div class="product-rank-badge">第{p['rank']}位</div>
      <div class="product-header">
        <span class="product-tag">{p['tag']}</span>
        <h3 class="product-title">{p['catch']}</h3>
        <div class="product-meta">
          <span class="product-brand">ブランド: {p['brand_name']}</span>
          <span class="product-capacity">規格・容量: {p['capacity']}</span>
          <span class="product-type">タイプ: {p['type']}</span>
        </div>
      </div>

      <div class="product-body">
        <div class="product-img-wrap">
          <img src="{it['img_url']}" alt="{it['name']}" class="product-img" loading="lazy">
        </div>
        <div class="product-info">
          <div class="product-price-box">
            <span class="price-label">楽天市場参考価格:</span>
            <span class="price-val">{price_str}</span>
            <span class="price-tax">(税込・送料込目安)</span>
          </div>
          <div class="product-features">
            <strong>有効成分・処方特徴:</strong> {p['features']}
          </div>
          <div class="product-value-point">
            <strong>冬の高保湿アプローチ:</strong> {p['value']}
          </div>
        </div>
      </div>

      <div class="product-desc">
        <p class="desc-lead">{p['desc_p1']}</p>
        <p class="desc-detail">{p['desc_p2']}</p>
      </div>

      <div class="product-advice-grid">
        <div class="advice-box target-box">
          <div class="advice-title">💡 こんな肌悩みの方に最適</div>
          <p>{p['target']}</p>
        </div>
        <div class="advice-box usage-box">
          <div class="advice-title">🧴 保湿効果を最大化する使用法</div>
          <p>{p['point']}</p>
        </div>
      </div>

      <div class="product-cta">
        <a href="{it['affiliate_url']}" class="rakuten-btn" target="_blank" rel="noopener nofollow">
          楽天市場で詳細・最安値をチェック <span>→</span>
        </a>
      </div>
    </div>
    """

# 比較テーブル作成
table_rows = ""
for idx, p in enumerate(product_details):
    it = items[idx]
    price_str = f"¥{it['price']:,}" if it['price'] > 0 else "オープン価格"
    table_rows += f"""
    <tr>
      <td class="tbl-rank">第{p['rank']}位</td>
      <td class="tbl-name"><a href="#rank-{p['rank']}">{p['brand_name']}<br><strong>{p['capacity']}</strong></a></td>
      <td class="tbl-type">{p['type']}</td>
      <td class="tbl-feat">{p['features']}</td>
      <td class="tbl-price">{price_str}</td>
    </tr>
    """

# 記事全体の完全HTMLコード
full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！角層深部の保水構造を立て直す薬用ヘパリン類似物質コスメランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬本番に深刻化するインナードライ・粉吹き乾燥を根本解決！角層深部の水分保持能を立て直す薬用ヘパリン類似物質コスメ10選を徹底比較！カルテHD、アドライズ、ヒルメナイド、ヘパソフト、ピアソンHPなど厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-heparinoid">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- OGP -->
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！角層深部の保水構造を立て直す薬用ヘパリン類似物質コスメランク10 | 冬コスメ徹底比較ラボ">
  <meta property="og:description" content="11月・12月の冬本番に深刻化するインナードライ・粉吹き乾燥を根本解決！角層深部の水分保持能を立て直す薬用ヘパリン類似物質コスメ10選を徹底比較！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-heparinoid">
  <meta property="og:image" content="{items[0]['img_url']}">
  <meta name="twitter:card" content="summary_large_image">

  <!-- JSON-LD 構造化データ -->
  <script type="application/ld+json">
  {json.dumps(schema_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(schema_itemlist, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(schema_faq, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(schema_breadcrumb, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #0284c7;
      --primary-light: #e0f2fe;
      --primary-dark: #0369a1;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --bg-light: #f8fafc;
      --border-color: #e2e8f0;
      --accent-coral: #0284c7;
      --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --card-hover-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text-main);
      background-color: #f1f5f9;
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
      max-width: 1000px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .site-logo {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--primary-dark);
      text-decoration: none;
    }}

    .container {{
      max-width: 900px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}

    .article-wrap {{
      background: #ffffff;
      padding: 3rem 2.5rem;
      border-radius: 12px;
      box-shadow: var(--card-shadow);
    }}

    .breadcrumb {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
    }}

    .breadcrumb a {{
      color: var(--primary-dark);
      text-decoration: none;
    }}

    .article-title {{
      font-size: 1.85rem;
      line-height: 1.4;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 1.5rem;
    }}

    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 2rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid var(--border-color);
    }}

    .lead-box {{
      background: #f0f9ff;
      border-left: 4px solid var(--primary);
      padding: 1.5rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 2.5rem;
      font-size: 1.05rem;
      line-height: 1.8;
    }}

    .section-title {{
      font-size: 1.4rem;
      font-weight: 700;
      color: #0f172a;
      margin: 3rem 0 1.5rem 0;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 2rem;
      margin-bottom: 3rem;
      position: relative;
      box-shadow: var(--card-shadow);
      transition: box-shadow 0.2s ease;
    }}

    .product-card:hover {{
      box-shadow: var(--card-hover-shadow);
    }}

    .product-rank-badge {{
      position: absolute;
      top: -12px;
      left: 20px;
      background: linear-gradient(135deg, #0284c7, #0369a1);
      color: #ffffff;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 0.25rem 1rem;
      border-radius: 20px;
      box-shadow: 0 2px 4px rgba(2, 132, 199, 0.3);
    }}

    .product-header {{
      margin-top: 0.5rem;
      margin-bottom: 1.5rem;
    }}

    .product-tag {{
      display: inline-block;
      font-size: 0.85rem;
      font-weight: 700;
      color: #0369a1;
      background: #e0f2fe;
      padding: 0.2rem 0.6rem;
      border-radius: 4px;
      margin-bottom: 0.5rem;
    }}

    .product-title {{
      font-size: 1.3rem;
      font-weight: 700;
      line-height: 1.4;
      color: #0f172a;
      margin-bottom: 0.5rem;
    }}

    .product-meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    .product-body {{
      display: grid;
      grid-template-columns: 240px 1fr;
      gap: 2rem;
      margin-bottom: 1.5rem;
    }}

    @media (max-width: 640px) {{
      .product-body {{
        grid-template-columns: 1fr;
      }}
      .article-wrap {{
        padding: 2rem 1.25rem;
      }}
      .article-title {{
        font-size: 1.5rem;
      }}
    }}

    .product-img-wrap {{
      text-align: center;
      background: #f8fafc;
      padding: 1rem;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .product-img {{
      max-width: 100%;
      max-height: 220px;
      object-fit: contain;
      border-radius: 4px;
    }}

    .product-info {{
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 0.75rem;
    }}

    .product-price-box {{
      background: #f8fafc;
      padding: 0.75rem 1rem;
      border-radius: 6px;
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
    }}

    .price-label {{
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    .price-val {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #b91c1c;
    }}

    .price-tax {{
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    .product-features, .product-value-point {{
      font-size: 0.95rem;
      line-height: 1.6;
    }}

    .product-desc {{
      margin: 1.5rem 0;
      font-size: 0.95rem;
      line-height: 1.8;
      color: #334155;
    }}

    .desc-lead {{
      margin-bottom: 1rem;
      font-weight: 500;
    }}

    .product-advice-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-bottom: 1.5rem;
    }}

    @media (max-width: 640px) {{
      .product-advice-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .advice-box {{
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.9rem;
      line-height: 1.6;
    }}

    .target-box {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      color: #166534;
    }}

    .usage-box {{
      background: #fdf2f8;
      border: 1px solid #fbcfe8;
      color: #9d174d;
    }}

    .advice-title {{
      font-weight: 700;
      margin-bottom: 0.35rem;
    }}

    .product-cta {{
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
      font-weight: 700;
      font-size: 1rem;
      padding: 0.85rem 2rem;
      border-radius: 50px;
      text-decoration: none;
      box-shadow: 0 4px 6px -1px rgba(191, 0, 0, 0.25);
      transition: all 0.2s ease;
      width: 100%;
      max-width: 420px;
    }}

    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 12px -2px rgba(191, 0, 0, 0.35);
      background: linear-gradient(135deg, #d60000, #aa0000);
    }}

    .comparison-table-wrap {{
      overflow-x: auto;
      margin: 2rem 0;
    }}

    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      background: #ffffff;
    }}

    .comparison-table th, .comparison-table td {{
      padding: 0.85rem 0.75rem;
      border: 1px solid var(--border-color);
      text-align: left;
    }}

    .comparison-table th {{
      background: #f8fafc;
      color: #0f172a;
      font-weight: 700;
      white-space: nowrap;
    }}

    .tbl-rank {{
      font-weight: 700;
      color: var(--primary-dark);
      white-space: nowrap;
      text-align: center;
    }}

    .tbl-name a {{
      color: #0f172a;
      text-decoration: none;
    }}

    .tbl-name a:hover {{
      color: var(--primary);
    }}

    .tbl-price {{
      font-weight: 700;
      color: #b91c1c;
      white-space: nowrap;
    }}

    .faq-list {{
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      margin: 2rem 0;
    }}

    .faq-item {{
      background: #f8fafc;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 1.25rem;
    }}

    .faq-q {{
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 0.5rem;
      display: flex;
      gap: 0.5rem;
    }}

    .faq-q-badge {{
      background: var(--primary);
      color: #ffffff;
      font-size: 0.75rem;
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      height: fit-content;
    }}

    .faq-a {{
      color: #475569;
      font-size: 0.95rem;
      line-height: 1.7;
    }}

    .internal-links-box {{
      background: #f8fafc;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.5rem;
      margin-top: 3rem;
    }}

    .internal-links-title {{
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 1rem;
      color: #0f172a;
    }}

    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 0.75rem;
    }}

    .internal-link {{
      color: #0369a1;
      text-decoration: none;
      font-size: 0.85rem;
      padding: 0.4rem 0.6rem;
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 6px;
      transition: all 0.2s;
    }}

    .internal-link:hover {{
      background: #e0f2fe;
      border-color: #7dd3fc;
    }}

    .site-footer {{
      background: #ffffff;
      border-top: 1px solid var(--border-color);
      padding: 2rem 0;
      margin-top: 4rem;
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">冬コスメ徹底比較ラボ</a>
      <nav>
        <a href="/" style="text-decoration: none; color: #475569; font-size: 0.9rem; font-weight: 600;">TOPへ戻る</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <article class="article-wrap">
      <nav class="breadcrumb">
        <a href="/">ホーム</a> &gt; <span>薬用ヘパリン類似物質コスメ高保湿ランク10</span>
      </nav>

      <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！角層深部の保水構造を立て直す薬用ヘパリン類似物質コスメランク10</h1>

      <div class="article-meta">
        <span>更新日: 2026年11月3日</span>
        <span>検証カテゴリー: 薬用高保湿・ヘパリン類似物質</span>
        <span>監修: 冬コスメ徹底比較ラボ 編集部</span>
      </div>

      <div class="lead-box">
        <strong>【11月・12月の冬本番に深刻化するインナードライ・粉吹き乾燥を根本解決！】</strong><br>
        外気温が急降下し、オフィスや自宅のエアコン暖房が本格稼働する11月〜12月。「どれだけ化粧水や高保湿クリームを重ねても、夕方になると肌がパリパリに突っ張る」「粉を吹いてファンデーションがまだらに崩れる」という深刻な肌枯れに悩まされる方が急増します。<br><br>
        その根本原因は、寒冷刺激と極端な湿度の低下によって、肌の細胞間脂質（ラメラ構造）が崩れ、角層自体の水分保持機能が破綻してしまうことにあります。単に表面に油分を塗るだけの対症療法では、蒸発していく水分を食い止めることはできません。<br><br>
        そこで今冬、美容のプロや皮膚科医からも絶大な支持を集めているのが<strong>『ヘパリン類似物質』</strong>を配合した薬用コスメです。角層深部まで浸透して乱れた保水構造を根本から立て直し、血行促進と抗炎症のトリプルアプローチで健やかな潤い肌を育てる、2026年最新の厳選10品を徹底検証・ランキング化しました。
      </div>

      <h2 class="section-title">🧪 ヘパリン類似物質が冬の過酷な乾燥肌を救う3大メカニズム</h2>
      <div style="margin-bottom: 2.5rem; font-size: 0.95rem; line-height: 1.8; color: #334155;">
        <p>ヘパリン類似物質は、人の体内に存在する保水物質「ヘパリン」に類似した高分子多糖類です。数十年にわたり皮膚科領域で乾燥性皮膚疾患の治療薬として用いられてきた歴史を持ち、近年では医薬部外品スキンケアとしての実用化が進み、冬のデイリーケアとして取り入れられるようになりました。一般的な保湿成分と比較して以下の3つの決定的な強みを持ちます。</p>
        <ul style="margin: 1rem 0 1rem 1.5rem;">
          <li><strong>1. 角層深部の保水構造（ラメラ構造）再建：</strong> 水分子を引き寄せて抱え込む力が極めて高く、壊れたラメラ構造の隙間にすり抜けるように浸透して水分を強固に留めます。</li>
          <li><strong>2. 寒冷による血行不良の改善：</strong> 11月〜12月の寒さで滞りがちな毛細血管の末梢血流を穏やかに促し、肌細胞へ酸素と栄養を行き渡らせてターンオーバーを正常化します。</li>
          <li><strong>3. 暖房乾燥・摩擦による微小炎症の鎮静：</strong> 乾燥が引き起こす微小な角層炎症を鎮静化し、赤みやヒリヒリ感、粉吹きといった肌トラブルの悪循環を断ち切ります。</li>
        </ul>
      </div>

      <h2 class="section-title">🏆 薬用ヘパリン類似物質コスメ高保湿おすすめランキング10選</h2>

      {items_html}

      <h2 class="section-title">📊 薬用ヘパリン類似物質コスメ10品 徹底スペック比較表</h2>
      <div class="comparison-table-wrap">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名・容量</th>
              <th>種別・タイプ</th>
              <th>有効成分・主処方</th>
              <th>参考価格</th>
            </tr>
          </thead>
          <tbody>
            {table_rows}
          </tbody>
        </table>
      </div>

      <h2 class="section-title">💡 11月・12月の冬本番に効果を倍増させるヘパリンコスメの正しい使い方</h2>
      <div style="margin-bottom: 2.5rem; font-size: 0.95rem; line-height: 1.8; color: #334155;">
        <p>ヘパリン類似物質コスメの保水力を最大限に活かすためには、冬の環境に合わせたステップと使い方のコツを押さえることが重要です。</p>
        <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; margin-top: 1rem;">
          <h3 style="font-size: 1.05rem; margin-bottom: 0.5rem; color: #0284c7;">① 洗顔後3分以内の水分補給が鉄則</h3>
          <p>冬のお風呂上がりや洗顔後は、室内の暖房によって急速に水分が蒸発していきます。タオルで優しく水分を拭き取った直後の毛穴が開いているうちに、カルテHDなどのヘパリン類似物質ローションを手で温めてから優しく包み込むようになじませてください。</p>
          <h3 style="font-size: 1.05rem; margin: 1rem 0 0.5rem; color: #0284c7;">② 水分補給後は乳液・クリームで必ず油膜シールド</h3>
          <p>ヘパリン類似物質が角層内部の水分を捕まえた後、そのまま放置すると冬の乾燥した外気に水分が奪われます。エマルジョンやクリーム、高純度ワセリンバームを重ねて「水分補給＋油分密閉」のダブルシールドを完成させましょう。</p>
          <h3 style="font-size: 1.05rem; margin: 1rem 0 0.5rem; color: #0284c7;">③ 擦らず「手のひらプレス」で浸透させる</h3>
          <p>冬の乾燥した肌は角質がめくれ上がり、摩擦に対して極めて敏感です。コットンで強く擦るパッティングは避け、手のひら全体で優しく肌を包み込み、体温でじっくり押し込むハンドプレスを意識してください。</p>
        </div>
      </div>

      <h2 class="section-title">❓ 専門家が答える！薬用ヘパリン類似物質コスメのよくある質問</h2>
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

      <div class="internal-links-box">
        <h3 class="internal-links-title">🔗 あわせて読みたい冬の高保湿スキンケア・コスメ特集</h3>
        <div class="internal-links-grid">
          <a href="/winter-rice-power" class="internal-link">🌾 米発酵・ライスパワー高保湿10選</a>
          <a href="/winter-ceramide-lotion" class="internal-link">🧴 高保湿セラミド化粧水10選</a>
          <a href="/winter-ceramide-cream" class="internal-link">🧴 高保湿セラミドクリーム10選</a>
          <a href="/winter-vaseline" class="internal-link">🛡️ 高純度ワセリン高保湿10選</a>
          <a href="/winter-placenta" class="internal-link">✨ 高濃度プラセンタ原液10選</a>
          <a href="/winter-amino-acid" class="internal-link">💧 高浸透アミノ酸コスメ10選</a>
          <a href="/winter-squalane-oil" class="internal-link">✨ 高純度スクワランオイル10選</a>
          <a href="/winter-argan-oil" class="internal-link">🥑 高保湿アルガンオイル10選</a>
          <a href="/winter-panthenol-cream" class="internal-link">🧪 高保湿パンテノールクリーム10選</a>
          <a href="/winter-horse-oil" class="internal-link">🐴 高保湿馬油クリーム10選</a>
          <a href="/winter-shea-butter" class="internal-link">🧈 高保湿シアバター10選</a>
          <a href="/winter-urea-cream" class="internal-link">🦶 高保湿尿素クリーム10選</a>
          <a href="/winter-medicinal-lip" class="internal-link">💄 高保湿薬用リップクリーム10選</a>
          <a href="/winter-peptide-serum" class="internal-link">🧬 高保湿ペプチド美容液10選</a>
        </div>
      </div>

    </article>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved.</p>
      <p style="margin-top: 0.5rem; font-size: 0.8rem; color: #94a3b8;">当サイトは楽天市場アフィリエイトプログラムに参加しており、適格販売により収入を得ています。</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-heparinoid.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-heparinoid.html!")
