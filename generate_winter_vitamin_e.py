import json
import re

with open("fetched_3new_nov_dec_yuzu_sake_vitamine.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_vitamin_e"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 ぷるぷる形状記憶プリン！真冬の冷え枯れ肌を一晩で弾力肌へ蘇らせるビタミンEマスク",
        "catch": "高純度ビタミンE（トコフェロール）×ナイアシンアミド。寒さで萎縮した冬肌をぷるんとした濃密ゲルが包み込み、翌朝押し返すハリへ",
        "brand_name": "Dear, Klairs (クレアス)",
        "capacity": "90ml (フレッシュリージュースド ビタミンEマスク)",
        "type": "高純度ビタミンEスリーピングパック・高保湿クリーム",
        "features": "トコフェロール（高純度ビタミンE）、ナイアシンアミド、アデノシン、セラミドNP、ツボクサエキス",
        "value": "崩しても数秒で元に戻る形状記憶テクスチャーが肌表面に強力なリフト密着膜を形成。就寝中の水分蒸発を完全に遮断",
        "desc_p1": "11月から12月にかけて冷え込みが強まると、血行不良により顔色が青白く沈み、肌の弾力が失われてしぼんでしまう『冬枯れ現象』。世界中で熱狂的な支持を集めるクレアスの『ビタミンEマスク』は、抗酸化の女王と呼ばれる高純度トコフェロールと美白・シワ改善成分ナイアシンアミドを贅沢にブレンドした集中ナイトパックです。",
        "desc_p2": "スプーンですくっても数秒で表面が平らに戻る不思議な杏仁豆腐・プリン状の形状記憶ゲルは、肌に乗せた瞬間にとろけて濃密なオイルイン膜へと変化。皮膚の毛細血管の巡りをサポートしながら、夜間のエアコン暖房による激しい乾燥から素肌を完全にガードします。翌朝顔を洗った瞬間の、手のひらを跳ね返すようなモチモチの弾力感と、内側から発光するような明るい透明感には誰もが息をのむはずです。",
        "target": "真冬になると顔が疲れてしぼんで見える方、朝起きると肌がカサついて突っ張る方、ビタミンC美容液の効果を何倍にも引き上げたい方",
        "point": "夜のお手入れの最後に、付属のスパチュラでアーモンド1粒大を取り顔全体に伸ばします。手のひらで顔を包み込んで体温で温めながらなじませてください。特に乾燥しやすい目元や口元には重ね塗りが効果的です。"
    },
    {
        "rank": 2,
        "tag": "🛡️ 70年愛される真冬の国民的救世主！トコフェロール酢酸エステル配合の指定医薬部外品",
        "catch": "ビタミンE誘導体が末梢血管を広げて血行を促進。真冬の頑固なひび・あかぎれ・しもやけを速攻で治癒へと導く濃厚リペア",
        "brand_name": "ユースキン (yuskin)",
        "capacity": "120g ポンプ (ユースキン ポンプ)",
        "type": "指定医薬部外品・高濃度ビタミンE薬用保湿クリーム",
        "features": "トコフェロール酢酸エステル（ビタミンE誘導体）、グリチルレチン酸、dl-カンフル、グリセリン、ヒアルロン酸Na",
        "value": "黄色いクリームはビタミンB2の天然色。真冬の過酷な寒冷で痛んだ角層の血行を促し、水分保持力を物理的に再建する家庭の必需品",
        "desc_p1": "日本の冬を支え続けてきた不朽の名作・ユースキン。その最大の有効成分は、血流を劇的に改善する『トコフェロール酢酸エステル（ビタミンE誘導体）』です。11月〜12月の水仕事や寒風で指先やひび割れ、かかとの角質肥厚が起こるのは、末梢の血流が滞って細胞に酸素と栄養が届かなくなることが根本原因です。",
        "desc_p2": "ユースキンを塗り込むと、ビタミンEが血管を拡張して血行を促し、肌が内側からポカポカと温まるような感覚をもたらします。濃厚でこっくりとした黄色いクリームは、肌にすり込むことで白っぽさが消え、サラッとした強力な保護被膜へと変化。使い勝手抜群のワンタッチポンプ容器なら、洗面所やリビングに置いてお風呂上がりや手洗い後に家族全員で手軽にレスキューケアが可能です。",
        "target": "冬になると手足のあかぎれ・ひび割れ・粉吹きに悩む方、かかとが硬くガサガサになる方、確かな薬用効果を求める方",
        "point": "手洗いや入浴の直後、水分を拭き取ったらすぐに1プッシュを手にとり、皮膚の温度で温めながら黄色みが消えるまでしっかりとすり込みます。就寝前に綿の手袋や靴下を重ねると、翌朝驚くほど滑らかな皮膚が再生します。"
    },
    {
        "rank": 3,
        "tag": "🌿 製薬会社発！天然型ビタミンEが肌荒れ・粉吹きを防ぐロングセラー薬用クリーム",
        "catch": "エーザイの皮膚科学研究。植物油由来の天然型ビタミンE（d-α-トコフェロール）と消炎成分が、冬のカサつく手肌とボディを密着保護",
        "brand_name": "Eisai (エーザイ) ザーネ",
        "capacity": "100g (ザーネクリーム)",
        "type": "医薬部外品・天然型ビタミンE高保湿薬用クリーム",
        "features": "天然型ビタミンE（酢酸d-α-トコフェロール）、グリチルリチン酸二カリウム、レシチン、グリセリン",
        "value": "合成ビタミンEより生体利用率が高い天然型ビタミンEを採用。刺激が少なく、顔から首・手足まで家族みんなで使える高保湿設計",
        "desc_p1": "製薬大手・エーザイが『素肌の血流とバリア機能』を追求して世に送り出した『ザーネクリーム』。主成分には、植物油から精製された生体親和性の極めて高い『天然型ビタミンE』を贅沢に配合しています。冬の乾燥によって皮膚が薄くなり、粉を吹いたりかゆみを感じるデリケートな肌を、優しく健やかに整えます。",
        "desc_p2": "クリームはこっくりと濃厚でありながら、肌に伸ばすとスーッとなじんでベタつきを残しません。大豆由来のレシチンが角層のラメラ構造を支え、水分と油分をガッチリと挟み込みます。無駄な香料を抑えたマイルドな使い心地で、冬の冷たい風にさらされる頬や口元の乾燥小ジワ対策から、ひじやすねの粉吹き防止まで、全身のマルチレスキュークリームとして大活躍します。",
        "target": "肌がデリケートで刺激の強いクリームが使えない方、天然型ビタミンEの穏やかな効果を実感したい方、顔にも体にも使える万能薬用クリームを求める方",
        "point": "朝晩の洗顔や入浴後、適量を手に取り乾燥が気になる部分に優しく伸ばします。手のひらで温めてから包み込むように密着させると、角層深くまでビタミンEが染み渡ります。"
    },
    {
        "rank": 4,
        "tag": "🍋 活性型ビタミンC×ビタミンE誘導体の黄金タッグ！冬の乾燥くすみと毛穴を撃退する集中美容液",
        "catch": "Wビタミン高浸透処方。トコフェロール酢酸エステルが血行を促し、ピュアビタミンCが冬枯れ毛穴とくすみを明るく晴らす",
        "brand_name": "ROHTO (ロート製薬) メラノCC",
        "capacity": "20ml (薬用しみ集中対策 プレミアム美容液)",
        "type": "高濃度Wビタミン薬用集中美容液",
        "features": "アスコルビン酸（活性型ビタミンC）、トコフェロール酢酸エステル（ビタミンE誘導体）、アラントイン、アルピニアホワイト",
        "value": "ビタミンCとビタミンEは互いの抗酸化力を再生し合う『相乗効果の黄金コンビ』。冬の冷えくすみと乾燥毛穴に濃密な一滴が直撃",
        "desc_p1": "SNSの美容界隈で圧倒的な支持を集めるロート製薬のメラノCCプレミアム美容液。美白のピュアビタミンCに加え、血行促進と皮脂の過酸化を防ぐ『トコフェロール酢酸エステル（ビタミンE誘導体）』がベストバランスで同時配合されている点が、冬のスキンケアにおいて最大の強みです。",
        "desc_p2": "通常版よりもリッチで濃密なオイル状のテクスチャーは、1滴ずつピンポイントで出せる密閉チューブを採用。肌に乗せるとじんわりとした温感とともに角層深部へすばやく浸透し、ビタミンEが寒さで滞った巡りを呼び覚まします。冬の紫外線やエアコン乾燥によるくすみ、開きがちな乾燥毛穴をキュッと引き締め、みずみずしい透明肌へと導きます。",
        "target": "冬になると毛穴の目立ちやくすみが気になる方、美白と血色感アップを同時に叶えたい方、密着感の高い濃厚美容液が好きな方",
        "point": "朝晩の化粧水の後、手のひらに4〜5滴を出して気になる部分、または顔全体になじませます。ビタミンEがビタミンCの浸透と安定性を高めるため、手のひらで優しく押し込むように塗布してください。"
    },
    {
        "rank": 5,
        "tag": "💧 天然トコフェロール100%の超濃密純粋オイル！手持ちの化粧水やクリームに1滴混ぜて冬枯れ肌を蘇らせる",
        "catch": "大豆・菜種由来の植物性高純度ビタミンE原液。水飴のように濃厚なオイルが目元や口元の乾燥小ジワをピタッと密閉",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "50ml (100%ナチュラル ビタミンEオイル)",
        "type": "100%純粋天然トコフェロール美容原液オイル",
        "features": "天然トコフェロール100%（非遺伝子組み換え植物抽出）、d-α-トコフェロール高含有",
        "value": "防腐剤・香料・添加物完全フリー。驚異的な粘度と抗酸化力で、冬の砂漠肌に究極のエモリエント膜を形成するマルチブースター",
        "desc_p1": "一般的な化粧品に「微量」しか含まれないビタミンEを、なんと純度100%のまま贅沢にボトリングした『&SH 100%ナチュラル ビタミンEオイル』。手にとるとまるで水飴のように粘度が高く黄金色に輝くテクスチャーは、高濃度トコフェロールそのものの証です。",
        "desc_p2": "このオイルの真骨頂は、手持ちのアイテムを即座に「真冬仕様の超高保湿コスメ」へアップグレードできる点にあります。乳液やクリームに1滴垂らして混ぜるだけで、保湿力とバリア保護膜の強度が劇的に向上。冬の暖房風にさらされても肌の内側の水分が1ミリも逃げない鉄壁のシールドを張り、目元やほうれい線のちりめんジワをふっくらと押し返します。",
        "target": "どんな高保湿クリームを塗っても数時間で乾いてしまう方、目元や口元の乾燥小ジワを集中的にケアしたい方、手持ちコスメをパワーアップさせたい方",
        "point": "粘度が高いため単体で塗るよりも、普段お使いの乳液やクリーム、またはホホバオイルなどのキャリアオイルに1〜2滴混ぜて手のひらで練り合わせてから塗布するのが最も滑らかになじむテクニックです。"
    },
    {
        "rank": 6,
        "tag": "🧪 トリプルビタミン×高濃度トコフェロール！寒暖差で揺らぐ冬肌のキメを速攻チャージする高機能アンプル",
        "catch": "ビタミンE誘導体×ビタミンC誘導体×ビタミンA。室外の極寒と暖房の効いた室内の激しい寒暖差に負けない強靭な肌基礎体力を構築",
        "brand_name": "シナジア (SYNERGIA)",
        "capacity": "10ml (SCエッセンスEX)",
        "type": "高濃度マルチビタミン集中修復アンプル",
        "features": "トコフェロール、パルミチン酸レチノール（ビタミンA）、テトラヘキシルデカン酸アスコルビル（脂溶性ビタミンC）、ヒト型セラミド",
        "value": "脂溶性ビタミンのトリプル相乗処方により、角層細胞の膜を酸化から守り抜き、冬の乾燥によるゴワつきや弾力低下を速攻リセット",
        "desc_p1": "冬は暖かい室内と凍てつく屋外を行き来することで、毛細血管の急激な拡張と収縮が繰り返され、肌のバリア機能がパニックを起こす『寒暖差ゆらぎ』が多発します。シナジアの『SCエッセンスEX』は、この過酷な温度変化に立ち向かうために開発された集中ドクターズセラムです。",
        "desc_p2": "ビタミンE（トコフェロール）を主軸に、ビタミンA（レチノール）と脂溶性ビタミンCを黄金比で配合。肌の細胞膜と同じリン脂質に溶け込むように浸透し、寒冷によって失われたハリとキメを素早く再構築します。サラリとした浸透性の高いエッセンスでありながら、塗布後は肌が内側から満たされたような高密度な弾力と輝きを実感できます。",
        "target": "暖房の部屋と外気の温度差で肌が赤くなったりゴワつく方、ハリ不足や毛穴のたるみが気になる方、本格的な集中美容液を求める方",
        "point": "化粧水の直後、スポイトから手のひらに2〜3滴を取り、顔全体に優しくハンドプレスします。寒暖差ダメージを受けやすい両頬には重ねづけして手のひらで温めてください。"
    },
    {
        "rank": 7,
        "tag": "💎 重力に抗う張力リフト！エラスプロ×トコフェロールが真冬のしぼみ肌をピンと引き上げる最高峰クリーム",
        "catch": "ロート製薬の皮膚科学の粋を結集。ビタミンEが寒冷による停滞を解き放ち、独自の高密着リフトバームが上向きのハリを形状記憶",
        "brand_name": "Obagi (オバジ) / ロート製薬",
        "capacity": "50g (オバジX ダーマアドバンスドリフト)",
        "type": "高機能ビタミンE高保湿張力リフトクリーム",
        "features": "トコフェロール（ビタミンE）、エラスプロ、エラスグロウ、コラーゲンコンプレックス",
        "value": "寒さでこわばり、下垂しやすい冬の肌をグッと引き上げて固定。濃厚な潤いと弾力を同時に注入するエイジングケアの最高峰",
        "desc_p1": "美容誌のベストコスメでリフト部門第1位を独占しているオバジの最高峰クリーム『ダーマアドバンスドリフト』。冬の寒さによって肌の血流が低下し、コラーゲンやエラスチンの生成が滞ると、肌全体が重力に負けてたるみやすくなります。この『冬のたるみ乾燥』にトコフェロールと先端ペプチドの力で立ち向かいます。",
        "desc_p2": "コクのあるこっくりとしたクリームは、肌に伸ばすとまるで肌を引っ張り上げるような強い密着感とテンション（張力）を感じさせます。トコフェロールが角層深くまで浸透して血行と代謝をサポートし、肌表面にはピーンと張るリフト膜を形成。夜塗って眠れば、翌朝のフェイスラインがすっきりと引き締まり、乾燥によるほうれい線や毛穴落ちをものともしない若々しいハリ肌に出会えます。",
        "target": "真冬の乾燥とともに頬のたるみやほうれい線が目立ってきた方、本格的なハリ・リフトアップを体感したい方、最高品質のクリームを求める方",
        "point": "夜のお手入れの最後に、パール粒大を手にとり、あご先からこめかみに向かってフェイスラインを引き上げるようにハンドプレスしながら伸ばします。手のひら全体で頬を包み込み、3秒間キープするとリフト効果が定着します。"
    },
    {
        "rank": 8,
        "tag": "🌸 アルガン幹細胞×ビタミンE誘導体×5種のヒト型セラミド！濃密なとろみで年齢肌を満たす高保水化粧水",
        "catch": "エトヴォスの最高峰エイジングケア。ビタミンE誘導体が冬の乾燥小ジワをふっくら押し上げ、セラミドが水分バリアを死守",
        "brand_name": "ETVOS (エトヴォス)",
        "capacity": "120ml (バイタライジングローション)",
        "type": "幹細胞×ビタミンE高保湿エイジングケア化粧水",
        "features": "トコフェリルリン酸Na（水溶性ビタミンE誘導体）、アルガニアスピノサ芽細胞エキス、ヒト型セラミド（1, 2, 3, 5, 6II）、ヒアルロン酸",
        "value": "敏感肌でも使える低刺激処方でありながら、美容液レベルの美容成分を凝縮。真冬の乾燥で硬くなった年齢肌をもっちり柔軟化",
        "desc_p1": "敏感肌のエイジングケアブランドとして名高いエトヴォスの『バイタライジングローション』。水溶性で角層への浸透スピードが極めて高いビタミンE誘導体『トコフェリルリン酸Na』を配合し、さらに過酷なモロッコの砂漠を生き抜くアルガンツリーの幹細胞エキスと5種のヒト型セラミドを贅沢に融合させた濃密化粧水です。",
        "desc_p2": "手に取るととろりとリッチなテクスチャーですが、肌に乗せるとすーっと角層へ吸い込まれ、ベタつかないシルキーな仕上がりを実現。ビタミンE誘導体が乾燥小ジワの気になる目元や口元をふっくらと押し上げ、セラミドが水分をがっちりホールドします。天然のローズ調のアロマが心地よく、冬のスキンケア時間を至福のひとときへと変えてくれます。",
        "target": "冬の乾燥小ジワが目立ってきた方、敏感肌でも攻めのエイジングケアをしたい方、とろみローションでしっとり満たされたい方",
        "point": "500円玉大を手にとり、手のひらで顔全体を包み込むように優しくなじませます。乾燥が気になる目尻や口元には、さらに少量を指先でトントンと重ねづけしてください。"
    },
    {
        "rank": 9,
        "tag": "🛡️ 高純度白色ワセリンの最高峰！ビタミンEや美容液の後に重ねて冬の冷風を100%遮断する保護シールド",
        "catch": "不純物を極限まで除去した高品質ワセリン。ベタつきを抑えたシルキー処方で、真冬の暖房乾燥から素肌の水分蒸発を物理的にブロック",
        "brand_name": "日興リカ (サンホワイト)",
        "capacity": "80g (サンホワイト シルキー Y-1)",
        "type": "高純度低刺激保護ワセリン",
        "features": "高純度白色ワセリン100%（酸処理を行わない高品質精製）、無香料・無着色・保存料フリー",
        "value": "ビタミンEオイルや美容液を塗った直後に重ねることで、有効成分の酸化と水分の蒸発を完全にストップ。アトピー肌や赤ちゃんの肌も安心",
        "desc_p1": "皮膚科医からも絶対的な信頼を置かれている日興リカの『サンホワイト シルキー Y-1』。一般的な黄色ワセリンや白色ワセリンよりもさらに高度に精製され、不純物を極限まで取り除いた最高純度の保護フィルムです。従来のワセリン特有のベタつきや伸びにくさを大幅に改良し、サラッと薄く伸びるシルキーな使い心地を実現しています。",
        "desc_p2": "ワセリンそのものには水分を与える力はありませんが、「すでに肌にある水分や、直前に塗ったビタミンE・美容液成分の蒸発を物理的に完全に防ぐ」という点において、ワセリンに勝る成分は地球上に存在しません。11月〜12月の木枯らしやエアコン暖房の直撃を受ける環境でも、肌表面に薄いシールドを張ることで、一日中みずみずしい潤いを逃さずキープできます。",
        "target": "どんな高保湿クリームでも乾いてしまう超乾燥肌の方、真冬に肌が赤くヒリつく敏感肌の方、ビタミンEケアの完璧なフタをしたい方",
        "point": "米粒大を手のひらに取り、両手をこすり合わせて手のひら全体に極薄く広げます。それを顔全体に『スタンプを押すように』優しく押し当てて密着させてください。擦らず薄く膜を張るのがベタつかせない秘訣です。"
    },
    {
        "rank": 10,
        "tag": "❄️ ヨーロッパの極寒から生まれた伝統処方！ミツロウ×アベンヌ温泉水×トコフェロールの濃厚ラップ",
        "catch": "天然ミツロウとアベンヌ温泉水の保護膜。ビタミンEが真冬の冷風で赤く荒れた頬やひび割れ肌を穏やかに修復",
        "brand_name": "Avene (アベンヌ)",
        "capacity": "40g (コールドクリーム N)",
        "type": "部分用・高密着コールドリペアクリーム",
        "features": "天然ミツロウ、アベンヌ温泉水、ミネラルオイル、トコフェロール（ビタミンE）",
        "value": "古代ローマの医師ガレノスが考案した伝統の『コールドクリーム処方』を現代の皮膚科学で再現。真冬の過酷な寒冷から素肌をガード",
        "desc_p1": "ヨーロッパの厳しい真冬の寒冷地で古くから愛されてきた『コールドクリーム』。アベンヌの『コールドクリーム N』は、肌に塗ると水分が蒸発する際にひんやりとした心地よさを与え、肌表面に天然ミツロウと良質な油分がラップのように密着して冷気を完全に遮断する部分用高保湿クリームです。",
        "desc_p2": "アベンヌ温泉水の持つ肌鎮静効果と、トコフェロールの抗酸化・血行促進作用が融合。冬の寒風にさらされて赤くなってしまった頬や、粉を吹いた小鼻の周り、乾燥でひび割れそうな指先などに塗り込むと、濃密な保護膜が肌を外部刺激から完璧に隔離し、急速に健やかな状態へとリペアします。携帯しやすいチューブタイプで、真冬の外出時のレスキューバームとしても欠かせません。",
        "target": "冬の寒風で頬が赤くヒリつく方、小鼻や口元の皮剥けを即座に落ち着かせたい方、冬のアウトドアやウィンタースポーツを楽しむ方",
        "point": "少量を指先に取り、赤みや乾燥が気になる部位に優しくトントンと置くように塗り広げます。おやすみ前の集中ナイトパックとして、乾燥部位に少し厚めに乗せておくのもおすすめです。"
    }
]

# JSON-LD 生成
jsonld_items = []
for i, p in enumerate(items):
    d = product_details[i]
    jsonld_items.append({
        "@type": "ListItem",
        "position": i + 1,
        "name": f"第{i+1}位：{d['brand_name']} {p['display_name']}",
        "description": d['catch'],
        "image": p['image'],
        "url": f"https://lumi-cosme.vercel.app/winter-vitamin-e.html#item-{i+1}",
        "offers": {
            "@type": "Offer",
            "price": str(p['price']),
            "priceCurrency": "JPY",
            "availability": "https://schema.org/InStock"
        }
    })

faq_list = [
    {
        "question": "ビタミンE（トコフェロール）は肌にどのような効果がありますか？冬に必須とされる理由は？",
        "answer": "ビタミンEは脂溶性の強力な抗酸化ビタミンであり、生体膜（細胞膜）を活性酸素や過酸化脂質の害から守る重要な働きをします。さらに大きな特徴として『末梢血管を拡張して血流を促進する作用』があります。11月〜12月の真冬は、寒気によって毛細血管が縮こまり、肌が酸素不足・栄養不足に陥ってゴワつきやくすみ、ひび割れが頻発します。ビタミンEを補給することで巡りを活性化させ、同時に強靭な油分膜で水分の蒸発を防げるため、真冬に最も頼りになる成分なのです。"
    },
    {
        "question": "ビタミンCとビタミンEは一緒に使うと効果が高まるというのは本当ですか？",
        "answer": "はい、皮膚科学的に完全に証明された相乗効果（シナジー）です。ビタミンCは水溶性、ビタミンEは脂溶性のため、肌の水分層と油分層の両方を隙間なく抗酸化することができます。さらに、ビタミンEが活性酸素を無力化して酸化された際、ビタミンCが存在するとビタミンEを元の還元型（活性型）に再生してくれるリサイクル機構が働きます。そのため、メラノCCやクレアスのようにビタミンCとEを組み合わせて使うことで、単体使用の何倍もの透明感とバリア保護効果が得られます。"
    },
    {
        "question": "ビタミンEオイルはオイリー肌やニキビ肌でも使えますか？",
        "answer": "高濃度のビタミンEオイル（トコフェロール原液など）は非常にリッチでエモリエント性が高いため、皮脂分泌の多いTゾーンや現在炎症を起こしている白ニキビ・赤ニキビの部位に直接厚塗りすることは避けてください。ただし、皮脂の酸化を防ぐ抗酸化作用自体はニキビ悪化防止に役立つため、オイリー肌や混合肌の方は化粧水や軽めのジェル乳液に1滴だけ混ぜて顔全体に薄くなじませるか、乾燥しやすいUゾーンや目元中心に使用するのが賢い方法です。"
    },
    {
        "question": "朝のメイク前にビタミンEコスメを使っても油焼けやメイク崩れしませんか？",
        "answer": "ビタミンE（トコフェロール）自体は抗酸化成分であり、油焼け（油分の酸化による肌トラブル）を起こす心配はありません。むしろ紫外線や乾燥による日中の酸化ストレスから肌を守ってくれます。メイク崩れを防ぐためには、油分の多い原液オイルは夜のケアを中心に使い、朝はエトヴォスのバイタライジングローションやメラノCCのような浸透性の高い処方を選ぶか、クリーム塗布後に軽くティッシュオフしてから下地を重ねるのがおすすめです。"
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
        "@id": "https://lumi-cosme.vercel.app/winter-vitamin-e.html"
    },
    "headline": "保湿力の強さで肌乾燥とさようなら！寒さで冷えた冬枯れ肌の巡りを高めてふっくら押し返すハリ艶を宿す高純度ビタミンE高保湿コスメランク10",
    "description": "11月・12月の寒冷乾燥と冷えぐすみ・ひび割れを救う高純度ビタミンEコスメを徹底厳選！クレアス、ユースキン、ザーネ、メラノCCからオバジ、サンホワイトまで楽天で今すぐ買えるおすすめ人気ランキング10選と血流改善スキンケア術を詳しく解説。",
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
    "name": "真冬の高純度ビタミンE高保湿コスメおすすめ人気ランキング10選",
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
  <title>保湿力の強さで肌乾燥とさようなら！寒さで冷えた冬枯れ肌の巡りを高めてふっくら押し返すハリ艶を宿す高純度ビタミンE高保湿コスメランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の寒冷乾燥と冷えぐすみ・ひび割れを救う高純度ビタミンEコスメを徹底厳選！クレアス、ユースキン、ザーネ、メラノCCからオバジ、サンホワイトまで楽天で今すぐ買えるおすすめ人気ランキング10選と血流改善スキンケア術を詳しく解説。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-vitamin-e.html">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！寒さで冷えた冬枯れ肌の巡りを高めてふっくら押し返すハリ艶を宿す高純度ビタミンE高保湿コスメランク10">
  <meta property="og:description" content="11月・12月の寒冷乾燥と冷えぐすみ・ひび割れを救う高純度ビタミンEコスメを徹底厳選！クレアス、ユースキン、ザーネ、メラノCCからオバジ、サンホワイトまで楽天で今すぐ買えるおすすめ人気ランキング10選。">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-vitamin-e.html">
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
      --primary-color: #047857;
      --primary-light: #ecfdf5;
      --primary-dark: #065f46;
      --accent-color: #059669;
      --text-main: #1f2937;
      --text-muted: #4b5563;
      --bg-light: #f0fdf4;
      --border-color: #a7f3d0;
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
      line-height: 1.8;
      border-left: 4px solid var(--accent-color);
      padding-left: 1.25rem;
      margin-top: 1rem;
    }}
    
    .toc-box {{
      background: var(--bg-light);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 1.5rem;
      margin-bottom: 3rem;
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 700;
      margin-bottom: 1rem;
      color: var(--primary-dark);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-list {{
      list-style: none;
      padding-left: 0.5rem;
    }}
    .toc-list li {{
      margin-bottom: 0.5rem;
      font-size: 0.95rem;
    }}
    .toc-list a {{
      color: var(--text-main);
      text-decoration: none;
      transition: color 0.2s;
    }}
    .toc-list a:hover {{
      color: var(--primary-color);
      text-decoration: underline;
    }}
    
    .content-section {{
      background: white;
      padding: 2.5rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
    }}
    .section-title {{
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--primary-dark);
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
      background: linear-gradient(135deg, #047857, #065f46);
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
      .article-header, .content-section, .product-card {{ padding: 1.5rem; }}
      .article-title {{ font-size: 1.45rem; }}
    }}
    
    .product-visual {{
      text-align: center;
    }}
    .product-img {{
      width: 100%;
      max-width: 260px;
      height: auto;
      border-radius: 10px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.08);
      margin-bottom: 1rem;
    }}
    .price-box {{
      background: #f9fafb;
      padding: 0.6rem;
      border-radius: 8px;
      margin-bottom: 1rem;
      border: 1px solid #e5e7eb;
    }}
    .price-label {{ font-size: 0.75rem; color: #6b7280; display: block; }}
    .price-value {{ font-size: 1.45rem; font-weight: 800; color: #b91c1c; }}
    .price-tax {{ font-size: 0.75rem; color: #6b7280; }}
    
    .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #bf0000, #990000);
      color: white;
      text-align: center;
      padding: 0.85rem 1rem;
      border-radius: 8px;
      text-decoration: none;
      font-weight: 800;
      font-size: 0.95rem;
      box-shadow: 0 4px 6px rgba(191, 0, 0, 0.2);
      transition: all 0.2s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #a80000, #800000);
      transform: translateY(-2px);
      box-shadow: 0 6px 8px rgba(191, 0, 0, 0.3);
    }}
    
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.25rem;
      font-size: 0.88rem;
    }}
    .spec-row {{
      display: flex;
      border-bottom: 1px solid #e5e7eb;
      padding: 0.5rem 0;
    }}
    .spec-th {{
      width: 110px;
      flex-shrink: 0;
      font-weight: 700;
      color: #4b5563;
    }}
    .spec-td {{
      flex-grow: 1;
      color: #1f2937;
    }}
    
    .review-box {{
      background: #f8fafc;
      border-left: 4px solid var(--primary-color);
      padding: 1.25rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 1.25rem;
    }}
    .review-box h4 {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
    }}
    .review-box p {{
      font-size: 0.92rem;
      line-height: 1.75;
      color: #334155;
      margin-bottom: 0.5rem;
    }}
    .review-box p:last-child {{ margin-bottom: 0; }}
    
    .target-box, .usage-box {{
      background: #f0fdf4;
      border: 1px solid #ecfdf5;
      padding: 0.85rem 1rem;
      border-radius: 8px;
      margin-bottom: 0.75rem;
      font-size: 0.9rem;
    }}
    .target-box strong, .usage-box strong {{
      color: var(--primary-dark);
      display: block;
      margin-bottom: 0.25rem;
    }}
    
    .faq-item {{
      border-bottom: 1px solid #e5e7eb;
      padding: 1.25rem 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
    }}
    .faq-a {{
      font-size: 0.95rem;
      line-height: 1.8;
      color: #374151;
    }}
    
    .footer-internal-links {{
      background: white;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2.5rem;
      margin-top: 3rem;
    }}
    .footer-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 0.75rem;
      margin-top: 1.25rem;
    }}
    .footer-links-grid a {{
      font-size: 0.88rem;
      color: #4b5563;
      text-decoration: none;
      padding: 0.4rem 0.6rem;
      background: #f9fafb;
      border-radius: 6px;
      border: 1px solid #e5e7eb;
      transition: all 0.2s;
    }}
    .footer-links-grid a:hover {{
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
      <a href="/#skincare">スキンケア・ボディケア特集</a>
      <span>&gt;</span>
      <span aria-current="page">高純度ビタミンEコスメ特集</span>
    </nav>

    <article class="article-header">
      <div class="article-meta">
        <time datetime="2026-11-04">公開日：2026年11月4日</time>
        <span>執筆：冬コスメ徹底比較ラボ 編集部（抗酸化皮膚生理学リサーチチーム）</span>
      </div>
      <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！寒さで冷えた冬枯れ肌の巡りを高めてふっくら押し返すハリ艶を宿す高純度ビタミンE高保湿コスメランク10</h1>
      <p class="article-lead">
        11月から12月は、急激な気温低下により肌の毛細血管が収縮し、血流の滞りと激しい水分蒸発が同時に進行する季節。肌が青白くしぼみ、いつものスキンケアが浸透しない「冬枯れ停滞肌」を救う切り札が、若返りのビタミンと呼ばれる「ビタミンE（トコフェロール）」です。末梢血管を広げて巡りを高める温感作用と、脂溶性ならではの強靭なバリア密着膜。本記事では、楽天公式APIよりリアルタイムに検証・取得した人気アイテムから厳選したランキング10選と皮膚科学に基づいた活用術を詳しく解説します。
      </p>
    </article>

    <section class="toc-box">
      <h2 class="toc-title">📑 目次・記事ナビゲーション</h2>
      <ul class="toc-list">
        <li><a href="#why-vitamin-e">1. なぜ真冬の乾燥停滞肌にビタミンEが必要なのか？皮膚生理学的メカニズム</a></li>
        <li><a href="#selection-criteria">2. 失敗しない冬の高純度ビタミンEコスメの選び方・3つの基準</a></li>
        <li><a href="#comparison-table">3. 高純度ビタミンEコスメ10選 スペック・価格比較表</a></li>
        <li><a href="#ranking-section">4. 高純度ビタミンEコスメおすすめ人気ランキング10選 詳細レビュー</a></li>
        <li><a href="#faq-section">5. 美容皮膚視点で答えるビタミンEコスメのよくある疑問Q&amp;A</a></li>
        <li><a href="#conclusion">6. まとめ：寒冷乾燥を根本打破する巡り温感保湿ルーティン</a></li>
      </ul>
    </section>

    <!-- セクション1 -->
    <section class="content-section" id="why-vitamin-e">
      <h2 class="section-title">🌿 1. なぜ真冬の乾燥停滞肌にビタミンEが必要なのか？皮膚生理学的メカニズム</h2>
      <p class="section-p">
        11月から12月にかけて外気温が10℃を下回ると、人間の体は熱を外に逃がさないように皮膚表面の毛細血管をぎゅっと収縮させます。その結果、表皮細胞に酸素や栄養を運ぶ血流が急激に低下し、<strong>『皮膚の酸欠・代謝低下』</strong>が起こります。
      </p>
      <p class="section-p">
        血流が滞ると、肌のターンオーバーが遅れて古い角質が硬くなり、さらに角層内の天然保湿因子（NMF）や細胞間脂質（セラミド）の生合成スピードも著しく落ち込みます。これに暖房による湿度の急低下が加わることで、肌の内側がつっぱり、顔色がどんより暗く沈み、触れるとゴワゴワとした冷たい感触になる『冬枯れしぼみ肌』が完成してしまうのです。
      </p>
      <p class="section-p">
        この寒冷による悪循環を根本から断ち切る栄養素こそが、<strong>『ビタミンE（トコフェロール）』</strong>です。
      </p>
      <p class="section-p">
        ビタミンEには、収縮した末梢血管を広げて血流を促す『血行促進作用』があります。寒さで強張った肌を内側からじんわりと温めて巡りを蘇らせ、表皮細胞に必要な水分と栄養の供給を再開させます。
      </p>
      <p class="section-p">
        さらにビタミンEは『脂溶性』であるため、肌の細胞膜（リン脂質）や皮脂膜と完全に一体化し、強力な抗酸化作用を発揮して過酷な暖房風や乾燥による皮脂の酸化を防ぎます。水分を一切逃がさない強靭なエモリエントシールドを張ることで、真冬の砂漠環境でもふっくらと押し返すような極上のハリと温かみのある血色感を宿すことができるのです。
      </p>
    </section>

    <!-- セクション2 -->
    <section class="content-section" id="selection-criteria">
      <h2 class="section-title">🔍 2. 失敗しない冬の高純度ビタミンEコスメの選び方・3つの基準</h2>
      <p class="section-p">
        真冬の過酷な乾燥と冷えを打破するために、ビタミンEコスメを選ぶ際は以下の3つの基準を意識しましょう。
      </p>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0; margin-bottom: 1.5rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">基準①：天然トコフェロール（生体親和性）とトコフェロール酢酸エステル（安定型薬用）の使い分け</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          「高純度オイル」や美容液で濃密なエイジング保湿をしたい場合は、天然d-α-トコフェロール配合の原液やマスクが最適です。一方、ひび・あかぎれ・しもやけの治療や手足の粉吹きを治したい場合は、医薬部外品として高配合されたトコフェロール酢酸エステル（ユースキンやザーネなど）を選びましょう。
        </p>
      </div>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0; margin-bottom: 1.5rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">基準②：ビタミンCやナイアシンアミドとの相乗処方（Wビタミン）</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          ビタミンEは単体でも強力ですが、ビタミンCやナイアシンアミドと組み合わせることで、抗酸化ネットワークが完成し美肌効果が何倍にも増幅します。冬のくすみや毛穴が気になる方は、メラノCCやクレアスのようなシナジー処方がベストバイです。
        </p>
      </div>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">基準③：テクスチャーと密閉度（スリーピングマスク・リフトクリーム・ワセリン）</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          夜間のエアコン暖房による水分蒸発を完全に食い止めたいなら、形状記憶ゲルや高密着リフトクリーム、純度100%ワセリンとの重ねづけが効果的。寝ている間に肌が乾かない重厚な保護膜を形成できるアイテムを選びましょう。
        </p>
      </div>
    </section>

    <!-- セクション3 比較表 -->
    <section class="content-section" id="comparison-table">
      <h2 class="section-title">📊 3. 高純度ビタミンEコスメ10選 スペック・価格比較表</h2>
      <p class="section-p">
        楽天公式APIよりリアルタイムに取得した最新価格と製品スペックの一覧表です。ケアしたい部位や肌悩みに合わせて比較検討してください。
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
        🏆 高純度ビタミンE高保湿コスメおすすめ人気ランキング10選
      </h2>
      {cards_joined}
    </section>

    <!-- セクション5 Q&A -->
    <section class="content-section" id="faq-section">
      <h2 class="section-title">❓ 5. 美容皮膚視点で答えるビタミンEコスメのよくある疑問Q&amp;A</h2>
      {faq_joined}
    </section>

    <!-- セクション6 まとめ -->
    <section class="content-section" id="conclusion">
      <h2 class="section-title">🌿 6. まとめ：寒冷乾燥を根本打破する巡り温感保湿ルーティン</h2>
      <p class="section-p">
        11月から12月にかけて訪れる本格的な寒波。冷たい木枯らしと暖房の効いた室内の行き来は、私たちが自覚している以上に肌の血流を奪い、乾燥とゴワつきを加速させます。
      </p>
      <p class="section-p">
        「どんなに化粧水を重ねても乾いてしまう」「顔色が青白く疲れて見える」と感じたら、それは水分不足だけでなく、血流停滞と皮脂膜の弱体化が起きているサインです。
      </p>
      <p class="section-p">
        ビタミンE（トコフェロール）を取り入れたスキンケアは、肌本来の巡りを呼び覚まし、脂溶性の強固なバリアで角層の水分を一滴たりとも逃しません。夜はクレアスのビタミンEマスクで黄金の集中パックを行い、手足やデリケート部位にはユースキンやザーネで薬用リペアを施す——この確かな皮膚科学のアプローチで、真冬でも内側から発光するふっくら艶やかなモチ肌をキープしてください。
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

with open("winter-vitamin-e.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated winter-vitamin-e.html successfully. Size: {len(html_content):,} bytes")
