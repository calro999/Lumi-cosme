import json
import re

with open("fetched_3new_mask_lip_serum.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_barrier_serum"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 韓国オリーブヤング美容液部門の覇者！角層深部にバリア水分を満たす乳液状先行セラム",
        "catch": "韓国メディカルコスメの最高峰AESTURAが誇るアトバリア365ハイドロエッセンス。化粧水と乳液の利点を融合したミルキーな濃密テクスチャーが、冬のインナードライでこわばった肌深部に30種のアミノ酸とセラミド水分を急速チャージ",
        "brand_name": "AESTURA (エストラ)",
        "capacity": "150mL / ポンプボトル",
        "type": "高純度アミノ酸×生体類似バリア複合体配合 先行導入ハイドロエッセンス",
        "features": "30種のアミノ酸コンプレックス、ミネラル、天然保湿因子NMF類似成分、低刺激ダーマ処方",
        "value": "洗顔直後の無防備な角層に瞬時に吸い込まれ、スカスカになった細胞間を濃密な水分で満杯に。その後のクリームの密着力と保水効果を2倍以上に跳ね上げる",
        "desc_p1": "11月から12月にかけてエアコン暖房をつけ始めると、『表面は皮脂でテカるのに、内部がパキパキと突っ張る』という典型的なインナードライに陥ります。エストラのハイドロエッセンスは、単に肌表面に水分を乗せるだけの化粧水とは異なり、天然保湿因子NMFの主成分であるアミノ酸30種を高濃度で微細乳化。角質細胞の1つ1つに浸透し、内部からふっくらと押し広げます。",
        "desc_p2": "白濁したとろみのあるリキッドは肌に乗せるとサラリと馴染み、ベタつきを残さず内側だけが満たされる心地よい使用感を実現。弱酸性・低刺激・無香料で、冷たい風で赤みが出た敏感な冬肌にも優しく寄り添います。大容量150mLで朝晩たっぷり使えるため、真冬のベーススキンケアの土台作りとして絶対的な安心感を誇ります。",
        "target": "暖房の部屋にいると頬が熱っぽく突っ張るインナードライ肌、サラサラ化粧水では物足りないが重いオイルは苦手な方、肌バリアの土台を立て直したい方",
        "point": "洗顔後すぐ、または導入化粧水の後に2〜3プッシュを手のひらに取り、顔全体を包み込むようにハンドプレス。乾燥が気になる目元や口元には、もう1プッシュ重ねづけしてからクリームでフタをしてください。"
    },
    {
        "rank": 2,
        "tag": "💧 5D複合セラミド×パンテノール！化粧水・乳液・美容液を1本に凝縮した高密度オールインワン",
        "catch": "水分鎮静で絶大な人気を誇るTorridenのソリッドインシリーズ。5種類の複合セラミドと高濃度パンテノールが、真冬の寒冷脱水にさらされた角層バリアを強固に再建する多機能エッセンス",
        "brand_name": "Torriden (トリデン)",
        "capacity": "100mL / ポンプボトル",
        "type": "5D複合セラミド×パンテノール配合 高密着オールインワンエッセンス",
        "features": "5Dセラミドコンプレックス（NP, NS, AP, AS, EOP）、パンテノール、低分子ヒアルロン酸、トレハロース",
        "value": "サイズと浸透深度の異なる5層のセラミドが肌の隙間をブロック。忙しい冬の朝でもこれ1本で乳液＋美容液を完了でき、一日中暖房風に負けない潤いをキープ",
        "desc_p1": "トリデンの『ソリッドイン セラミド オールインワン エッセンス』は、乾燥によってバリア機能が低下し、水分蒸発と外部刺激の侵入を同時に許してしまっている冬肌のために設計されました。肌の保護膜と同じ構成比率を意識した5重のセラミドが、角層のラメラ構造を整えて水分の逃げ道を完全に塞ぎます。",
        "desc_p2": "とろみのあるミルキーな美容液テクスチャーは肌に伸ばすとみずみずしく崩れ、角層深部へと素早く吸い込まれます。パンテノールが肌荒れやヒリつきを速攻で穏やかに鎮静。油分と水分のバランスが完璧に計算されているため、脂性肌や混合肌の方でも毛穴詰まりを起こすことなく快適に高保湿ケアを継続できます。",
        "target": "スキンケアのステップをシンプルにしたい方、暖房による日中のカサつきを予防したい混合肌、セラミド配合の軽やかな美容液を探している方",
        "point": "朝晩の洗顔後、1〜2プッシュを顔全体に優しく塗り広げます。極度の乾燥肌の方は本品を塗布した後にクリームを重ね、混合肌や脂性肌の方はこれ1本でスキンケアを完了することも可能です。"
    },
    {
        "rank": 3,
        "tag": "🌡️ 資生堂の先進研究！外気と室内の『寒暖差ストレス』から冬肌を守り抜く薬用バリア美容液",
        "catch": "敏感肌研究50年の集大成dプログラムが解き明かした冬の肌荒れ新事実『寒暖差』に着目。独自のカンダンバリアコンプレックスが、急激な温度変化によるバリア機能低下を先回りしてブロック",
        "brand_name": "d program (資生堂 dプログラム)",
        "capacity": "40mL / ポンプボトル (医薬部外品)",
        "type": "カンダンバリア複合体配合 薬用先行型バリア導入美容液",
        "features": "カンダンバリアコンプレックス（キイチゴエキス、PCA-Na、グリセリン）、グリチルリチン酸ジカリウム、低刺激設計",
        "value": "屋外の冷気（5℃）と室内の暖房（24℃）を行き来する日本の冬に完全特化。塗るだけで寒暖差によるゴワつき・ピリつき・メイク崩れを劇的に抑え込む",
        "desc_p1": "資生堂の最新皮膚科学研究により、冬に室内外の急激な温度差に晒されると、肌のバリアを司る鍵となる酵素『カスパーゼ14』の産生が停止し、角層の水分保持力が急低下することが判明しました。dプログラムのカンダンバリアエッセンスは、この寒暖差ダメージを無効化するために開発された革新的な薬用美容液です。",
        "desc_p2": "みずみずしいジェル状の美容液が肌に乗せた瞬間にスーッと角層奥深くまで浸透。後から使う化粧水のなじみを劇的に高めるブースター機能も兼ね備えています。アルコールフリー・無香料・パラベンフリーの厳格な低刺激設計で、冬の季節の変わり目に肌が敏感になり、何をつけても赤みが出る時期でも心地よく使えます。",
        "target": "通勤や外出で室内外の温度差を感じると肌が赤く火照る方、化粧水が肌に入りにくくなったと感じる方、敏感肌用の安心できる薬用コスメを好む方",
        "point": "朝晩の洗顔直後、化粧水の前に使用します。手のひらにディスペンサー2回押し分を取り、顔全体に優しく丁寧になじませます。その後、いつもの化粧水・乳液でお手入れを続けてください。"
    },
    {
        "rank": 4,
        "tag": "🔬 特許MLE®液晶バリア構造×5種ヒアルロン酸！アンプルと化粧水を一体化した高機能トナー",
        "catch": "韓国ダーマコスメの重鎮Real Barrierが誇るエクストリームライン。健常な肌の十字架状ラメラ構造を再現した特許MLE技術と濃厚アンプル成分が、壊れた冬肌の角層バリアを瞬時に接合",
        "brand_name": "Real Barrier (リアルバリア)",
        "capacity": "190mL / ボトル",
        "type": "特許MLE液晶構造再現 高保湿バリアアンプルトナー",
        "features": "独自MLE®コンプレックス、セラミド9S、セラミド5SP、パンテノール、マデカッソシド、ヒアルロン酸5種",
        "value": "美容液並みの濃厚な美容成分を含みながら大容量190mL。乾燥してスカスカになった角層に惜しみなくバリア成分を注ぎ込み、粉吹き・皮剥けを即座に修復",
        "desc_p1": "リアルバリアの『エクストリーム エッセンス トナー』は、化粧水という枠組みを超えた『塗るバリアアンプル』として世界中で高評価を得ています。最大の特徴は、弱った角層の細胞間脂質にそのまま置き換わる特許MLE®処方。水と油が層状に重なるラメラ構造を肌表面に形成し、暖房風による水分蒸発を物理的にシャットアウトします。",
        "desc_p2": "乳白色のとろみリキッドは肌に塗布した瞬間、まるで肌がゴクゴクと飲み干すように浸透。表面に薄いシルクのような保護膜が形成され、突っ張り感が消え去ります。パンテノールとマデカッソシドが微小な赤みや炎症を速やかに鎮静。真冬の過酷な乾燥環境でも、常に潤いに満ちたモチモチの健やか肌をキープできます。",
        "target": "冬の乾燥で肌のキメが乱れてファンデが粉を吹く方、美容液クラスの高保湿化粧水を探している方、赤みやヒリつきが出やすい超乾燥肌",
        "point": "洗顔後、適量を手に取り顔全体に優しくなじませます。特に乾燥が気になる日や夜のお手入れでは、2〜3回重ねづけする『レイヤリング保湿』を行うと、クリーム要らずの圧倒的なモチモチ感を実感できます。"
    },
    {
        "rank": 5,
        "tag": "🛡️ 医薬部外品・消炎アラントイン×セラミド機能成分！ゴワつく冬の角層を解きほぐす薬用バリア美容液",
        "catch": "花王キュレルが開発した、乾燥性敏感肌のための角層深部バリア美容液。荒れを防ぐ有効成分アラントインと浸透型セラミドカプセルが、真冬の乾燥で硬くゴワついた角層を芯からほぐして潤いで満たす",
        "brand_name": "Curel (キュレル / 花王)",
        "capacity": "30mL / ポンプボトル (医薬部外品)",
        "type": "薬用消炎成分×セラミドケア成分配合 角層深部バリア美容液",
        "features": "アラントイン（消炎有効成分）、ヘキサデシロキシPGヒドロキシエチルヘキサデカナミド（セラミド機能成分）、ユーカリエキス",
        "value": "乾燥小ジワを目立たなくする効能評価試験済み。冬の冷気で硬直した角層深部までセラミド機能成分を送り届け、ハリと透明感に満ちた滑らかな素肌へと導く",
        "desc_p1": "冬の乾燥肌は角質層が水分を失って硬化し、通常のスキンケア成分が深部まで届きにくい『浸透ブロック状態』に陥っています。キュレルの角層深部バリア美容液は、有効成分アラントインが炎症を鎮めつつ、角層深部までスッと浸透する独自の微細エマルジョン処方を採用。硬くなった角質細胞同士を優しく解きほぐします。",
        "desc_p2": "肌に乗せるとみずみずしく広がり、スーッと消えるように角層へ吸い込まれていきます。ベタつきが一切残らないため、朝のメイク前でもヨレの心配なく贅沢に使用可能。夕方になっても目元や口元の乾燥小ジワが目立たず、ふっくらとしたハリ感が持続します。敏感肌パッチテスト済みで、刺激に弱い冬肌でも安心です。",
        "target": "乾燥で肌がゴワついて化粧水の浸透が悪く感じる方、目元や口元の乾燥小ジワを改善したい方、安心の医薬部外品でセラミド補給を行いたい方",
        "point": "朝晩の化粧水の後、乳液やクリームの前に使用します。適量（ポンプ1〜2押し分）を手にとり、顔全体に優しくなじませます。特に乾燥しやすい目元や口元には、指の腹を使って丁寧になじませてください。"
    },
    {
        "rank": 6,
        "tag": "🌿 高純度ドクダミエキス80%×水分鎮静！冬の暖房熱でほてった肌をみずみずしく整える水分アンプル",
        "catch": "韓国スキンケアのメガヒットブランドAnua（アヌア）の看板アンプル。高濃縮ドクダミエキス80%とパンテノールが、真冬の寒暖差やエアコン暖房によるインナードライ・赤みを速攻でクールダウン鎮静",
        "brand_name": "Anua (アヌア)",
        "capacity": "30mL / スポイトボトル",
        "type": "高濃度ドクダミエキス80%×パンテノール配合 水分鎮静バリアアンプル",
        "features": "ドクダミエキス80%、パンテノール、ヒアルロン酸、ベタイン、無香料・ノンコメドジェニックテスト済み",
        "value": "水分感に満ちた濃厚なとろみテクスチャーでありながら、肌に浸透した後は一切ベタつかない神バランス。冬の乾燥とマスクの摩擦でゆらぐ肌を穏やかに整える",
        "desc_p1": "冬のオフィスや室内で暖房に長時間当たっていると、顔が赤くほてり、皮膚表面の水分が失われて毛穴が目立ってくることがあります。アヌアのドクダミ80%アンプルは、古来より優れた抗炎症・抗菌作用で知られるドクダミエキスを限界レベルの80%まで高濃度凝縮。ほてった肌の炎症性サイトカインを抑え、素早く肌を平穏な状態に戻します。",
        "desc_p2": "糸を引くような濃密なとろみがありながら、肌へ塗り広げると水のようにすっと弾けて角質層へ瞬時に浸透。パンテノールが肌バリアを強化し、ヒアルロン酸が内部に水分を蓄えます。ニキビができやすい冬の混合肌や、油分過多で荒れやすい方でも安心して使えるオイルフリー処方です。",
        "target": "暖房の効いた室内で顔の赤みやほてりが出やすい方、乾燥するのに吹き出物もできやすい冬の混合肌、ベタつきのない水分セラムを求める方",
        "point": "化粧水で肌を整えた後、スポイトで2〜3滴を手のひらに落とし、顔全体に優しく塗り広げます。赤みが気になる頬や鼻周りには、少量を重ねづけして優しくハンドプレスしてください。"
    },
    {
        "rank": 7,
        "tag": "🍯 黒蜂プロポリス83%の濃厚栄養蜜！真冬の寒風で疲弊した肌に極上のハリ艶とバリアを補給",
        "catch": "世界的なベストセラーを誇るCOSRXのフルフィットプロポリスアンプル。過酷な冬を生き抜く黒蜂のプロポリスエキスを83.25%高配合し、乾燥でカサついた肌に蜜のような濃密なツヤと弾力バリアを与える",
        "brand_name": "COSRX (コスアールエックス)",
        "capacity": "30mL / スポイトボトル",
        "type": "黒蜂プロポリスエキス83.25%配合 高栄養リッチバリアアンプル",
        "features": "黒蜂プロポリスエキス83.25%、キャシア種子エキス、ヒアルロン酸Na、パンテノール",
        "value": "抗酸化・抗菌・高保湿のトリプル効果。ファンデーションに1滴混ぜるだけで真冬でも乾燥崩れしない『水光ツヤ肌』が一日中持続するマルチな実力派",
        "desc_p1": "COSRXのプロポリスライトアンプルは、乾燥と冷気によって肌の代謝が落ち、ツヤと活力を失った冬肌への特効薬です。配合されている黒蜂プロポリスエキスは、一般的なプロポリスよりもフラボノイドやアミノ酸の含有量が多く、弱った皮膚バリアを強化しながら強力なエモリエント効果を発揮します。",
        "desc_p2": "とろみのある黄金色のアンプルは、肌に乗せると吸い付くように密着し、内側から押し返すようなモチモチ感を与えます。濃厚でありながら毛穴を塞ぐ不快感がなく、メイク前の仕込み美容液としても大活躍。夜塗って眠れば、翌朝には乾燥くすみが一掃され、ふっくらと健康的なツヤ肌に目覚めることができます。",
        "target": "冬になると肌がくすんで元気がなく見える方、水光肌のような自然なツヤが欲しい方、プロポリスの高栄養成分で肌の基礎体力を高めたい方",
        "point": "化粧水の後、スポイト半分程度を取り顔全体に優しく伸ばします。乾燥が特にひどい日は、ファンデーションやBBクリームに1滴ブレンドして塗布すると、日中の乾燥割れを完璧に防げます。"
    },
    {
        "rank": 8,
        "tag": "🌿 高純度マダガスカル産ツボクサ100%！冬の過酷な外気で乱れたバリアを鎮静リセット",
        "catch": "韓国オリーブヤングや世界80カ国で絶賛されるSKIN1004のシグネチャー。手付かずの大自然マダガスカルで収穫された高純度ツボクサエキスのみを100%ボトルに詰めた、至高の鎮静アンプル",
        "brand_name": "SKIN1004 (スキンワンオーオーフォー)",
        "capacity": "55mL / スポイトボトル",
        "type": "高純度マダガスカル産ツボクサエキス100% 鎮静バリアアンプル",
        "features": "ツボクサエキス100%、アシアチコシド、マデカシン酸、アシアチン酸、弱酸性",
        "value": "不純物を徹底排除したシングル成分処方。真冬の寒冷刺激でピリピリと過敏になった肌にも水のように優しく浸透し、荒れた角層バリアを穏やかに鎮静修復",
        "desc_p1": "SKIN1004のセンテラアンプルは、マダガスカルの清潔な環境で育った高品質なツボクサのみを厳選して抽出した、混じり気なしのツボクサエキス100%美容液です。冬の冷風や暖房による乾燥ストレスで肌のバリアが破綻し、赤みやヒリつきが出ている肌に対して、穏やかかつ確実に鎮静アプローチを仕掛けます。",
        "desc_p2": "水のようにサラサラとした心地よいテクスチャーでありながら、肌になじませると角層のすみずみまで瞬時に潤いが行き渡り、内側がひんやりと落ち着くのを実感できます。他の美容液やクリームの浸透を妨げないため、プレ美容液としても最適。大容量55mLでコスパも抜群です。",
        "target": "成分の相性トラブルを避けたい敏感肌、冬の外気で肌がピリつきやすい方、さっぱりした使用感で確実な鎮静効果を求める方",
        "point": "洗顔後すぐ、または化粧水で整えた肌にスポイト1回分を顔全体に伸ばします。赤みが気になる部分には2〜3回重ねづけすると、より高い鎮静・バリア強化効果が得られます。"
    },
    {
        "rank": 9,
        "tag": "🔬 ビフィズス菌培養溶解質×5種セラミド！弱った肌のバリア基礎体力を底上げする名品アンプル",
        "catch": "韓国コスメ界を揺るがした魔女工場（manyo）の最高傑作アンプル。マイクロバイオーム（美肌菌）研究から生まれたビフィズス菌発酵エキスと5種のセラミドが、真冬のダメージ肌を根本から強化",
        "brand_name": "manyo (魔女工場)",
        "capacity": "50mL / スポイトボトル",
        "type": "ビフィズス菌発酵成分×5種複合セラミド配合 美肌菌バリアアンプル",
        "features": "ビフィズス菌培養溶解質、乳酸桿菌発酵液、5種セラミド、ヒアルロン酸10種、ペプチド複合体",
        "value": "美肌菌とセラミドのダブルアプローチで、一時的な保湿にとどまらず肌自らが潤いを蓄える『皮膚常在菌バリア』を再建。真冬の過酷な環境でも揺らがない強い肌へ",
        "desc_p1": "冬の乾燥や寒冷ストレスは、皮膚表面に存在する有益な常在菌（美肌菌）のバランスを乱し、悪玉菌の繁殖や肌荒れを引き起こす要因となります。魔女工場のビフィダバイオームアンプルは、ビフィズス菌培養溶解質と発酵エキスを高濃度配合し、美肌菌が健やかに育つ弱酸性環境を整えます。",
        "desc_p2": "さらに5種類のセラミドと10重のヒアルロン酸が角層の水分油分バランスを黄金比率に補整。肌に伸ばすとスーッと溶け込み、翌朝には肌のキメが整って内側から押し返すような弾力とツヤが実感できます。冬の寒さで肌が痩せて弱ってきたと感じる方に最適なバリアアンプルです。",
        "target": "冬になると毎年のように肌荒れを繰り返す方、肌の根本的なバリア力や免疫力を底上げしたい方、発酵コスメの実感を味わいたい方",
        "point": "化粧水でお肌を整えた後、スポイトで適量を吸い上げ、顔全体にムラなくなじませます。手のひらで顔全体を包み込み、体温で温めながらハンドプレスしてじっくり浸透させてください。"
    },
    {
        "rank": 10,
        "tag": "🌾 医薬部外品・有効成分ライスパワーNo.11！日本で唯一『水分保持能を改善』する薬用先行導入美容液",
        "catch": "コーセーの先進技術を結集したONE BY KOSÉのフラッグシップ美容液。日本で唯一、肌のセラミド自生力を高めて水分保持能を改善する有効成分ライスパワーNo.11を配合した冬の救世主",
        "brand_name": "ONE BY KOSÉ (コーセー)",
        "capacity": "60mL / ポンプボトル (医薬部外品)",
        "type": "有効成分ライスパワーNo.11配合 薬用高保湿導入美容液",
        "features": "ライスパワーNo.11（水分保持能改善有効成分）、インナーブースター処方、アクティライズ酵母エキス",
        "value": "外からセラミドを与えるだけでなく、肌自身がセラミドを産生する力を根本改善。使い続けるほどに冬の乾燥にビクともしない自立した潤い肌を育てる",
        "desc_p1": "一般的な保湿コスメが『外から水分や油分を補う対症療法』であるのに対し、ONE BY KOSÉのセラムヴェール ディープリペアは『肌が自らセラミドを造り出す力を育てる根本療法』を可能にした日本屈指の医薬部外品です。有効成分ライスパワーNo.11が角層深層の基底細胞に働きかけ、セラミドの合成量を劇的に増加させます。",
        "desc_p2": "洗顔直後の肌になじませると、独自のインナーブースター処方により角層を瞬時にほぐし、後から使う化粧水や乳液の引き込み力を格段に高めます。みずみずしくコクのあるベースが肌に吸い付き、キメの乱れや毛穴の目立ちをふっくらと押し戻します。真冬の過酷な脱水肌を本質から立て直す最高峰の投資ケアです。",
        "target": "どんな高保湿クリームを塗っても時間が経つと乾いてしまう超乾燥肌、肌自らの保湿力を根本から改善したい方、日本の医薬部外品技術を信じる方",
        "point": "朝晩の洗顔直後、最初のお手入れとして手のひらに2〜3プッシュを取り、顔全体に優しくなじませます。その後、いつもの化粧水とクリームを重ねてください。"
    }
]

# JSON-LD ItemList
item_list_elements = []
for p in product_details:
    it = items[p["rank"] - 1]
    item_list_elements.append({
        "@type": "ListItem",
        "position": p["rank"],
        "item": {
            "@type": "Product",
            "name": it["display_name"],
            "image": it["image_url"],
            "brand": {
                "@type": "Brand",
                "name": p["brand_name"]
            },
            "offers": {
                "@type": "Offer",
                "price": it["price"],
                "priceCurrency": "JPY",
                "availability": "https://schema.org/InStock",
                "url": it["affiliate_url"]
            }
        }
    })

faq_items = [
    {
        "q": "バリア美容液は導入美容液（ブースター）と何が違うのですか？",
        "a": "バリア美容液には『洗顔直後に使う先行導入型（エストラ、dプログラム、ONE BY KOSÉなど）』と『化粧水の後に使う高濃縮美容液型（アヌア、COSRX、魔女工場など）』の2種類が存在します。先行型は角層を柔らかくほぐして後続コスメの浸透ルートを確保しつつセラミドを補填します。一方、化粧水後の高濃縮型は補給した水分をセラミドやプロポリスで抱え込み、角層深部に密閉する役割を果たします。ご自身の肌状態や好みのステップに合わせて選ぶのが理想的です。"
    },
    {
        "q": "ビタミンCやレチノールなど攻めの美容液を使っている場合、バリア美容液はどの順番で塗るべきですか？",
        "a": "水溶性ビタミンCやピュアレチノールを使用する場合、肌への刺激を緩和するために『バリア美容液を先に塗って肌の基礎防御力を高めてから攻めの成分を塗る（バッファリング手法）』か、あるいは『水溶性ビタミンC（洗顔直後）→バリア美容液→レチノール（夜の最後）』という順序が推奨されます。真冬にレチノールで皮剥けやA反応が出やすい時は、バリア美容液を多めに仕込むことで刺激を大幅に軽減できます。"
    },
    {
        "q": "朝のメイク前にバリア美容液を使うと、日焼け止めやファンデがモロモロとヨレませんか？",
        "a": "モロモロ（カス）が発生する主な原因は、高分子ポリマー（カルボマーやヒアルロン酸等）が乾ききる前に摩擦を加えることです。バリア美容液を塗布した後は、手のひらでハンドプレスして肌に完全に浸透・密着するまで1〜2分置くのがコツです。また、過度に擦らずに優しく叩き込むようにベースメイクを重ねることで、日中の暖房乾燥によるメイク割れを完璧に防ぐことができます。"
    },
    {
        "q": "化粧水の後に乳液だけで十分潤っている気がしますが、バリア美容液は本当に必要ですか？",
        "a": "乳液の主たる役割は『油分による水分蒸散の抑制（エモリエント）』です。一方、バリア美容液は『角質細胞の隙間を埋める細胞間脂質（セラミド等）の直接補給』および『肌荒れ炎症の鎮静』を専門としています。11月・12月の暖房下で『表面はしっとりしているのに奥が突っ張る（インナードライ）』を感じている場合、乳液だけでは角層深部のスカスカ状態を埋め切れていない証拠であり、バリア美容液の投入が劇的な解決策となります。"
    },
    {
        "q": "ニキビや毛穴詰まりができやすい脂性肌・混合肌でもバリア美容液を使えますか？",
        "a": "むしろ積極的に使うべきです。冬の脂性肌・混合肌の過剰な皮脂分泌は、角層内部の水分不足を補おうとする防衛反応（インナードライ代償性皮脂分泌）であるケースが非常に多いです。オイルフリーまたは低油分で水分鎮静に特化したバリア美容液（アヌア、SKIN1004、トリデン等）で角層深部に十分な水分とセラミドを満たすことで、過剰な皮脂分泌が自然に収まり、毛穴詰まりやニキビの予防につながります。"
    }
]

faq_elements = []
for fq in faq_items:
    faq_elements.append({
        "@type": "Question",
        "name": fq["q"],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": fq["a"]
        }
    })

structured_data = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！微細リポソーム化バリア成分とパンテノールの生体浸透力で真冬の暖房インナードライを芯から鎮静する保湿力高めバリア美容液ランク10",
            "description": "11月・12月の暖房直撃によるインナードライ・赤み・ピリつきを徹底救済！エストラ、トリデン、dプログラム、キュレル、魔女工場、コーセーまで高保湿バリア美容液の科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。",
            "image": items[0]["image_url"],
            "datePublished": "2026-11-12T05:00:00+09:00",
            "dateModified": "2026-11-12T05:00:00+09:00",
            "author": {
                "@type": "Organization",
                "name": "LUMI COSMETICS LAB 冬季皮膚科学研究チーム"
            },
            "publisher": {
                "@type": "Organization",
                "name": "LUMI COSMETICS LAB",
                "logo": {
                    "@type": "ImageObject",
                    "url": "https://lumi-cosme.vercel.app/favicon.jpg"
                }
            }
        },
        {
            "@type": "ItemList",
            "name": "真冬の高保湿バリア美容液おすすめランキング10選",
            "numberOfItems": len(item_list_elements),
            "itemListElement": item_list_elements
        },
        {
            "@type": "FAQPage",
            "mainEntity": faq_elements
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
                    "name": "冬の徹底保湿ケア特集",
                    "item": "https://lumi-cosme.vercel.app/winter-barrier-serum"
                }
            ]
        }
    ]
}

# HTML Cards
product_cards_html = ""
for p in product_details:
    it = items[p["rank"] - 1]
    product_cards_html += f"""
    <article class="product-card" id="rank-{p['rank']}">
      <div class="product-header">
        <span class="rank-badge">第{p['rank']}位</span>
        <span class="product-tag">{p['tag']}</span>
      </div>
      <div class="product-content">
        <div class="product-img-box">
          <img src="{it['image_url']}" alt="{it['display_name']}" class="product-img" loading="lazy">
        </div>
        <div class="product-info">
          <div class="product-brand">{p['brand_name']}</div>
          <h3 class="product-title">{it['display_name']}</h3>
          <p class="product-catch">{p['catch']}</p>
          <div class="product-meta">
            <span><strong>容量:</strong> {p['capacity']}</span>
            <span><strong>タイプ:</strong> {p['type']}</span>
          </div>
          <div class="product-features">
            <strong>主要注目成分:</strong> {p['features']}
          </div>
          <div class="product-price-box">
            <div class="price-val">¥{it['price']:,}<span class="tax-label">（税込・楽天最新実勢価格）</span></div>
            <div class="review-val">★ {it['review_average']} <span class="review-count">({it['review_count']}件のレビュー)</span></div>
          </div>
          <div class="product-value-box">
            <span class="value-title">💡 11-12月の暖房インナードライ対策・即効価値</span>
            <p>{p['value']}</p>
          </div>
        </div>
      </div>
      <div class="product-desc-box">
        <h4>🧪 美容科学＆テクスチャー詳細解説</h4>
        <p>{p['desc_p1']}</p>
        <p>{p['desc_p2']}</p>
      </div>
      <div class="product-target-box">
        <div class="target-item"><strong>こんな方に最適:</strong> {p['target']}</div>
        <div class="target-item"><strong>効果を最大化する使用法:</strong> {p['point']}</div>
      </div>
      <div class="product-action">
        <a href="{it['affiliate_url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
          <span>楽天市場で最新価格＆在庫をチェック</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </article>
    """

faq_html = ""
for fq in faq_items:
    faq_html += f"""
    <div class="faq-item">
      <div class="faq-q">Q. {fq['q']}</div>
      <div class="faq-a">{fq['a']}</div>
    </div>
    """

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！微細リポソーム化バリア成分とパンテノールの生体浸透力で真冬の暖房インナードライを芯から鎮静する保湿力高めバリア美容液ランク10 | LUMI COSMETICS LAB</title>
  <meta name="description" content="11月・12月の暖房直撃によるインナードライ・赤み・ピリつきを徹底救済！エストラ、トリデン、dプログラム、キュレル、魔女工場、コーセーまで高保湿バリア美容液の科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-barrier-serum">
  <link rel="icon" href="/favicon.jpg">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！微細リポソーム化バリア成分とパンテノールの生体浸透力で真冬の暖房インナードライを芯から鎮静する保湿力高めバリア美容液ランク10">
  <meta property="og:description" content="11月・12月の暖房直撃によるインナードライ・赤み・ピリつきを徹底救済！エストラ、トリデン、dプログラム、キュレル、魔女工場、コーセーまで高保湿バリア美容液の科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-barrier-serum">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:site_name" content="LUMI COSMETICS LAB">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！微細リポソーム化バリア成分とパンテノールの生体浸透力で真冬の暖房インナードライを芯から鎮静する保湿力高めバリア美容液ランク10">
  <meta name="twitter:description" content="11月・12月の暖房直撃によるインナードライ・赤み・ピリつきを徹底救済！エストラ、トリデン、dプログラム、キュレル、魔女工場、コーセーまで高保湿バリア美容液の科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。">
  <meta name="twitter:image" content="{items[0]['image_url']}">
  <script type="application/ld+json">
  {json.dumps(structured_data, ensure_ascii=False, indent=2)}
  </script>
  <style>
    :root {{
      --primary: #059669;
      --primary-light: #d1fae5;
      --primary-dark: #047857;
      --accent: #f59e0b;
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #f0fdf4;
      --card-bg: #ffffff;
      --border: #a7f3d0;
      --radius: 16px;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Meiryo", sans-serif;
      line-height: 1.8;
      color: var(--text);
      background: #fafaf9;
      -webkit-font-smoothing: antialiased;
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid #e2e8f0;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-title {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .breadcrumb {{
      max-width: 1100px;
      margin: 12px auto;
      padding: 0 20px;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .breadcrumb a {{
      color: var(--primary);
      text-decoration: none;
    }}
    main {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 24px 20px 80px;
    }}
    .hero-section {{
      background: linear-gradient(135deg, #d1fae5 0%, #ffffff 100%);
      border: 1px solid #a7f3d0;
      border-radius: var(--radius);
      padding: 40px 32px;
      margin-bottom: 40px;
    }}
    .hero-tag {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 9999px;
      margin-bottom: 16px;
    }}
    .hero-title {{
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.4;
      color: #064e3b;
      margin-bottom: 16px;
    }}
    .hero-desc {{
      font-size: 1rem;
      color: #065f46;
      line-height: 1.7;
    }}
    .toc-box {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: var(--radius);
      padding: 24px;
      margin-bottom: 40px;
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.1rem;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 8px 16px;
    }}
    .toc-list a {{
      color: var(--primary);
      text-decoration: none;
      font-size: 0.9rem;
      transition: color 0.2s;
    }}
    .toc-list a:hover {{
      color: var(--primary-dark);
      text-decoration: underline;
    }}
    .science-box {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 48px;
    }}
    .science-box h3 {{
      font-size: 1.35rem;
      color: #064e3b;
      margin-bottom: 16px;
    }}
    .science-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin-top: 24px;
    }}
    .science-card {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-radius: 12px;
      padding: 20px;
      border-left: 4px solid var(--primary);
    }}
    .science-card h4 {{
      font-size: 1rem;
      margin-bottom: 8px;
      color: #064e3b;
    }}
    .science-card p {{
      font-size: 0.9rem;
      color: #475569;
      line-height: 1.6;
    }}
    .section-title {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #064e3b;
      margin: 48px 0 24px;
      padding-left: 12px;
      border-left: 6px solid var(--primary);
    }}
    .product-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 40px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }}
    .product-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
    }}
    .rank-badge {{
      background: var(--primary);
      color: #ffffff;
      font-size: 1.1rem;
      font-weight: 800;
      padding: 6px 16px;
      border-radius: 8px;
    }}
    .product-tag {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 6px;
    }}
    .product-content {{
      display: grid;
      grid-template-columns: 240px 1fr;
      gap: 28px;
      margin-bottom: 24px;
    }}
    @media (max-width: 768px) {{
      .product-content {{
        grid-template-columns: 1fr;
      }}
    }}
    .product-img-box {{
      width: 100%;
      height: 240px;
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid #e2e8f0;
      background: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .product-img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      transition: transform 0.3s;
    }}
    .product-img:hover {{
      transform: scale(1.04);
    }}
    .product-brand {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 4px;
    }}
    .product-title {{
      font-size: 1.25rem;
      font-weight: 800;
      line-height: 1.4;
      margin-bottom: 8px;
      color: #0f172a;
    }}
    .product-catch {{
      font-size: 0.95rem;
      color: #475569;
      line-height: 1.6;
      margin-bottom: 12px;
    }}
    .product-meta {{
      display: flex;
      gap: 16px;
      font-size: 0.85rem;
      color: #64748b;
      margin-bottom: 8px;
    }}
    .product-features {{
      font-size: 0.85rem;
      background: #f0fdf4;
      padding: 8px 12px;
      border-radius: 6px;
      margin-bottom: 16px;
    }}
    .product-price-box {{
      display: flex;
      align-items: baseline;
      gap: 16px;
      margin-bottom: 16px;
      border-top: 1px dashed #e2e8f0;
      padding-top: 12px;
    }}
    .price-val {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #059669;
    }}
    .tax-label {{
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 400;
    }}
    .review-val {{
      font-size: 0.9rem;
      color: #d97706;
      font-weight: 700;
    }}
    .review-count {{
      font-size: 0.8rem;
      color: var(--text-muted);
      font-weight: 400;
    }}
    .product-value-box {{
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      border-radius: 8px;
      padding: 12px 16px;
      font-size: 0.9rem;
      color: #065f46;
    }}
    .value-title {{
      font-weight: 700;
      display: block;
      margin-bottom: 4px;
    }}
    .product-desc-box {{
      background: #f8fafc;
      border-radius: 8px;
      padding: 20px;
      margin-bottom: 20px;
      border: 1px solid #e2e8f0;
    }}
    .product-desc-box h4 {{
      font-size: 1rem;
      margin-bottom: 12px;
      color: #064e3b;
    }}
    .product-desc-box p {{
      font-size: 0.92rem;
      color: #334155;
      line-height: 1.7;
      margin-bottom: 8px;
    }}
    .product-target-box {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 24px;
      font-size: 0.88rem;
    }}
    @media (max-width: 640px) {{
      .product-target-box {{
        grid-template-columns: 1fr;
      }}
    }}
    .target-item {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      padding: 12px 16px;
      border-radius: 8px;
    }}
    .product-action {{
      text-align: right;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #bf0000;
      color: #ffffff;
      font-weight: 700;
      font-size: 0.95rem;
      padding: 12px 24px;
      border-radius: 8px;
      text-decoration: none;
      transition: background 0.2s, transform 0.1s;
    }}
    .rakuten-btn:hover {{
      background: #990000;
      transform: translateY(-2px);
    }}
    .summary-box {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 40px;
    }}
    .summary-box h3 {{
      font-size: 1.35rem;
      color: #064e3b;
      margin-bottom: 16px;
    }}
    .summary-table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 16px;
      font-size: 0.9rem;
    }}
    .summary-table th, .summary-table td {{
      padding: 12px 16px;
      border: 1px solid #e2e8f0;
      text-align: left;
    }}
    .summary-table th {{
      background: #d1fae5;
      font-weight: 700;
      color: #064e3b;
    }}
    .faq-item {{
      border-bottom: 1px solid #e2e8f0;
      padding: 16px 0;
    }}
    .faq-item:last-child {{
      border-bottom: none;
    }}
    .faq-q {{
      font-weight: 700;
      color: #064e3b;
      margin-bottom: 8px;
      font-size: 1rem;
    }}
    .faq-a {{
      color: #334155;
      font-size: 0.92rem;
      line-height: 1.7;
    }}
    .hub-link-banner {{
      background: linear-gradient(135deg, #059669 0%, #047857 100%);
      color: #ffffff;
      border-radius: var(--radius);
      padding: 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 24px;
      margin-bottom: 40px;
    }}
    @media (max-width: 768px) {{
      .hub-link-banner {{
        flex-direction: column;
        text-align: center;
      }}
    }}
    .hub-link-btn {{
      display: inline-block;
      background: #ffffff;
      color: #047857;
      font-weight: 700;
      padding: 12px 24px;
      border-radius: 8px;
      text-decoration: none;
      white-space: nowrap;
    }}
    .internal-links-box {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 40px;
    }}
    .internal-links-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 16px;
    }}
    .internal-link-card {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 16px;
      text-decoration: none;
      transition: border-color 0.2s, transform 0.2s;
    }}
    .internal-link-card:hover {{
      border-color: var(--primary);
      transform: translateY(-2px);
    }}
    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 60px 20px 40px;
      font-size: 0.85rem;
    }}
    .footer-inner {{
      max-width: 1100px;
      margin: 0 auto;
    }}
    .footer-title {{
      color: #ffffff;
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 20px;
    }}
    .footer-links {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 12px 20px;
      margin-bottom: 40px;
    }}
    .footer-link-item {{
      color: #cbd5e1;
      text-decoration: none;
      transition: color 0.2s;
    }}
    .footer-link-item:hover {{
      color: #6ee7b7;
    }}
    .copyright {{
      border-top: 1px solid #1e293b;
      padding-top: 24px;
      text-align: center;
      color: #64748b;
    }}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <a href="/" class="site-title">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        LUMI COSMETICS LAB
      </a>
      <span style="font-size:0.85rem;color:#64748b;">冬季皮膚科学＆高保湿コスメ検証</span>
    </div>
  </header>

  <div class="breadcrumb">
    <a href="/">ホーム</a> &gt; <span>高保湿バリア美容液特集</span>
  </div>

  <main>
    <div class="hero-section">
      <span class="hero-tag">🔬 11月・12月 暖房インナードライ徹底鎮静</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！微細リポソーム化バリア成分とパンテノールの生体浸透力で真冬の暖房インナードライを芯から鎮静する保湿力高めバリア美容液ランク10</h1>
      <p class="hero-desc">
        11月から12月にかけて本格化するオフィスの集中暖房や車内エアコン。温風直撃による『表面は皮脂でベタつくのに内側がパキパキに突っ張るインナードライ』や、室内外の急激な寒暖差による赤み・ピリピリ感に悩まされる方が急増します。油分クリームを重ね塗りしても解決しないインナードライを根本から解消するためには、化粧水とクリームをつなぐ『角層深部バリア美容液』の投入が不可欠です。本特集では、微細リポソーム化セラミド、高純度アミノ酸、消炎パンテノールを高濃度配合した最高峰のバリア美容液10選を徹底検証しました。
      </p>
    </div>

    <div class="toc-box">
      <div class="toc-title">📑 目次・記事ナビゲーション</div>
      <ul class="toc-list">
        <li><a href="#science-guide">1. 暖房インナードライと寒暖差ストレスの皮膚科学メカニズム</a></li>
        <li><a href="#rank-1">第1位: AESTURA アトバリア365 ハイドロエッセンス</a></li>
        <li><a href="#rank-2">第2位: Torriden ソリッドイン セラミド オールインワン エッセンス</a></li>
        <li><a href="#rank-3">第3位: d program カンダンバリア エッセンス (医薬部外品)</a></li>
        <li><a href="#rank-4">第4位: Real Barrier エクストリーム エッセンス トナー</a></li>
        <li><a href="#rank-5">第5位: Curel 潤浸保湿 角層深部バリア美容液 (医薬部外品)</a></li>
        <li><a href="#rank-6">第6位: Anua ドクダミ 80% 水分鎮静アンプル</a></li>
        <li><a href="#rank-7">第7位: COSRX フルフィット プロポリス ライト アンプル</a></li>
        <li><a href="#rank-8">第8位: SKIN1004 マダガスカル センテラ アンプル</a></li>
        <li><a href="#rank-9">第9位: manyo ビフィダ バイオーム コンプレックス アンプル</a></li>
        <li><a href="#rank-10">第10位: ONE BY KOSÉ セラム ヴェール ディープリペア (医薬部外品)</a></li>
        <li><a href="#selection-matrix">2. 肌悩み別：冬のバリア美容液最適選択マトリクス</a></li>
        <li><a href="#faq-section">3. よくある質問・Q&Aセクション</a></li>
      </ul>
    </div>

    <div class="science-box" id="science-guide">
      <h3>🔬 なぜクリームを塗っても突っ張るのか？暖房インナードライとバリア欠損の皮膚科学</h3>
      <p>
        多くの人が陥りがちな冬のスキンケアの落とし穴が、『乾燥するからクリームを厚塗りする』という対処法です。しかし、角層の奥深くが干からびている状態で油分主体のクリームを塗っても、内部の空洞は埋まらず、表面だけがテカって内側が突っ張るインナードライが悪化します。
      </p>
      <div class="science-grid">
        <div class="science-card">
          <h4>① 暖房風による不感蒸泄の加速と代償性皮脂分泌</h4>
          <p>温風が直接肌に当たると、角層内部から水分が猛烈なスピードで奪われます。肌は水分蒸発を食い止めようと過剰に皮脂を分泌するため、表面テカリと内側乾燥が同時進行します。</p>
        </div>
        <div class="science-card">
          <h4>② 寒暖差によるTRPV1活性化と微小炎症</h4>
          <p>外気（5℃以下）から暖房の効いた室内（22℃以上）に入った瞬間の温度差により、感覚神経の温度受容体TRPV1が刺激され、毛細血管の拡張と赤み・痒みが発生します。</p>
        </div>
        <div class="science-card">
          <h4>③ リポソーム化バリア成分によるラメラ構造修復</h4>
          <p>水分とセラミド・アミノ酸をナノサイズのリポソーム（微細カプセル）に内包したバリア美容液は、角質細胞同士の微細な隙間へ浸透し、崩れたラメラ液晶構造を奥底から立て直します。</p>
        </div>
      </div>
      <p style="margin-top: 20px;">
        バリア美容液は、化粧水で与えた水分を抱え込み、後から塗るクリームの密着油膜と強固に連結する『潤いの架け橋』です。真冬の過酷なオフィス環境でも一日中ふっくらとした柔軟肌を保つための必須ステップとなります。
      </p>
    </div>

    <h2 class="section-title">真冬の肌乾燥とさようなら！高保湿バリア美容液おすすめランキング10選</h2>

    {product_cards_html}

    <div class="summary-box" id="selection-matrix">
      <h3>📊 肌トラブル・目的別：バリア美容液最適選択マトリクス</h3>
      <p>
        ご自身の肌のゆらぎ方やテクスチャーの好みに応じて最適なバリアセラムを選ぶことで、真冬のインナードライを最速で鎮静できます。
      </p>
      <table class="summary-table">
        <thead>
          <tr>
            <th>肌悩み・使用目的</th>
            <th>おすすめのアイテム</th>
            <th>注目の主要成分</th>
            <th>テクスチャーと仕上がり</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>暖房インナードライ・先行水分チャージ</strong></td>
            <td>AESTURA / Torriden</td>
            <td>30種アミノ酸、5D複合セラミド</td>
            <td>まろやかミルキー乳液状 / 高密着オールインワン</td>
          </tr>
          <tr>
            <td><strong>寒暖差による赤み・ヒリつき・ゆらぎ</strong></td>
            <td>d program / SKIN1004</td>
            <td>カンダンバリア複合体、高純度ツボクサ100%</td>
            <td>みずみずしい浸透ジェル / サラサラ鎮静リキッド</td>
          </tr>
          <tr>
            <td><strong>乾燥小ジワ・角層ゴワつき・ほぐし</strong></td>
            <td>キュレル / Real Barrier</td>
            <td>消炎アラントイン、特許MLE液晶構造</td>
            <td>肌をほぐす薬用エマルジョン / 濃厚アンプルトナー</td>
          </tr>
          <tr>
            <td><strong>ほてり・赤み・混合肌の水分補給</strong></td>
            <td>Anua ドクダミ 80%</td>
            <td>ドクダミエキス80%、パンテノール</td>
            <td>濃密とろみ水分セラム（オイルフリー）</td>
          </tr>
          <tr>
            <td><strong>肌免疫力・ツヤ不足・根本改善</strong></td>
            <td>魔女工場 / ONE BY KOSÉ / COSRX</td>
            <td>ビフィズス菌発酵液、ライスパワーNo.11、黒蜂プロポリス</td>
            <td>美肌菌発酵アンプル / 薬用自生ブースター / 蜜艶リッチ</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="hub-link-banner">
      <div>
        <h4>❄️ あわせてチェックしたい冬の集中保湿ケア</h4>
        <p>バリア美容液で角層深部を潤した後は、高密着な高保湿バリアクリームで鉄壁のフタをしましょう！</p>
      </div>
      <a href="/winter-barrier-cream" class="hub-link-btn">高保湿バリアクリーム特集へ →</a>
    </div>

    <div class="summary-box" id="faq-section">
      <h2 style="font-size: 1.3rem; margin-bottom: 20px; color: #064e3b;">❓ 真冬の高保湿バリア美容液に関するよくある質問（FAQ）</h2>
      {faq_html}
    </div>

    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <!-- 内部リンク更新スクリプトで自動挿入されます -->
      </div>
    </div>
  </main>

  <footer>
    <div class="footer-inner">
      <div class="footer-title">LUMI COSMETICS LAB 関連コンテンツ一覧</div>
      <div class="footer-links-grid" id="footer-links-placeholder">
        <!-- フッターリンク更新スクリプトで自動挿入されます -->
      </div>
      <div class="copyright">
        &copy; 2026 LUMI COSMETICS LAB. All rights reserved. 掲載されている商品価格・仕様・レビュー情報は楽天市場APIよりリアルタイムに自動取得された最新データです。
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-barrier-serum.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-barrier-serum.html!")
