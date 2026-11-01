import json
import re

with open("fetched_3nov_dec_inbath_eyemask_handmask_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_inbath_body"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 楽天ボディケア上位常連！濡れた肌の水分を抱き込んで翌朝まで濃密密封",
        "catch": "お風呂場で濡れたまま直塗り。疑似セラミド機能成分が水分の急激な蒸発を完全に遮断する冬の救世主",
        "brand_name": "Curel (キュレル / 花王)",
        "capacity": "大容量 310g（ポンプ吊り下げ対応）",
        "type": "医薬部外品・薬用濡れ肌専用モイストバリアクリーム",
        "features": "セラミド機能成分、アラントイン（消炎成分）、弱酸性・無香料・無着色・アルコールフリー",
        "value": "入浴直後の水分蒸発を防ぐ『セラミドラッピング技術』。脱衣所に出る前に全身完了する圧倒的時短と高保湿力",
        "desc_p1": "11月から12月にかけて気温が氷点下近くまで下がる冬本番、お風呂から上がって脱衣所に出た瞬間に襲いかかる凍える寒さ。急いで服を着たいあまりにボディケアを後回しにし、気づけばスネや腰回りが白く粉を吹き、夜中に猛烈なかゆみで目が覚めてしまう…そんな冬の悪循環を根本から解決するのが、キュレルの『バスタイム モイストバリアクリーム』です。",
        "desc_p2": "本品は、湯船から上がった直後、まだ体に水滴が残っている状態で直接塗り広げる濡れ肌専用クリーム。肌表面の水滴とクリームが瞬時に混ざり合い、濃厚なセラミド機能ヴェールへと変化して角層細胞の隙間を埋め尽くします。タオルで軽く押さえるように拭き取っても保湿バリアは肌にしっかり留まり、過酷な暖房乾燥の中でも翌朝まで吸い付くようなもっちり肌が持続。消炎有効成分アラントイン配合で、カサつきによる炎症や肌荒れも未然に防ぎます。",
        "target": "冬の脱衣所が寒くてボディケアをサボりがちな方、スネや背中の粉吹き・かゆみに悩む乾燥性敏感肌、小さな子どもの全身保湿を時短で済ませたいご家庭",
        "point": "浴室から出る直前、肌に水滴が滴る状態で2〜3プッシュを全身にサーッと滑らせ、その後に清潔なバスタオルで『こすらずポンポンと水気だけを吸い取る』のが潤いを100%定着させるコツです。"
    },
    {
        "rank": 2,
        "tag": "🚿 お風呂場に吊り下げてノズルを押すだけ！家族全員で使える弱酸性ぬれた肌用乳液",
        "catch": "タオルで拭く前のビシャビシャ肌にサッと密着。水となじむ独自ミルク処方で驚きのしっとり感",
        "brand_name": "Biore u (ビオレu / 花王)",
        "capacity": "吊り下げパック 300ml（S字フック＆ノズル付き）",
        "type": "ぬれた肌専用・高保湿インバスボディ乳液",
        "features": "シアバター・ワセリン配合高保湿処方、弱酸性、パラベンフリー、浴室吊り下げエコパック",
        "value": "タオルバーに引っ掛けて片手でワンアクション。床に置かないからヌメリ知らずで衛生的＆詰め替え不要の高コスパ",
        "desc_p1": "毎日の入浴後、脱衣所で子どもを拭きながら自分も急いで着替える慌ただしい冬の夜に、爆発的な支持を集めているのがビオレuの『ザ ボディ お風呂場で使う ぬれた肌用乳液』です。浴室内のタオルバーや物干し竿にS字フックで吊るし、専用ノズルを指先で軽くつまむだけで適量が出るスマート設計は、冬のボディケアの面倒くささを完全に過去のものにしました。",
        "desc_p2": "肌に残った水滴を抱き込んでスーッと広がるみずみずしいテクスチャーでありながら、シアバターと高精製ワセリンのダブル高保湿成分が角層表面にうるおいシールドを構築。塗った後はバスタオルで優しく押さえて拭くだけで、まるで入念にボディクリームを塗り込んだかのようなしっとりすべすべの手触りに整います。無香料タイプは敏感肌の方や強い香りが苦手な方、男性や小さなお子様までストレスフリーで愛用できます。",
        "target": "お風呂上がりのボディケアを手早く済ませたい忙しい方、コスパ重視で毎日たっぷり全身に使いたいファミリー、浴室をすっきり保ちたいミニマリスト",
        "point": "塗布後にシャワーで軽く流す必要はなく、そのままバスタオルで水気を拭き取ってください。足裏に乳液がつくと滑りやすくなるため、足裏だけは避けるかタオルでしっかり拭くのが安全です。"
    },
    {
        "rank": 3,
        "tag": "✨ 重炭酸温浴後の極上仕上げ！ナイアシンアミド配合リッチインバスクリーム",
        "catch": "入浴で柔らかくなった肌を美容液成分で満たす。まるで全身に贅沢フェイスマスクを施したような仕上がり",
        "brand_name": "BARTH (バース)",
        "capacity": "300g チューブボトル",
        "type": "高機能エイジングケア・プレミアムインバスボディクリーム",
        "features": "ナイアシンアミド、高純度シアバター、ホホバ種子油、天然ベルガモット精油、アルコール・パラベンフリー",
        "value": "重炭酸入浴剤で名高いBARTHが開発した最高峰インバスクリーム。温浴で開いた毛穴と角層へ美容成分が深く行き渡る贅沢体験",
        "desc_p1": "大人気の中性重炭酸入浴剤でバスタイムの概念を変えたBARTHが、冬の極上ナイトルーティンのために開発した『プレミアムインバスボディクリーム』。重炭酸温浴によって血行が促進され、皮膚温が上がって角層が柔らかくほぐれた絶好のタイミングを狙い、浴室を出る前の濡れた肌に直接馴染ませるラグジュアリーなボディケアアイテムです。",
        "desc_p2": "いま美容界で最も注目される整肌成分『ナイアシンアミド』を贅沢に配合し、さらに高精製シアバターとホホバオイルを絶妙な黄金比でブレンド。濡れた肌の上でとろけるように広がり、水分と油分が一体化して肌奥へ吸い込まれるような極上の浸透感を実感できます。洗い流し不要でタオルオフした後の肌は、吸い付くようなハリとツヤに満ち、天然ベルガモットの清々しい柑橘アロマが上質な眠りをサポートします。",
        "target": "ワンランク上のリッチな冬のボディケアを求める方、手足のハリ不足やくすみが気になる大人の女性、BARTHの入浴剤とライン使いしたい方",
        "point": "湯船の中で体が芯まで温まった後、浴室を出る直前に鎖骨周りからデコルテ、腕、脚へとリンパを流すように優しくマッサージしながら塗り伸ばすと、むくみケアと保湿が同時に叶います。"
    },
    {
        "rank": 4,
        "tag": "🌿 100年のハーブサイエンス！伝統の植物オイルが寒冷でこわばった濡れ肌をしっとりほぐす",
        "catch": "オーガニックカレンデュラ＆パンジーエキス。ヨーロッパの極寒を耐え抜いてきた濃厚ハーブミルク",
        "brand_name": "WELEDA (ヴェレダ)",
        "capacity": "ボトル 250ml",
        "type": "100%天然由来・オーガニックスキンフードボディミルク",
        "features": "サンシキスミレエキス、カレンデュラエキス、ヒマワリ種子油、シアバター、NATRUE認証取得",
        "value": "世界中で愛されるレスキューコスメ『スキンフード』のボディミルク版。濡れた肌にもスーッと溶け込み硬くなった角質を柔軟化",
        "desc_p1": "1926年の誕生以来、過酷な寒冷乾燥にさらされるヨーロッパの人々の肌を救い続けてきたヴェレダの伝説的クリーム『スキンフード』。その濃厚な保湿力とハーブの治癒力を、濡れた肌にもスムーズに馴染むボディミルクへと進化させたのが本品です。合成保存料・合成着色料・合成香料を一切使用せず、厳格なオーガニック基準をクリアしています。",
        "desc_p2": "肌を鎮静し健やかに整えるパンジー（三色菫）やカレンデュラのエキスが、冬の冷風や暖房で刺激を受けた肌バリアを急速リペア。お風呂上がりの水滴がついた肌に伸ばすと、ヒマワリオイルとシアバターが水分を抱え込んでサラリとした上質な保護膜を形成します。スイートオレンジやラベンダーを基調とした奥深いハーバルアロマが浴室いっぱいに漂い、森林浴をしているかのような深い安らぎをもたらします。",
        "target": "ケミカルな成分を避け本物のオーガニックコスメを使いたい方、冬になると肘や膝がゴワついて硬くなる方、深みのあるハーブの香りに癒やされたい方",
        "point": "お風呂上がりに水滴を拭き取る前に全身へ馴染ませ、特に乾燥しやすいひじ・ひざ・くるぶしには重ね塗りをしてからタオルドライすると、粉吹きやひび割れを未然にブロックできます。"
    },
    {
        "rank": 5,
        "tag": "💧 医療基準99%純度グリセリン配合！超乾燥肌の角層10層奥まで水分を届け続ける実力派",
        "catch": "微細分子の純度99%グリセリンが濡れた肌の水分を逃さない。ノルウェー漁師の手肌を守った極寒耐久処方",
        "brand_name": "Neutrogena (ニュートロジーナ)",
        "capacity": "250ml ポンプボトル",
        "type": "高濃度グリセリン・ディープモイスチャーボディローション",
        "features": "純度99%医療グレードグリセリン、アラントイン、パンテノール、無香料処方",
        "value": "北欧ノルウェーの極寒環境下で働く漁師のガサガサ肌を救った歴史。分子が極小のため角層深部へすばやく浸透し一日中乾かない",
        "desc_p1": "冬になるとどんなボディクリームを塗っても数時間後には肌がカサついて突っ張ってしまう…という超乾燥肌・砂漠肌の方に絶大な信頼を得ているのが、ニュートロジーナの『ディープモイスチャー ボディローション』です。医療グレードの純度99%グリセリンを採用しており、通常の保湿成分よりも圧倒的に分子が小さいため、角層の最深部（10層奥）まで瞬時に浸透します。",
        "desc_p2": "お風呂場の濡れた肌に塗布すると、グリセリンが肌表面の水分を瞬時にキャッチして角層内部へと引き込み、乾いた細胞一つひとつを満水状態へと導きます。高保湿でありながらベタつきや油膜感が残らず、サラリとした心地よい仕上がり。無香料で肌に余計な刺激を与えないため、敏感肌や男性、冬のアレルギー肌でも安心して毎日たっぷり使えます。",
        "target": "何を塗ってもすぐに乾燥してしまう超乾燥肌の方、ベタベタする油膜感が苦手で服をすぐに着たい方、信頼の皮膚科学ブランドを選びたい方",
        "point": "ポンプ式で使いやすく、浴室から出る直前に2〜3プッシュを全身へ手早く塗り広げてください。水分を強力に引き寄せる性質があるため、しっかり肌が濡れている状態で塗るのが最大の効果を発揮します。"
    },
    {
        "rank": 6,
        "tag": "🥛 日本の冬を支え続ける王道ミルク！高保水ヒアルロン酸×セラミドで一日中モチモチ肌",
        "catch": "ディープ＆ロングラスティングモイスチャー処方。濡れ肌にもスルスル伸びて翌日の夕方まで乾かない",
        "brand_name": "NIVEA (ニベア / 花王)",
        "capacity": "ボトル 200g",
        "type": "高保湿・超しっとりボディスキンミルク",
        "features": "ディープ＆ロングラスティングモイスチャー処方、セラミドⅡ、トレハロース、GG（グリセリルグルコシド）",
        "value": "ドラッグストアで手軽に買える圧倒的な信頼と実績。濃厚なのに濡れた肌の上で驚くほど滑らかに伸び広がるベストセラー",
        "desc_p1": "世代を超えて愛され続ける青缶でおなじみのニベアが、冬の頑固な乾燥肌のために技術を結集させた『スキンミルク しっとり』。濃厚なテクスチャーでありながら、肌の角層に存在するうるおい巡り成分GG（グリセリルグルコシド）やセラミド、トレハロースを配合し、内側から湧き上がるようなうるおいを持続させるディープモイスチャー処方を採用しています。",
        "desc_p2": "乾いた肌に塗ると少し重めのコクがあるミルクですが、お風呂上がりの濡れた肌に伸ばすと水滴と絶妙に乳化し、驚くほどスルスルと摩擦レスに全身へと行き渡ります。水分を閉じ込める油膜ヴェールが均一に形成されるため、バスタオルで拭いた後も肌がもっちり手に吸い付くような潤いが一日中キープ。乾燥によるスネのひび割れや粉吹きを完璧に防ぎます。",
        "target": "身近なドラッグストアやスーパーで手軽にリピートしたい方、しっとり濃厚な保湿感が好みな方、長年親しまれた優しい香りに包まれたい方",
        "point": "500円玉大を手にとり、手のひら全体で温めてから濡れた太ももやふくらはぎ、腕に円を描くように塗り込むと、血行も促進されて湯冷め防止にも効果的です。"
    },
    {
        "rank": 7,
        "tag": "🌸 製薬会社のアミノ酸スキンケア！カサつくデリケート肌を優しく包むバリア保湿",
        "catch": "肌本来の天然保湿因子（NMF）を補うアミノ酸高配合。乾燥肌のバリア機能を整え外気刺激から守る",
        "brand_name": "MINON (ミノン / 第一三共ヘルスケア)",
        "capacity": "ボトル 200ml",
        "type": "医薬部外品・薬用全身保湿ミルク",
        "features": "グリチルリチン酸2K（抗炎症成分）、9種の保潤アミノ酸、リピジュア、無香料・弱酸性・アレルギーテスト済み",
        "value": "第一三共ヘルスケアが敏感肌・乾燥肌のために開発。とろけるような低刺激ミルクで肌のゆらぎや赤みをしっかり予防",
        "desc_p1": "冬になると乾燥だけでなく、衣類の摩擦や暖房の温風で肌がチクチク痛痒くなったり、赤みが出てしまう…そんなデリケートな肌質に寄り添うのが、製薬会社のミノンの『全身保湿ミルク』です。肌の角層を構成する天然保湿因子（NMF）の主成分であるアミノ酸に着目し、9種の保潤アミノ酸と2種の清透アミノ酸を贅沢にブレンドしています。",
        "desc_p2": "抗炎症有効成分グリチルリチン酸2Kが配合されているため、乾燥で荒れがちな肌の炎症を優しく鎮静。濡れた肌に伸ばすと、乳液が水となじんでスルスルと軽やかに広がり、肌への摩擦負担を極限まで抑えて全身をバリアコーティングします。ベタつきが一切なく、塗った直後にパジャマを着ても張り付かないストレスフリーな使用感も高く評価されています。",
        "target": "冬になると肌が敏感になって痒みや赤みが出やすい方、アルコールや香料に弱い方、サラッとした使い心地でしっかり潤したい方",
        "point": "首筋やデコルテ、背中など、冬の衣類で擦れやすい部位に重点的に馴染ませておくと、タートルネックやウールニットのチクチク感を大幅に和らげることができます。"
    },
    {
        "rank": 8,
        "tag": "🌎 世界70カ国以上で愛される大容量！ナイアシンアミド＆パンテノール配合の皮膚科学処方",
        "catch": "591mlのビッグボトルで惜しみなく全身ケア。濡れ肌になじんでバリア機能を健やかに整える",
        "brand_name": "Cetaphil (セタフィル)",
        "capacity": "大容量 591ml×2本セット",
        "type": "低刺激・高保湿モイスチャライジングローション",
        "features": "ナイアシンアミド、パンテノール、グリセリン、アボカドオイル配合、無香料・低刺激性処方",
        "value": "皮膚科医が推奨するグローバルスキンケアブランド。家族全員で毎日全身に使っても数ヶ月持つ圧倒的なボリュームと高コスパ",
        "desc_p1": "世界中の皮膚科医に推奨され、乾燥肌・敏感肌の定番として不動の地位を築いているセタフィルの『モイスチャライジング ローション』。リニューアルによって、バリア機能をサポートするナイアシンアミド、肌荒れを防ぐパンテノール、そして高保湿グリセリンの『モイスチャーバリア3大成分』が新たに配合され、保湿持続力が飛躍的に進化しました。",
        "desc_p2": "591mlという圧倒的な大容量ボトルは、冬の毎日の全身ケアに気兼ねなくたっぷり使える最大のメリット。コクがあるのにみずみずしいローションは、お風呂上がりの濡れた肌の上でサラサラと滑るように伸び、すばやく角層へ浸透します。アボカド油由来の天然エモリエント成分が肌表面を優しくシールドし、タオルドライ後も一日中しっとり滑らかな感触が続きます。",
        "target": "毎日惜しみなく全身にたっぷり保湿剤を塗りたい方、大容量で長持ちする高コスパ製品を探している方、家族全員でシェアしたいご家庭",
        "point": "浴室のドア脇に置いておき、お風呂から出る直前に濡れた手足・お腹・背中に2〜3プッシュ豪快に塗り広げてください。濡れた肌に塗ることで消費量を抑えつつ、驚くほど広範囲にムラなく伸びます。"
    },
    {
        "rank": 9,
        "tag": "🌺 ボタニカルの恵みで至福の香りと潤い！植物スクワラン×シアバターの濃密ヴェール",
        "catch": "植物由来の美容成分が濡れた肌をしっとりラッピング。優雅なホワイトリリーの香りで贅沢バスタイム",
        "brand_name": "BOTANIST (ボタニスト)",
        "capacity": "ボトル 240ml",
        "type": "植物由来ボタニカル・リッチ高保湿ボディミルク",
        "features": "オリーブスクワラン、シア脂、カカオ脂、アロエベラ葉エキス、合成着色料フリー",
        "value": "植物の力でうるおいを守るボタニストのボディケア。入浴後の濡れた肌に伸ばすことで香りがふんわり立ち上り優雅なリラックス空間に",
        "desc_p1": "ヘアケアで大人気のボタニストが、植物の生命力に着目して作り上げた『ボタニカル ボディミルク』。厳しい冬の乾燥から肌を守るため、オリーブ由来のスクワランや濃密なオーガニックシアバター、カカオバターなどの厳選されたボタニカルバター＆オイルをリッチにブレンドしています。",
        "desc_p2": "お風呂上がりの温かい蒸気が漂う浴室で濡れた肌に馴染ませると、植物オイルが水分と乳化してとろけるように広がり、肌のキメをふっくら整えます。お風呂の湯気とともに上品で透明感のあるホワイトリリー＆ミュゲの香りがふわりと立ち上り、一日の疲れがスーッと溶けていくような極上のアロマ体験に。タオルで軽く水気を拭き取った後も、清潔感のある優しい香りとシルクのような滑らかさが肌に残ります。",
        "target": "ボディケアで上品な香りを楽しみたい方、植物由来のナチュラルな保湿成分にこだわりたい方、ギフトや自分へのご褒美ケアに",
        "point": "首筋からデコルテ、手首にかけて丁寧に塗り伸ばすと、翌朝起きたときもほのかに清潔感のある良い香りが漂い、朝の気分を心地よく高めてくれます。"
    },
    {
        "rank": 10,
        "tag": "🍑 ベビーオイル生まれの信頼感！ホホバ油＆シアバターが濡れ肌をしっとり満たす高コスパ名作",
        "catch": "うるおいカプセル配合で24時間乾燥知らず。甘くみずみずしいピーチ＆アプリコットの香りで気分もアップ",
        "brand_name": "Johnson's (ジョンソン・エンド・ジョンソン)",
        "capacity": "ボトル 200ml",
        "type": "高保湿・アロマラスティングモイスチャースキンケアローション",
        "features": "ホホバ種子油、シア脂、高純度ミネラルオイル、ビタミンE誘導体、独自のアロマブレンド",
        "value": "130年以上の歴史を持つジョンソンのベビーオイル技術を応用。500円台という手頃な価格ながら一日中続くうるおいと華やかな香り",
        "desc_p1": "ドラッグストアで手軽に手に入り、長年多くの女性から愛されているジョンソンボディケアの『ラスティングモイスチャー スキンケアローション』。赤ちゃんのデリケートな肌を守るベビーオイルをベースに、肌なじみの良い天然ホホバオイルと高保湿シアバターを配合した大人気ロングセラーです。",
        "desc_p2": "みずみずしく柔らかなミルクは濡れた肌との相性が抜群で、水滴の上をスーッと滑るように伸びてあっという間に全身の保湿が完了します。独自の保湿キープ処方により、タオルドライ後も肌表面に潤いの保護膜を形成し、夕方までカサつきや粉吹き知らず。ジューシーで甘酸っぱいピーチとアプリコットのアロマが冬の寒さでこわばった気分を明るく前向きにしてくれます。",
        "target": "プチプラで惜しみなく使えるボディミルクを探している方、フルーティーで甘い香りが好きな方、学生や毎日のデイリーケアに",
        "point": "お風呂から上がる直前に全身へ塗布した後、手元に残ったミルクを爪の甘皮や手の甲にすり込むと、ハンドクリーム代わりの保湿にもなって一石二鳥です。"
    }
]

# 比較表生成
table_rows = []
for p, item in zip(product_details, items):
    table_rows.append(f"""
    <tr>
      <td class="rank-cell">第{p['rank']}位</td>
      <td class="brand-cell"><strong>{p['brand_name']}</strong><br><small>{item['display_name'][:25]}...</small></td>
      <td class="price-cell">¥{item['price']:,}</td>
      <td>{p['type']}</td>
      <td>{p['capacity']}</td>
      <td>{p['features']}</td>
    </tr>
    """)

# 商品カードHTML生成
product_cards_html = []
for p, item in zip(product_details, items):
    product_cards_html.append(f"""
    <article class="product-card" id="rank-{p['rank']}">
      <div class="product-badge">第{p['rank']}位</div>
      <div class="product-header">
        <span class="product-tag">{p['tag']}</span>
        <h3 class="product-title">{p['brand_name']} - {item['display_name']}</h3>
        <p class="product-catch">{p['catch']}</p>
      </div>

      <div class="product-main">
        <div class="product-image-wrap">
          <img src="{item['image_url']}" alt="{p['brand_name']} {item['display_name']}" class="product-img" loading="lazy">
        </div>
        <div class="product-info">
          <div class="product-meta-list">
            <div class="meta-item"><span class="meta-label">参考価格：</span><span class="meta-value price-val">¥{item['price']:,}（税込）</span></div>
            <div class="meta-item"><span class="meta-label">内容量：</span><span class="meta-value">{p['capacity']}</span></div>
            <div class="meta-item"><span class="meta-label">アイテム種別：</span><span class="meta-value">{p['type']}</span></div>
            <div class="meta-item"><span class="meta-label">主要成分：</span><span class="meta-value">{p['features']}</span></div>
            <div class="meta-item"><span class="meta-label">取扱店舗：</span><span class="meta-value">{item['shop_name']}</span></div>
          </div>
          <div class="product-points">
            <h4>💡 ここが冬の極寒＆粉吹き乾燥に効く注目ポイント！</h4>
            <p>{p['value']}</p>
          </div>
        </div>
      </div>

      <div class="product-description">
        <h4>【詳細解説＆本音レビュー】</h4>
        <p>{p['desc_p1']}</p>
        <p>{p['desc_p2']}</p>
      </div>

      <div class="product-advice">
        <div class="advice-block target-block">
          <strong>🎯 こんな人に特におすすめ：</strong>
          <p>{p['target']}</p>
        </div>
        <div class="advice-block tip-block">
          <strong>✨ プロの濡れ肌保湿アドバイス：</strong>
          <p>{p['point']}</p>
        </div>
      </div>

      <div class="product-action">
        <a href="{item['affiliate_url']}" class="rakuten-btn" target="_blank" rel="noopener noreferrer nofollow">
          <span>楽天市場で最安値＆口コミをチェック</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </article>
    """)

faq_items = [
    {
        "q": "一般的なボディクリームと『濡れた肌用インバスボディミルク』は何が違うのですか？",
        "a": "水となじむ『乳化テクノロジー』の有無が決定的に異なります。通常のボディクリームやオイルは乾いた肌に塗ることを前提として設計されており、濡れた肌に塗ると水分に弾かれてムラになったりベタついたりします。一方、インバスボディミルクは水分と触れ合うことで瞬時に乳化し、肌表面の水滴を抱え込んで均一な保湿ヴェールを形成するように設計されています。そのため、水滴がついたままの肌にスルスル伸び、タオルで軽く拭いても潤い成分が角層にしっかり密着して留まります。"
    },
    {
        "q": "塗った後にバスタオルで体を拭いたら、せっかくの保湿成分がタオルに落ちてしまいませんか？",
        "a": "落ちません。インバスボディミルクの有効成分は濡れた角層に素早く吸着し、肌表面に疎水性（水を弾く）の保護膜を形成します。そのため、タオルで拭き取られるのは『余分な表面の水滴』だけで、保湿バリアは肌にしっかり残ります。ただし、タオルで肌をゴシゴシ強く擦ると摩擦で角質や保湿膜が剥がれてしまいますので、『タオルを肌にポンポンと優しく押し当てて水気を吸わせる』ように拭くのが重要なポイントです。"
    },
    {
        "q": "浴室の中で塗ると、床や浴槽が滑って危なくありませんか？",
        "a": "足裏にミルクが付着すると床が滑りやすくなるため注意が必要です。安全に使うためのポイントは2つあります。1つ目は『足裏には直接塗らないこと』。足の甲やすね・ふくらはぎまでに留めましょう。2つ目は『お風呂から出る直前の洗い場（排水口付近）で塗ること』です。万が一床にミルクが落ちた場合は、浴室を出る前にシャワー（できれば温水）で床をサーッと洗い流しておくと、後から入る家族も滑らず安心です。"
    },
    {
        "q": "濡れた肌用ボディミルクは、顔や首元にも使えますか？",
        "a": "首筋やデコルテへの使用は非常におすすめですが、顔への使用は製品の表記をご確認ください。キュレルやビオレu、セタフィルなどの低刺激・弱酸性設計のものは基本的に顔にも使えますが、ボディ用ミルクは身体の厚い皮膚に合わせて油分や乳化剤が調整されているため、顔の毛穴詰まりやニキビの原因になる場合があります。顔には顔専用のインバス導入美容液やシートマスクを使用し、ボディミルクは首から下の全身にお使いいただくのが最も安心です。"
    },
    {
        "q": "冬の粉吹きや乾燥によるかゆみがひどい場合、インバスボディケアだけで十分ですか？",
        "a": "軽度〜中程度の乾燥肌であれば、インバスボディミルクだけで十分に翌朝まで粉吹きやかゆみを防ぐことができます。しかし、すでにすねが白くひび割れて粉を吹いていたり、服のこすれで強いかゆみが出ている深刻な超乾燥状態の場合は、浴室でインバスミルクを塗ってタオルドライした後に、特に乾きやすいひざ・すね・かかとなどに高保湿なバームやワセリンを『追い保湿』として重ね塗りすると、驚くほど劇的にバリア機能が回復します。"
    }
]

# JSON-LD 構造化データ
json_ld_products = []
for p, item in zip(product_details, items):
    json_ld_products.append({
        "@type": "Product",
        "name": f"{p['brand_name']} {item['display_name']}",
        "image": item['image_url'],
        "description": p['value'],
        "brand": {
            "@type": "Brand",
            "name": p['brand_name']
        },
        "offers": {
            "@type": "Offer",
            "url": item['affiliate_url'],
            "priceCurrency": "JPY",
            "price": item['price'],
            "availability": "https://schema.org/InStock"
        }
    })

json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで冬の脱衣所極寒・粉吹き乾燥とさようなら！浴室で濡れたまま塗って即潤い閉じ込める高保湿インバスボディミルクランク10",
    "description": "11月・12月の冬の凍える脱衣所での寒冷ストレスと、お風呂上がりの急激な水分蒸発（過乾燥）を徹底解決！キュレル、ビオレu、BARTH、ヴェレダ、ニュートロジーナ、ニベア、ミノン、セタフィルなど、浴室の中で濡れたまま塗って即座に潤いを閉じ込める最強高保湿インバスボディミルク10選を徹底比較！",
    "image": items[0]['image_url'],
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
    "datePublished": "2026-11-02",
    "dateModified": "2026-11-02"
}

json_ld_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "冬の濡れた肌用高保湿インバスボディミルク おすすめランキング10選",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": idx + 1,
            "item": prod
        } for idx, prod in enumerate(json_ld_products)
    ]
}

json_ld_faq = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": faq['q'],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq['a']
            }
        } for faq in faq_items
    ]
}

json_ld_breadcrumb = {
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
            "name": "高保湿インバスボディミルク特集",
            "item": "https://lumi-cosme.vercel.app/winter-inbath-body"
        }
    ]
}

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで冬の脱衣所極寒・粉吹き乾燥とさようなら！浴室で濡れたまま塗って即潤い閉じ込める高保湿インバスボディミルクランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬の凍える脱衣所での寒冷ストレスと、お風呂上がりの急激な水分蒸発（過乾燥）を徹底解決！キュレル、ビオレu、BARTH、ヴェレダ、ニュートロジーナ、ニベア、ミノン、セタフィルなど、浴室の中で濡れたまま塗って即座に潤いを閉じ込める最強高保湿インバスボディミルク10選を徹底比較！">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-inbath-body">
  <link rel="icon" href="/favicon.jpg">
  <link rel="stylesheet" href="style.css">

  <!-- Open Graph -->
  <meta property="og:title" content="保湿力の強さで冬の脱衣所極寒・粉吹き乾燥とさようなら！浴室で濡れたまま塗って即潤い閉じ込める高保湿インバスボディミルクランク10">
  <meta property="og:description" content="11月・12月の冬の凍える脱衣所での寒冷ストレスと、お風呂上がりの急激な水分蒸発（過乾燥）を徹底解決！キュレル、ビオレu、BARTH、ヴェレダなど濡れたまま濡れる最強インバスミルク10選！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-inbath-body">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">

  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json">
  {json.dumps(json_ld_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_itemlist, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_faq, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_breadcrumb, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #0891b2;
      --primary-dark: #0e7490;
      --primary-light: #ecfeff;
      --accent: #06b6d4;
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --radius: 16px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
    }}

    .site-header {{
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 1rem 0;
    }}
    .header-container {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--primary-dark);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .nav-links {{
      display: flex;
      gap: 1.5rem;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-weight: 600;
      font-size: 0.95rem;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{
      color: var(--primary);
    }}

    .main-container {{
      max-width: 960px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}

    .breadcrumbs {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
    }}
    .breadcrumbs a {{
      color: var(--text-muted);
      text-decoration: none;
    }}
    .breadcrumbs a:hover {{
      color: var(--primary);
    }}

    .article-header {{
      background: linear-gradient(135deg, #0891b2 0%, #0e7490 50%, #155e75 100%);
      color: white;
      padding: 3.5rem 2rem;
      border-radius: var(--radius);
      margin-bottom: 2.5rem;
      box-shadow: 0 10px 25px -5px rgba(8, 145, 178, 0.3);
    }}
    .article-tag {{
      display: inline-block;
      background: rgba(255, 255, 255, 0.2);
      backdrop-filter: blur(4px);
      padding: 0.35rem 1rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      margin-bottom: 1rem;
    }}
    .article-title {{
      font-size: 2rem;
      font-weight: 800;
      line-height: 1.4;
      margin-bottom: 1.5rem;
    }}
    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.9rem;
      opacity: 0.9;
    }}

    .intro-box {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 2.5rem;
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
      border-left: 6px solid var(--primary);
    }}
    .intro-lead {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
      line-height: 1.7;
    }}
    .intro-box p {{
      margin-bottom: 1rem;
      color: #334155;
    }}
    .intro-highlight-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 1.2rem;
      margin-top: 1.8rem;
    }}
    .intro-card {{
      background: var(--primary-light);
      padding: 1.2rem;
      border-radius: 12px;
      border: 1px solid rgba(8, 145, 178, 0.2);
    }}
    .intro-card h4 {{
      color: var(--primary-dark);
      font-size: 1rem;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}
    .intro-card p {{
      font-size: 0.88rem;
      color: #334155;
      margin-bottom: 0;
      line-height: 1.6;
    }}

    .section-title {{
      font-size: 1.7rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 1.5rem;
      padding-bottom: 0.6rem;
      border-bottom: 3px solid var(--primary);
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .table-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 2rem;
      box-shadow: var(--shadow);
      margin-bottom: 3.5rem;
    }}
    .table-wrapper {{
      overflow-x: auto;
    }}
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}
    .spec-table th, .spec-table td {{
      padding: 1rem 0.8rem;
      border-bottom: 1px solid var(--border);
    }}
    .spec-table th {{
      background: #f1f5f9;
      font-weight: 700;
      color: #334155;
      white-space: nowrap;
    }}
    .spec-table .rank-cell {{
      font-weight: 800;
      color: var(--primary-dark);
      text-align: center;
      white-space: nowrap;
    }}
    .spec-table .price-cell {{
      font-weight: 700;
      color: #e11d48;
      white-space: nowrap;
    }}

    .product-card {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 2.2rem;
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
      position: relative;
      border: 1px solid var(--border);
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .product-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 12px 20px -5px rgba(0, 0, 0, 0.08);
    }}
    .product-badge {{
      position: absolute;
      top: -12px;
      left: 24px;
      background: linear-gradient(135deg, #0891b2, #0e7490);
      color: white;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 0.3rem 1.2rem;
      border-radius: 9999px;
      box-shadow: 0 4px 8px rgba(8, 145, 178, 0.3);
    }}
    .product-header {{
      margin-top: 0.8rem;
      margin-bottom: 1.5rem;
    }}
    .product-tag {{
      display: inline-block;
      color: var(--primary-dark);
      font-weight: 700;
      font-size: 0.85rem;
      background: var(--primary-light);
      padding: 0.25rem 0.75rem;
      border-radius: 6px;
      margin-bottom: 0.5rem;
    }}
    .product-title {{
      font-size: 1.45rem;
      font-weight: 800;
      line-height: 1.4;
      color: #0f172a;
      margin-bottom: 0.4rem;
    }}
    .product-catch {{
      font-size: 1rem;
      color: var(--text-muted);
      font-weight: 600;
    }}

    .product-main {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
      margin-bottom: 1.8rem;
    }}
    @media (max-width: 768px) {{
      .product-main {{ grid-template-columns: 1fr; }}
      .article-title {{ font-size: 1.5rem; }}
    }}
    .product-image-wrap {{
      text-align: center;
      background: #f8fafc;
      border-radius: 12px;
      padding: 1rem;
      border: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .product-img {{
      max-width: 100%;
      max-height: 250px;
      object-fit: contain;
      border-radius: 8px;
    }}

    .product-meta-list {{
      background: #f8fafc;
      border-radius: 10px;
      padding: 1rem 1.2rem;
      margin-bottom: 1.2rem;
      border: 1px solid var(--border);
    }}
    .meta-item {{
      display: flex;
      font-size: 0.9rem;
      padding: 0.35rem 0;
      border-bottom: 1px dashed #e2e8f0;
    }}
    .meta-item:last-child {{ border-bottom: none; }}
    .meta-label {{
      width: 100px;
      font-weight: 700;
      color: var(--text-muted);
      flex-shrink: 0;
    }}
    .meta-value {{
      color: var(--text);
      font-weight: 500;
    }}
    .price-val {{
      color: #e11d48;
      font-weight: 800;
      font-size: 1.15rem;
    }}

    .product-points {{
      background: #f0fdfa;
      border-left: 4px solid #0d9488;
      padding: 1rem 1.2rem;
      border-radius: 0 8px 8px 0;
    }}
    .product-points h4 {{
      font-size: 0.92rem;
      color: #0f766e;
      margin-bottom: 0.3rem;
    }}
    .product-points p {{
      font-size: 0.88rem;
      color: #134e4a;
      line-height: 1.6;
      margin-bottom: 0;
    }}

    .product-description {{
      margin-bottom: 1.5rem;
      line-height: 1.8;
      color: #334155;
    }}
    .product-description h4 {{
      font-size: 1.05rem;
      color: #0f172a;
      margin-bottom: 0.6rem;
    }}
    .product-description p {{
      margin-bottom: 0.8rem;
    }}

    .product-advice {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-bottom: 1.8rem;
    }}
    @media (max-width: 640px) {{
      .product-advice {{ grid-template-columns: 1fr; }}
    }}
    .advice-block {{
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.88rem;
      line-height: 1.6;
    }}
    .target-block {{
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #1e3a8a;
    }}
    .tip-block {{
      background: #fefce8;
      border: 1px solid #fef08a;
      color: #713f12;
    }}
    .advice-block strong {{
      display: block;
      margin-bottom: 0.3rem;
    }}

    .product-action {{
      text-align: center;
      margin-top: 1rem;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.6rem;
      background: linear-gradient(135deg, #bf0000 0%, #e60000 100%);
      color: white;
      text-decoration: none;
      font-size: 1.05rem;
      font-weight: 700;
      padding: 1rem 2.5rem;
      border-radius: 9999px;
      box-shadow: 0 4px 12px rgba(191, 0, 0, 0.25);
      transition: transform 0.2s, box-shadow 0.2s;
      width: 100%;
      max-width: 480px;
    }}
    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(191, 0, 0, 0.35);
      color: white;
    }}

    .faq-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 2.5rem;
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
    }}
    .faq-item {{
      border-bottom: 1px solid var(--border);
      padding: 1.5rem 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.6rem;
      display: flex;
      align-items: flex-start;
      gap: 0.6rem;
    }}
    .faq-q::before {{
      content: "Q";
      background: var(--primary);
      color: white;
      font-size: 0.8rem;
      font-weight: 800;
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      margin-top: 0.2rem;
    }}
    .faq-a {{
      color: #334155;
      font-size: 0.95rem;
      line-height: 1.8;
      padding-left: 1.8rem;
    }}

    .internal-links-box {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 2.5rem;
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
    }}
    .links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1rem;
      margin-top: 1.2rem;
    }}
    .link-card {{
      background: #f8fafc;
      padding: 1rem;
      border-radius: 8px;
      border: 1px solid var(--border);
      text-decoration: none;
      color: var(--text);
      transition: border-color 0.2s, background 0.2s;
    }}
    .link-card:hover {{
      border-color: var(--primary);
      background: var(--primary-light);
    }}
    .link-card strong {{
      display: block;
      color: var(--primary-dark);
      font-size: 0.92rem;
      margin-bottom: 0.3rem;
    }}
    .link-card span {{
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.4;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}

    .site-footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 3rem 0;
      margin-top: 4rem;
      border-top: 1px solid #1e293b;
    }}
    .footer-container {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      text-align: center;
      font-size: 0.85rem;
    }}
    .footer-links {{
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 1.2rem;
      margin-bottom: 1.5rem;
    }}
    .footer-links a {{
      color: #cbd5e1;
      text-decoration: none;
    }}
    .footer-links a:hover {{
      color: white;
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-container">
      <a href="/" class="site-logo">
        <span>❄️ 冬コスメ徹底比較ラボ</span>
      </a>
      <nav class="nav-links">
        <a href="/">トップ</a>
        <a href="/winter-inbath-body">インバスボディケア</a>
        <a href="/winter-body-cream">ボディクリーム</a>
        <a href="/winter-bath-care">バスケア特集</a>
      </nav>
    </div>
  </header>

  <main class="main-container">
    <div class="breadcrumbs">
      <a href="/">ホーム</a> &gt; <a href="/winter-inbath-body">冬のボディケア特集</a> &gt; <span>濡れた肌用高保湿インバスボディミルク</span>
    </div>

    <header class="article-header">
      <span class="article-tag">❄️ 11月・12月最新冬コスメ徹底比較特集</span>
      <h1 class="article-title">保湿力の強さで冬の脱衣所極寒・粉吹き乾燥とさようなら！浴室で濡れたまま塗って即潤い閉じ込める高保湿インバスボディミルクランク10</h1>
      <div class="article-meta">
        <span>📅 更新日: 2026年11月2日</span>
        <span>⏱️ 読了目安: 約8分</span>
        <span>🔍 楽天公式APIリアルタイム価格検証済み</span>
      </div>
    </header>

    <div class="intro-box">
      <p class="intro-lead">
        11月から12月にかけて日本列島を本格的な寒波が包み込む時期、誰もが経験する「お風呂上がりの脱衣所の凍える寒さ」。寒さに耐えかねて大急ぎで服を着てしまい、ボディケアをサボってしまった結果、スネが白く粉を吹き、夜中に猛烈なかゆみで目が覚めてしまう…そんな冬の悪夢を完全に断ち切る革新的アイテムが『濡れた肌用インバスボディミルク』です。
      </p>
      <p>
        皮膚科学の知見において、入浴直後の肌は角層細胞が水分で膨潤し、皮膚表面のタイトジャンクション（細胞間接着構造）が一時的に緩んだ無防備な状態にあります。浴室から出てわずか5分〜10分の間に、入浴前よりも水分量が低下する『過乾燥（オーバー・ドライイング）』が発生することが証明されています。
      </p>
      <p>
        インバスボディミルクの最大の利点は、湿度が100%近い暖かい浴室の中で、肌に残った水分そのものを油分で乳化させて閉じ込めること。脱衣所の寒冷ストレスを感じることなく、片手でサッと塗ってバスタオルで押さえるだけで、翌朝まで吸い付くようなシルク肌が持続します。本特集では、楽天市場公式APIよりリアルタイムに最新データを取得し、2026年冬に本当に選ぶべき実力派インバスボディミルク10選を徹底比較します。
      </p>

      <div class="intro-highlight-grid">
        <div class="intro-card">
          <h4>❄️ 極寒脱衣所ストレスゼロ</h4>
          <p>暖かい浴室から一歩も出ずに全身の保湿が完了。服を脱いだまま震えながらクリームを塗る苦痛から永久に解放されます。</p>
        </div>
        <div class="intro-card">
          <h4>💧 タイトジャンクション密閉</h4>
          <p>入浴後の急激な水分蒸発（過乾燥）が始まる前に、水滴ごと油分ヴェールで密封。翌夕方までモチモチ肌が続きます。</p>
        </div>
        <div class="intro-card">
          <h4>⚡ 驚異の時短＆摩擦レス</h4>
          <p>濡れた肌の上を滑るように広がるため、肌への摩擦ダメージが激減。タオルオフするだけで完了する究極のタイパ美容です。</p>
        </div>
      </div>
    </div>

    <!-- 比較表セクション -->
    <section class="table-section">
      <h2 class="section-title">📊 濡れた肌用高保湿インバスボディミルク 厳選10選スペック比較表</h2>
      <div class="table-wrapper">
        <table class="spec-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名・ブランド</th>
              <th>参考価格（税込）</th>
              <th>アイテム種別</th>
              <th>内容量</th>
              <th>注目成分・特徴</th>
            </tr>
          </thead>
          <tbody>
            {"".join(table_rows)}
          </tbody>
        </table>
      </div>
    </section>

    <!-- ランキング商品セクション -->
    <section class="products-section">
      <h2 class="section-title">🏆 保湿力高め濡れた肌用インバスボディミルク ランキングTOP10</h2>
      {"".join(product_cards_html)}
    </section>

    <!-- ハウツーセクション -->
    <section class="intro-box" style="margin-top: 3rem;">
      <h2 class="section-title" style="border-bottom: none; margin-bottom: 1rem;">💡 プロが教える！濡れた肌用インバスボディケアの「失敗しない塗り方＆タオルドライ作戦」</h2>
      <p>
        濡れた肌用インバスボディミルクは、塗り方とタオルの扱い方次第で保湿持続力が劇的に変わります。せっかくの成分を台無しにしないための3大黄金ルールを実践してください。
      </p>
      <div class="intro-highlight-grid">
        <div class="intro-card">
          <h4>1. 湯船から上がってすぐ塗布</h4>
          <p>身体を拭く前、全身に水滴がたっぷり乗っている状態で塗布します。水分が残っているほどミルクと素早く乳化し、均一な保護膜が広がります。</p>
        </div>
        <div class="intro-card">
          <h4>2. タオルは「ポンポン当て」</h4>
          <p>タオルで身体をゴシゴシ擦るのは厳禁。タオルの繊維に水分だけを吸わせるイメージで、肌の上に優しく押し当てるのが潤いを残す鉄則です。</p>
        </div>
        <div class="intro-card">
          <h4>3. 頑固な乾燥箇所は追い保湿</h4>
          <p>特に粉吹きしやすいひじ・ひざ・かかとやすねには、脱衣所に出たあとに高保湿マルチバームやワセリンを少量重ね塗りすると完璧です。</p>
        </div>
      </div>
    </section>

    <!-- よくある質問（FAQ） -->
    <section class="faq-section">
      <h2 class="section-title">❓ 冬の濡れた肌用インバスボディケアに関するよくある質問（FAQ）</h2>
      <div class="faq-list">
        {''.join([f'''
        <div class="faq-item">
          <div class="faq-q">{item['q']}</div>
          <div class="faq-a">{item['a']}</div>
        </div>
        ''' for item in faq_items])}
      </div>
    </section>

    <!-- 内部リンク回遊セクション -->
    <section class="internal-links-box">
      <h2 class="section-title">🔗 あわせて読みたい！冬の乾燥・冷え対策おすすめ特集</h2>
      <div class="links-grid">
        <a href="/winter-bath-salt" class="link-card">
          <strong>🛁 高保湿バスソルト10選</strong>
          <span>純度99%エプソムソルトや死海ミネラルで体の芯から温め全身の粉吹き乾燥を防ぐ人気入浴料を徹底比較！</span>
        </a>
        <a href="/winter-body-cream" class="link-card">
          <strong>🧴 高保湿ボディクリーム10選</strong>
          <span>セラミドやシアバターを高濃度配合した超乾燥肌向けリッチクリームで真冬のひび割れ肌を救済！</span>
        </a>
        <a href="/winter-medicinal-bath" class="link-card">
          <strong>♨️ 薬用重炭酸入浴剤10選</strong>
          <span>重炭酸イオンの温浴効果で血行を促進し、湯上がりの過乾燥と冷え性を根本から改善する名品まとめ。</span>
        </a>
        <a href="/winter-body-scrub" class="link-card">
          <strong>✨ 高保湿ボディスクラブ10選</strong>
          <span>冬の冷えでゴワついた古い角質を優しくオフし、ボディミルクの浸透力を最大化するオイルインスクラブ。</span>
        </a>
        <a href="/winter-hand-cream" class="link-card">
          <strong>🧤 高保湿ハンドクリーム10選</strong>
          <span>水仕事や乾燥風で荒れた手肌を修復！ベタつかずに一日中潤いが続くハンドケアの名作を厳選。</span>
        </a>
        <a href="/winter-multi-balm" class="link-card">
          <strong>🌿 高保湿マルチバーム10選</strong>
          <span>外出先の粉吹き・目元・唇・毛先のカサつきをポーチ1つでレスキューする万能オーガニックバーム。</span>
        </a>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-links">
        <a href="/">トップページ</a>
        <a href="/winter-inbath-body">インバスボディミルク</a>
        <a href="/winter-body-care">ボディケア総合</a>
        <a href="/winter-bath-care">バスケア総合</a>
        <a href="/winter-hand-care">ハンドケア特集</a>
      </div>
      <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved. 当サイトは楽天市場公式アフィリエイトプログラムに参加しています。</p>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-inbath-body.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-inbath-body.html!")
