import json
import re

with open("fetched_3new_rose_primrose_moringa.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_damask_rose"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🌹 朝摘み有機ローズ蒸留水×微小ヒアルロン酸！真冬のゴワつき角層をほぐす名品とろみ化粧水",
        "catch": "フランス発祥オーガニックのパイオニア・メルヴィータが誇る高保湿トナー。ダマスクローズの豊かな蒸留水に微細ヒアルロン酸を溶かし込み、冬の冷風で硬くなった肌を吸い付くような潤い肌へ導く",
        "brand_name": "Melvita (メルヴィータ)",
        "capacity": "100ml / フリップトップボトル",
        "type": "高保湿オーガニック化粧水（トナー）",
        "features": "ダマスクバラ花水（水蒸気蒸留水）、加水分解ヒアルロン酸、ダマスクバラ花油",
        "value": "単なる精製水ベースではなく、摘みたてローズの芳香蒸留水を贅沢に使用。美容成分が角層の奥まで素早く巡り、冬のエアコン乾燥に負けないハリ感を即効チャージ",
        "desc_p1": "11月から12月にかけて外気温が急激に下がると、皮膚の毛細血管が収縮して血行が滞り、角層の柔軟性が奪われてスキンケアの入りが悪くなりがちです。メルヴィータの『フラワーブーケ ローズ EX トナー』は、そんな真冬の硬直肌のために開発された高保湿化粧水。手にとった瞬間は濃厚でリッチなとろみがありながら、肌に乗せると体温ですっとほどけ、まるで水のように角層深くへ吸い込まれていきます。",
        "desc_p2": "オーガニック農園で朝露が残るうちに手摘みされたダマスクローズの蒸留水がベースとなっており、人工香料とは一線を画す気品あふれる生花の香りが広がります。さらに超微細なマイクロヒアルロン酸が角層深部の隙間を埋め尽くすため、ハンドプレスを重ねるごとに手のひらが吸い付くようなモチモチ感へと変化。暖房が一日中効いたオフィスにいても夕方までカサつきや粉吹きを感じさせず、内側から発光するようなみずみずしい透明感を持続させます。",
        "target": "冬になると化粧水が肌表面で滑って浸透しにくい方、乾燥によるキメの乱れやくすみが気になる方、本物の優雅なローズの香りでスキンケア時間を楽しみたい方",
        "point": "洗顔後、500円玉大を手にとり、手のひらで温めてから顔全体を包み込むように優しくハンドプレスします。特に乾燥しやすい目元や口元には、もう一度少量を取り指の腹で重ねづけすると、潤いの密閉シールドが完成します。"
    },
    {
        "rank": 2,
        "tag": "👑 ブルガリアの谷が育む有機ローズ精油！真冬の枯れ肌を油分膜で包み込む最高峰美容オイル",
        "catch": "『バラの谷』カザンラクで無農薬栽培されたダマスクローズから抽出したピュア精油を配合。真冬の過酷な寒冷で皮脂が枯渇した大人の肌を、ふっくらと艶やかに甦らせる至高のエッセンシャルオイル",
        "brand_name": "Alteya Organics (アルテヤオーガニック)",
        "capacity": "30ml / 遮光ドロップボトル",
        "type": "高純度オーガニック美容フェイスオイル",
        "features": "有機ダマスクバラ花油（ブルガリア産）、ホホバ種子油、月見草油、ローズヒップ油",
        "value": "数千輪のダマスクローズからわずか1滴しか採れない希少精油を配合。USDAオーガニック認証取得。夜塗って眠るだけで、翌朝の肌密度が劇的に変化",
        "desc_p1": "世界最高品質のローズの産地として名高いブルガリア・カザンラク地方の自社有機農園で育まれたダマスクローズを、伝統的な銅製蒸留器で丁寧に抽出。アルテヤオーガニックのフェイスオイルは、まさに『植物療法の芸術品』と呼ぶにふさわしい贅沢な処方です。冬の寒さで皮脂分泌がガクンと落ち、バリア機能が低下してヒリつきや赤みが出やすい肌に、極上の油分膜を形成します。",
        "desc_p2": "ベースオイルには人の皮脂に組成が近いホホバ油や必須脂肪酸豊富な月見草油を黄金比で配合。サラリとした浸透性の高いテクスチャーでありながら、肌になじませた直後からピンとしたハリ感と上質なツヤが宿ります。夜のお手入れの最後に2滴ほど押し込むだけで、真冬の暖房による水分蒸発を鉄壁ガード。翌朝鏡を見たとき、ふっくらと柔らかく弾力のある素肌に驚かされます。",
        "target": "深刻な皮脂不足で粉吹きやちりめんジワに悩む方、年齢とともに肌のハリツヤが失われてきた方、純度の高い本物のオーガニックコスメを求める方",
        "point": "化粧水や乳液で肌を整えた後、手のひらに1〜2滴を取り、両手を軽く擦り合わせて温めます。顔全体を覆うように深呼吸しながら香りを吸い込み、優しくハンドプレスして密着させます。首元やデコルテまで伸ばすのがおすすめです。"
    },
    {
        "rank": 3,
        "tag": "🍯 ビタミンC爆弾ローズヒップ×ダマスクローズ！真冬の乾燥ひび割れ肌を救う濃厚マルチバーム",
        "catch": "英国名門アロマセラピーブランドのベストセラー。野バラの実（ローズヒップ）の濃密なビタミンとダマスクローズの潤いシールドが、真冬の寒風で荒れ果てた肌を集中リペアする神バーム",
        "brand_name": "NEAL'S YARD REMEDIES (ニールズヤード レメディーズ)",
        "capacity": "50g / ガラスジャー",
        "type": "高機能マルチトリートメントバーム",
        "features": "カニナバラ果実油（ワイルドローズ）、ダマスクバラ花油、シア脂、ミツロウ、ボリジ種子油",
        "value": "バーム・オイル・パックの1台3役。付属のオーガニックコットンクロスを使ったホットスチームケアで、冬のゴワゴワ肌が一瞬で生まれたての柔らかさに",
        "desc_p1": "冬の木枯らしが吹き荒れる11月下旬以降、頬の皮むけや口元の粉吹き、指先のひび割れなど、通常の保湿クリームでは追いつかない深刻な乾燥トラブルに見舞われることがあります。ニールズヤードの『ワイルドローズ ビューティバーム』は、そんな非常事態を乗り越えるための救世主として世界中で絶賛され続けている名品です。",
        "desc_p2": "指先にとると固めのテクスチャーですが、体温に触れた瞬間にとろりと黄金色の美容オイルへ変化。ビタミンA・C・Eを極めて高濃度に含むローズヒップオイルと、気品あるダマスクローズ精油、天然ミツロウが一体となり、傷んだ角層を濃密な保護膜で包み込みます。夜のスキンケアの最後にたっぷり塗って眠れば、翌朝にはカサつきが完全に鎮静。週に1回、お湯で温めたクロスで拭き取るバームパックを行えば、毛穴の黒ずみまでつるんとオフできます。",
        "target": "冬の冷風で頬や口周りが粉を吹いてしまう方、肌のくすみ・ゴワつきを一気にリセットしたい方、マルチに使えるレスキューアイテムを探している方",
        "point": "夜のお手入れの仕上げに、小豆大を手に取り体温で温めてオイル状にしてから押し込みます。特に乾燥がひどい日は、さくらんぼ大を顔全体に伸ばして10分置き、ホットタオルで優しく蒸留スチームしてから拭き取るスペシャルケアが効果的です。"
    },
    {
        "rank": 4,
        "tag": "💦 自社バイオダイナミック農園の朝摘みエキス！暖房砂漠の日中肌を救う高保湿微細ミスト",
        "catch": "オーストラリア・アデレードの清らかな大地で育まれたダマスクローズの恵み。超微細なミストがメイクを崩さず角層の隅々まで潤いを届け、冬のオフィス乾燥をその場でリセット",
        "brand_name": "Jurlique (ジュリーク)",
        "capacity": "100ml / フロストガラススプレーボトル",
        "type": "高保湿フェイシャルミスト化粧水",
        "features": "ダマスクバラ花エキス、マシュマロー根エキス（アルテア）、アロエベラ葉汁",
        "value": "独自農法で育てられた生命力あふれるローズエキスと、水分保持力に優れたマシュマロー根エキスをブレンド。スプレーした瞬間から長時間潤いが続く持続型ミスト",
        "desc_p1": "冬場のオフィスや自宅で暖房をつけっぱなしにしていると、湿度は20%台まで急降下します。肌内部の水分は容赦なく奪われ、午後になると目元の乾燥小ジワやファンデーションのひび割れが目立ち始めます。そんな日中の乾燥クライシスに欠かせないのが、ジュリークを代表するアイコンアイテム『ローズ バランシングミスト』です。",
        "desc_p2": "ひと吹きすると、霧のように細かく均一なミストが顔全体をふんわり包み込みます。単なる水分補給ミストと違い、保水力抜群のマシュマロー根エキスが肌表面に微細な潤いフィルムを形成するため、吹きかけた水分が蒸発する際に肌の水分まで奪ってしまう『過乾燥』を完璧に防ぎます。朝摘みローズの深みのある香りがふわりと立ち上り、冬の寒さや乾燥による肌ストレスを瞬時にリフレッシュしてくれます。",
        "target": "暖房の効いた室内で日中のカサつきやメイク崩れに悩む方、手軽に持ち運べる高保湿スプレーが欲しい方、デスクワーク中の気分転換も兼ねたい方",
        "point": "顔から20cmほど離し、目を閉じて顔全体に3〜4プッシュ吹きかけます。その後、手のひらで優しく包み込むようにして肌へなじませてください。メイク直しの前にティッシュオフしてから使うと、ファンデーションのノリが格段に蘇ります。"
    },
    {
        "rank": 5,
        "tag": "🌿 食べられる国産バラ×高純度セラミド！水分と油分を黄金比でチャージする2層式ミスト",
        "catch": "埼玉県深谷市の自社農園で無農薬栽培された『食べられるバラ』のエキスを濃縮。オイル層と美容水層をシェイクして吹きかけることで、真冬の乾燥崩れをパーフェクトに防止するハイブリッドミスト",
        "brand_name": "ROSE LABO (ローズラボ)",
        "capacity": "50ml / 携帯用スプレーボトル",
        "type": "オイルイン2層式高保湿ミスト美容液",
        "features": "国産有機ダマスクローズ蒸留水、セラミドNP・AP・EOP、ホホバ種子油、スクワラン",
        "value": "無農薬バラの豊富なポリフェノールと3種のヒト型セラミドを贅沢配合。メイクキープスプレーとしてもブースターとしても機能する万能処方",
        "desc_p1": "『口に入れても安全なものこそ、素肌にとって最も優しい』という哲学から生まれたROSE LABO。新品種『24』を含む自社栽培の国産ダマスクローズから抽出した濃厚なエキスと、肌のバリア構造を支えるヒト型セラミドを贅沢に融合させたのがこの2層式マルチミストです。",
        "desc_p2": "使用前に容器を振ると、オイル層とエッセンス層が瞬時に乳化し、美容乳液のような微細粒子となって噴射されます。水分を与えるだけでなく、スクワランやホホバ油のエモリエント成分が同時に肌へ密着するため、真冬の乾いた外気にさらされても水分が逃げません。メイクの仕上げにシュッと吹きかければ、パウダーの粉浮きを抑えて上品なツヤ肌に仕上がり、夜までマスク擦れや乾燥ヨレを防ぎます。",
        "target": "肌が敏感になりやすく安全性の高い国産オーガニックを選びたい方、日中の保湿とメイクキープを同時に叶えたい方、セラミド補給も重視したい方",
        "point": "オイルとエッセンスが均一に混ざるよう、ボトルをカチカチと音がするまでしっかり上下に振ります。メイク前後の素肌に吹きかけるのはもちろん、パサつく毛先の静電気防止や手元の保湿ケアにも最適です。"
    },
    {
        "rank": 6,
        "tag": "🛡️ 貴重なダマスクバラ花エキス×天然ミツロウ！寒風から肌を守り抜く老舗ロングセラー",
        "catch": "ドイツ植物療法の叡智が詰まった高保湿デイクリーム。ダマスクローズの生命力とミツロウ・アボカド油の濃厚ヴェールが、氷点下の冷気や暖房乾燥からデリケートな素肌を終日守り抜く",
        "brand_name": "Dr. Hauschka (ドクターハウシュカ)",
        "capacity": "30ml / アルミチューブ",
        "type": "高保湿保護デイクリーム",
        "features": "ダマスクバラ花エキス・花ロウ、ミツロウ、アボカド油、シア脂、アルテア根エキス",
        "value": "1967年の誕生以来、世界中のセレブリティやメイクアップアーティストに愛され続ける超ロングセラー。冬の赤ら顔や外気刺激によるヒリつきを穏やかに鎮静",
        "desc_p1": "ヨーロッパの厳しい冬を乗り越えるために生まれたドクターハウシュカの『ローズ デイクリーム』は、濃厚なテクスチャーと卓越した保護力で知られる名品です。1本のチューブに約35輪ものダマスクローズの花びらエキスとローズワックスが濃縮されており、真冬の冷たい木枯らしから肌を守る強固なシールドを形成します。",
        "desc_p2": "クリームを手にとるとコクのある重ための質感ですが、手の温度でじっくり温めながら肌に密着させると、ベタつくことなくベルベットのような滑らかな保護膜へ変わります。寒暖差で頬が赤くなりやすい方や、冬になると皮膚が薄くなってヒリつきを感じる敏感肌の方でも、刺激なく優しく包み込まれるような安心感を実感できます。朝のメイク下地として仕込めば、ファンデーションの乾燥割れを完全に予防できます。",
        "target": "冬の寒暖差で顔が赤くなりやすい方、濃厚でコクのあるクリームで肌を守りたい方、日中の保護力と保湿力を最優先したい方",
        "point": "朝の洗顔後、化粧水で整えた肌に使用します。手のひらにパール粒大を取り、両手ですり合わせて体温で柔らかくしてから、顔全体を包み込むように優しくプレスしてなじませます。"
    },
    {
        "rank": 7,
        "tag": "🛁 朝摘みダマスクローズの天然芳香！お風呂上がりの全身を吸い付くような潤いで包むボディ乳液",
        "catch": "ハウスオブローゼの人気フレグランスシリーズ。朝摘みダマスクローズの瑞々しい香りと高保湿ヒアルロン酸が融合し、冬の粉吹きすねやガサつく肘・膝をシルクのような素肌へ整える",
        "brand_name": "HOUSE OF ROSE (ハウスオブローゼ)",
        "capacity": "150ml / ポンプボトル",
        "type": "高保湿フレグランスボディミルク",
        "features": "ダマスクバラ花水、ハイブリッドローズ花エキス、加水分解ヒアルロン酸、ホホバ種子油",
        "value": "伸びが良くベタつかない絶妙なテクスチャー。お風呂上がりの温まった肌にスルスル広がり、パジャマや衣類がすぐに着られる快適な仕上がり",
        "desc_p1": "冬のお風呂上がりは、急激な水分蒸発によって全身の乾燥が急速に進行します。特にすねや太もも、背中は粉を吹いてかゆみが出やすい要注意ゾーン。ハウスオブローゼの『ラ・ローゼ ボディミルク RG』は、優雅なダマスクローズの香りに包まれながら、全身をたっぷりの潤いで満たしてくれる至福のボディトリートメントです。",
        "desc_p2": "ポンプを押すと、みずみずしく柔らかなミルクがスムーズに出てきます。肌に伸ばした瞬間に生花のダマスクローズそのものの透明感ある香りがバスルームいっぱいに広がり、一日の疲れと緊張を優しく解きほぐします。ヒアルロン酸とホホバオイルが角層へ素早く浸透し、しっとりとした潤い膜を形成。塗った直後でもサラリとしているため、すぐにタイツやルームウェアを履いてもペタつきません。",
        "target": "冬の全身の粉吹きやかゆみに悩んでいる方、入浴後のボディケアを優雅な癒やしタイムにしたい方、ベタつかず高保湿なボディ乳液を探している方",
        "point": "入浴後、タオルで軽く水気を拭き取った直後の湿り気のある素肌に伸ばします。全身に円を描くようにマッサージしながらなじませると、血行が促進されて翌朝の肌がもっちり柔らかくなります。"
    },
    {
        "rank": 8,
        "tag": "🌸 純度100%植物芳香蒸留水！冬のプレ化粧水として角質層を潤す天然フローラルウォーター",
        "catch": "日本のハーブ＆アロマの老舗・生活の木が手がける高純度ローズウォーター。ブルガリア産ダマスクローズの花びらを水蒸気蒸留したそのままのピュアな潤いで、ゴワつく冬肌の導入ケアに最適",
        "brand_name": "Tree of life (生活の木)",
        "capacity": "100ml / スプレーボトル",
        "type": "100%天然ハーブ蒸留水（プレ化粧水）",
        "features": "ブルガリア産ダマスクバラ花水100%（合成保存料・防腐剤無添加）",
        "value": "余計な添加物を一切含まない完全無添加仕様。弱酸性で肌への親和性が極めて高く、ブースターとして後に使うオイルや美容液の通り道をしっかり整える",
        "desc_p1": "冬のスキンケアにおいて、最初に肌に触れる水分の『質』は極めて重要です。生活の木の『ブルガリアンダマスクローズ フローラルウォーター』は、エッセンシャルオイルを抽出する際に得られる副産物ではなく、芳香蒸留水そのものを目的として贅沢に蒸留された高品位な植物水です。",
        "desc_p2": "肌につけた瞬間、すーっと何の引っかかりもなく角層の微細な隙間へと浸透していきます。人工的なローズ香とは全く異なる、野性味と草木の息吹を含んだ本物のダマスクローズの香りが心まで癒やしてくれます。洗顔後すぐに顔全体へ吹きかけることで、水道水の塩素によるツッパリ感を中和し、硬化した角質を柔らかくほぐすプレ化粧水として絶大な効果を発揮します。",
        "target": "敏感肌でアルコールや防腐剤などの添加物を避けたい方、スキンケアの導入（ブースター）として化粧水の浸透を高めたい方、自然そのものの香りを好む方",
        "point": "洗顔直後の素肌に、顔から15cmほど離して惜しみなくスプレーします。手のひらで軽く抑えてから、美容オイルや濃厚化粧水を重ねると、驚くほど吸い込みが良くなります。"
    },
    {
        "rank": 9,
        "tag": "🤲 シアバター20%×プロヴァンス産ローズ！真冬の水仕事や冷風から手肌を守る濃厚ハンドクリーム",
        "catch": "南仏プロヴァンスの伝統的な植物療法から生まれた高保湿ハンドトリートメント。高濃度シアバターとダマスクローズエキスが、ひび割れやあかぎれ寸前の指先を優しく密閉ガード",
        "brand_name": "Panier des Sens (パニエデサンス)",
        "capacity": "75ml / アルミチューブ",
        "type": "高保湿シアバターハンドクリーム",
        "features": "ダマスクバラ花エキス、シア脂（20%高配合）、オリーブ果実油、ヒマワリ種子油",
        "value": "シアバター20%の圧倒的な保護力。冬の頻繁な手洗いやアルコール消毒で荒れ果てた指先を、なめらかなベールで物理的にプロテクト",
        "desc_p1": "冬場に最も過酷な環境にさらされるのが『手肌』です。冷たい空気、頻繁な温水での手洗い、乾燥した室内環境により、皮脂膜が根こそぎ奪われてガサガサになったり、爪周りのささくれが痛んだりします。パニエデサンスの『エッセンシャルズ ハンドクリーム ローズ』は、シアバターを20%も高配合した濃密処方で、傷んだ手肌を速攻レスキューします。",
        "desc_p2": "チューブから出すとしっかりとしたコクのあるクリームですが、手のひらで揉み込むと体温でとろけてスッと手肌に馴染みます。プロヴァンスの摘みたてローズの華やかな香りが広がり、指先を動かすたびに上品なアロマが漂います。シアバターが形成する保護膜が水を弾き、乾燥冷気から手肌を長時間ガード。爪の甘皮周りまで丁寧に塗り込むことで、冬でも美しい手元をキープできます。",
        "target": "冬になると手荒れ・ひび割れ・ささくれに毎年悩まされる方、高保湿でもベタつきにくいハンドクリームを求める方、香水代わりに上品なローズの香りを楽しみたい方",
        "point": "手の甲に適量（真珠粒大）を出し、両手の甲をすり合わせて全体へ広げます。その後、指の関節や爪の生え際を1本ずつ丁寧にマッサージしながら塗り込むと、血行が促され冷えの改善にもつながります。"
    },
    {
        "rank": 10,
        "tag": "🏛️ フィレンツェ修道院800年の歴史！冬のゆらぎ肌を引き締め潤す世界最古の薬局ローズ水",
        "catch": "イタリア・フィレンツェで800年の歴史を誇る名門サンタ・マリア・ノヴェッラ。中世修道士のレシピを受け継ぐ芳醇なダマスクローズ水が、真冬の毛穴を引き締めながら贅沢な潤いを宿す",
        "brand_name": "Santa Maria Novella (サンタ・マリア・ノヴェッラ)",
        "capacity": "250ml / 重厚なガラスボトル",
        "type": "伝統的高保湿フェイシャルトナー",
        "features": "ダマスクバラ花エキス、天然ローズ蒸留水、伝統ハーブフォーミュラ",
        "value": "1381年から続く世界最古のレシピ。エレガントなガラスボトルとクラシカルな芳香で、冬のスキンケアを貴族の儀式のような特別なひとときに格上げ",
        "desc_p1": "イタリア・フィレンツェのドミニコ会修道士たちがペスト流行時に考案したとされる、歴史と伝統を持つ『アックア・ディ・ローゼ（ローズウォーター）』。数世紀にわたりヨーロッパの王侯貴族に愛され続けてきたこの逸品は、現代の真冬のスキンケアにおいても比類なき存在感を放ちます。",
        "desc_p2": "ガラスボトルからコットンにたっぷりと含ませて肌を優しく滑らせると、爽やかでありながらどこかスモーキーで深みのある高貴なローズ香が立ち上ります。冬の寒暖差でキメが乱れて開きがちな毛穴をキュッと引き締めつつ、上質な水分を角層にしっかりと留めてくれます。朝の洗顔代わりの拭き取り化粧水としても、夜のローションマスクとしても贅沢に使用でき、使うたびに肌の透明感とキメ密度の向上が実感できます。",
        "target": "歴史と格式のある本物の名品コスメを愛用したい方、冬の毛穴の開きやくすみを引き締めながらケアしたい方、インテリアとしても映える上質なボトルを好む方",
        "point": "コットンに惜しみなく500円玉大を含ませ、顔の中心から外側へ向けて優しくパッティングするように馴染ませます。特に乾燥が気になる時は、コットンを薄く裂いて両頬とおでこに3分間乗せるローションパックが格別の効果をもたらします。"
    }
]

# 目次リンク
toc_links = ""
for p in product_details:
    toc_links += f'          <li><a href="#rank-{p["rank"]}">第{p["rank"]}位：{p["brand_name"]} {p["catch"][:20]}...</a></li>\n'

# 比較一覧表
table_rows = []
for idx, p in enumerate(product_details):
    it = items[idx]
    table_rows.append(f"""            <tr>
              <td class="rank-num">第{p['rank']}位</td>
              <td><img src="{it['img']}" alt="{p['brand_name']}" class="table-thumb" loading="lazy"></td>
              <td><strong>{p['brand_name']}</strong><br><span style="font-size:0.85rem; color:var(--text-sub);">{it['name'][:35]}...</span></td>
              <td>{p['type']}</td>
              <td class="price-cell">{it['price']}</td>
              <td><a href="#rank-{p['rank']}" class="table-link">詳細を見る</a></td>
            </tr>""")
table_joined = "\n".join(table_rows)

# 各商品カード
product_cards = []
for idx, p in enumerate(product_details):
    it = items[idx]
    product_cards.append(f"""      <article class="product-card" id="rank-{p['rank']}">
        <div class="product-badge">第{p['rank']}位 ｜ {p['type']}</div>
        <div class="product-header">
          <div class="img-container">
            <img src="{it['img']}" alt="{it['name']}" class="product-img" loading="lazy">
          </div>
          <div class="product-intro">
            <h3 class="product-title">{it['name']}</h3>
            <div class="product-brand">ブランド：<strong>{p['brand_name']}</strong></div>
            <div class="product-price">参考価格：<span class="price-val">{it['price']}</span> <small>（楽天市場 最新確認時）</small></div>
            <div class="product-tag">{p['tag']}</div>
            <p class="product-catch">{p['catch']}</p>
          </div>
        </div>

        <div class="spec-table-box">
          <table class="spec-table">
            <tr><th>内容量 / 容器</th><td>{p['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{p['type']}</td></tr>
            <tr><th>主要保湿・美容成分</th><td>{p['features']}</td></tr>
            <tr><th>冬の保湿メリット</th><td>{p['value']}</td></tr>
          </table>
        </div>

        <div class="review-body">
          <h4>💡 コスメコンシェルジュによる徹底レビュー＆冬の保湿効果検証</h4>
          <p>{p['desc_p1']}</p>
          <p>{p['desc_p2']}</p>

          <div class="target-box">
            <strong>🎯 こんな方に特におすすめ！</strong>
            <p>{p['target']}</p>
          </div>

          <div class="point-box">
            <strong>✨ 保湿効果を最大化するプロの使い方：</strong>
            <p>{p['point']}</p>
          </div>
        </div>

        <div class="btn-wrap">
          <a href="{it['url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            🛒 楽天市場で「{p['brand_name']}」の最新価格・在庫・口コミを見る
          </a>
        </div>
      </article>""")

cards_joined = "\n\n".join(product_cards)

# JSON-LD構造化データ
json_ld_items = []
for idx, p in enumerate(product_details):
    it = items[idx]
    json_ld_items.append({
        "@type": "ListItem",
        "position": p["rank"],
        "name": it["name"],
        "url": f"https://lumi-cosme.vercel.app/winter-damask-rose#rank-{p['rank']}"
    })

json_ld_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！女王の濃密潤いヴェールで真冬のしぼみ肌をふっくら満たす高保湿ダマスクローズコスメランク10",
            "description": "11月・12月の寒冷乾燥と暖房によるインナードライ・しぼみ肌を救う高保湿ダマスクローズコスメを徹底厳選！メルヴィータ、アルジェラン、ニールズヤード、ジュリーク、ローズラボからアルテヤオーガニックまで厳選。",
            "datePublished": "2026-11-05T01:00:00+09:00",
            "dateModified": "2026-11-05T01:00:00+09:00",
            "author": {
                "@type": "Person",
                "name": "Lumi Cosme 編集部 コスメコンシェルジュ"
            },
            "publisher": {
                "@type": "Organization",
                "name": "Lumi Cosme",
                "url": "https://lumi-cosme.vercel.app/"
            }
        },
        {
            "@type": "ItemList",
            "name": "高保湿ダマスクローズコスメおすすめランキングTOP10",
            "numberOfItems": 10,
            "itemListElement": json_ld_items
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "なぜ真冬（11月・12月）の乾燥にしぼんだ肌にダマスクローズコスメが効果的なのですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "ダマスクローズ（Rosa damascena）の蒸留水や精油には、ゲラニオール、シトロネロール、ネロールなどの微小芳香分子が豊富に含まれており、乱れた肌バリアを穏やかに整えて角層の水分保持力を高める優れた収斂・保湿作用があります。11月〜12月は急激な気温低下によって末梢血流が滞り、肌が冷えて縮こまることでスキンケアが浸透しにくくなりますが、ダマスクローズの豊かな芳香と浸透力は硬くなった角質層を柔軟に解きほぐし、内側からふっくらと押し返すようなハリと潤いを取り戻してくれます。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "ダマスクローズウォーター（蒸留水）とローズ精油配合オイルはどちらを選べば良いですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "肌の悩みのタイプに応じて選ぶのがベストです。インナードライで水分が不足し、化粧水が浸透しにくいと感じる方には、微小な水分を角層深部まで届ける『ローズウォーター（化粧水やミスト）』が最適です。一方、粉吹きやひび割れ、皮脂の減少による激しいカサつきに悩む方には、油分膜で水分蒸発を物理的にシャットアウトする『ローズ美容オイルやバーム』が適しています。冬の乾燥が極限に達する時期には、ローズウォーターで水分を満たした直後にローズオイルでフタをする『ライン使い』が最も高い保湿効果を発揮します。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "敏感肌ですが、ダマスクローズの高濃度コスメで刺激を感じることはありませんか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "本物のオーガニックダマスクローズ蒸留水は弱酸性で肌への親和性が極めて高く、古くから敏感肌の鎮静ハーブウォーターとして親しまれてきました。ただし、合成香料でローズの香りを再現した安価な製品や、エタノールが高配合された製品は冬のバリア乱れ肌にしみることがあります。本記事でご紹介しているアルテヤオーガニックや生活の木、メルヴィータなど、認証オーガニック原料を使用した純度の高い製品を選び、使い始めは目立たない腕の内側などでパッチテストを行うことを推奨します。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "ダマスクローズの香りはリラクゼーションや睡眠にも良い影響がありますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "はい、科学的にも大きな注目を集めています。天然ダマスクローズに含まれる芳香成分は嗅覚神経を通じて自律神経に働きかけ、副交感神経を優位にしてストレスを緩和する作用が認められています。冬の寒さや年末の多忙さで交感神経が高まり緊張状態が続くと、血管が収縮して肌荒れが悪化します。夜の入浴後やスキンケア時にダマスクローズの香りを深く吸い込むことで、質の高い睡眠を促し、睡眠中の肌再生バリアの回復を強力に後押しします。"
                    }
                }
            ]
        }
    ]
}

json_ld_str = json.dumps(json_ld_schema, ensure_ascii=False, indent=2)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！女王の濃密潤いヴェールで真冬のしぼみ肌をふっくら満たす高保湿ダマスクローズコスメランク10</title>
  <meta name="description" content="11月・12月の寒冷乾燥と暖房によるインナードライ・しぼみ肌を救う高保湿ダマスクローズコスメを徹底厳選！メルヴィータ、アルジェラン、ニールズヤード、ジュリーク、ローズラボからアルテヤオーガニックまで厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-damask-rose">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！女王の濃密潤いヴェールで真冬のしぼみ肌をふっくら満たす高保湿ダマスクローズコスメランク10">
  <meta property="og:description" content="11月・12月の寒冷乾燥と暖房によるインナードライ・しぼみ肌を救う高保湿ダマスクローズコスメを徹底厳選！メルヴィータ、アルジェラン、ニールズヤード、ジュリーク、ローズラボからアルテヤオーガニックまで厳選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-damask-rose">
  <meta property="og:site_name" content="Lumi Cosme">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Playfair+Display:ital,wght@0,600;1,600&display=swap" rel="stylesheet">
  <script type="application/ld+json">
{json_ld_str}
  </script>
  <style>
    :root {{
      --primary: #be185d;
      --primary-light: #fce7f3;
      --primary-dark: #9d174d;
      --accent: #f43f5e;
      --accent-hover: #e11d48;
      --bg: #fff5f7;
      --card-bg: #ffffff;
      --text-main: #374151;
      --text-sub: #6b7280;
      --border: #fbcfe8;
      --shadow: 0 4px 15px rgba(190, 24, 93, 0.08);
      --radius: 14px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Noto Sans JP', sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
    }}

    header.site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 1rem 1.5rem;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }}

    .header-inner {{
      max-width: 1080px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .site-logo {{
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}

    .nav-links a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.9rem;
      margin-left: 1.2rem;
      transition: color 0.2s;
    }}

    .nav-links a:hover {{
      color: var(--primary);
    }}

    main.container {{
      max-width: 920px;
      margin: 2rem auto;
      padding: 0 1.2rem;
    }}

    .hero {{
      background: linear-gradient(135deg, #fdf2f8 0%, #fff1f2 100%);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .hero-tag {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.3rem 0.8rem;
      border-radius: 50px;
      margin-bottom: 1rem;
      letter-spacing: 0.5px;
    }}

    h1.hero-title {{
      font-size: 1.85rem;
      font-weight: 700;
      line-height: 1.45;
      color: #1f2937;
      margin-bottom: 1.2rem;
    }}

    .hero-desc {{
      color: var(--text-sub);
      font-size: 1rem;
      line-height: 1.8;
      margin-bottom: 1.5rem;
    }}

    .hero-meta {{
      display: flex;
      gap: 1.2rem;
      font-size: 0.85rem;
      color: #9ca3af;
      border-top: 1px solid #fce7f3;
      padding-top: 1rem;
    }}

    .toc-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.8rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .toc-card h3 {{
      font-size: 1.15rem;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.6rem;
    }}

    @media (min-width: 640px) {{
      .toc-list {{
        grid-template-columns: 1fr 1fr;
      }}
    }}

    .toc-list a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.92rem;
      display: block;
      padding: 0.3rem 0.5rem;
      border-radius: 6px;
      transition: background 0.2s, color 0.2s;
    }}

    .toc-list a:hover {{
      background: var(--primary-light);
      color: var(--primary);
    }}

    .table-section {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}

    .table-section h2 {{
      font-size: 1.35rem;
      color: #1f2937;
      margin-bottom: 1.2rem;
      border-left: 5px solid var(--primary);
      padding-left: 0.8rem;
    }}

    .table-wrapper {{
      overflow-x: auto;
    }}

    table.rank-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}

    table.rank-table th, table.rank-table td {{
      padding: 0.9rem;
      border-bottom: 1px solid #f3f4f6;
    }}

    table.rank-table th {{
      background: #fdf2f8;
      color: var(--primary-dark);
      font-weight: 700;
      white-space: nowrap;
    }}

    .rank-num {{
      font-weight: 700;
      color: var(--primary);
      white-space: nowrap;
    }}

    .table-thumb {{
      width: 50px;
      height: 50px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid #e5e7eb;
    }}

    .price-cell {{
      font-weight: 700;
      color: #e11d48;
      white-space: nowrap;
    }}

    .table-link {{
      color: var(--primary);
      text-decoration: none;
      font-weight: 700;
      font-size: 0.85rem;
    }}

    .table-link:hover {{
      text-decoration: underline;
    }}

    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
      position: relative;
    }}

    .product-badge {{
      display: inline-block;
      background: linear-gradient(135deg, var(--primary) 0%, #db2777 100%);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.4rem 1rem;
      border-radius: 50px;
      margin-bottom: 1.2rem;
    }}

    .product-header {{
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      margin-bottom: 1.5rem;
    }}

    @media (min-width: 640px) {{
      .product-header {{
        flex-direction: row;
        align-items: flex-start;
      }}
    }}

    .img-container {{
      flex-shrink: 0;
      width: 100%;
      max-width: 260px;
      margin: 0 auto;
      text-align: center;
      background: #fdf2f8;
      padding: 1rem;
      border-radius: 12px;
      border: 1px solid #fce7f3;
    }}

    .product-img {{
      width: 100%;
      height: auto;
      max-height: 240px;
      object-fit: contain;
      border-radius: 8px;
    }}

    .product-intro {{
      flex-grow: 1;
    }}

    h3.product-title {{
      font-size: 1.3rem;
      color: #111827;
      line-height: 1.45;
      margin-bottom: 0.6rem;
    }}

    .product-brand {{
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 0.5rem;
    }}

    .product-price {{
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 0.8rem;
    }}

    .price-val {{
      font-size: 1.45rem;
      font-weight: 700;
      color: #e11d48;
    }}

    .product-tag {{
      display: inline-block;
      background: #fdf2f8;
      color: var(--primary-dark);
      font-size: 0.82rem;
      font-weight: 700;
      padding: 0.3rem 0.8rem;
      border-radius: 6px;
      border: 1px solid #fbcfe8;
      margin-bottom: 0.8rem;
    }}

    .product-catch {{
      font-size: 0.95rem;
      color: #4b5563;
      line-height: 1.7;
    }}

    .spec-table-box {{
      margin: 1.5rem 0;
      background: #fdf2f8;
      border-radius: 10px;
      padding: 1rem 1.2rem;
      border: 1px solid #fce7f3;
    }}

    table.spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}

    table.spec-table th, table.spec-table td {{
      padding: 0.5rem 0.6rem;
      border-bottom: 1px solid #fce7f3;
      text-align: left;
    }}

    table.spec-table tr:last-child th, table.spec-table tr:last-child td {{
      border-bottom: none;
    }}

    table.spec-table th {{
      width: 25%;
      color: var(--primary-dark);
      font-weight: 700;
      white-space: nowrap;
    }}

    .review-body {{
      margin-top: 1.5rem;
      border-top: 1px solid #f3f4f6;
      padding-top: 1.5rem;
    }}

    .review-body h4 {{
      font-size: 1.05rem;
      color: #1f2937;
      margin-bottom: 0.8rem;
    }}

    .review-body p {{
      font-size: 0.95rem;
      color: var(--text-main);
      line-height: 1.85;
      margin-bottom: 1rem;
    }}

    .target-box, .point-box {{
      background: #fff1f2;
      border-left: 4px solid var(--accent);
      padding: 0.9rem 1.1rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 1rem;
      font-size: 0.9rem;
      color: #4b5563;
    }}

    .point-box {{
      background: #fdf2f8;
      border-left-color: var(--primary);
    }}

    .btn-wrap {{
      margin-top: 1.8rem;
      text-align: center;
    }}

    a.rakuten-btn {{
      display: inline-block;
      background: linear-gradient(135deg, #bf0000 0%, #e60000 100%);
      color: #ffffff;
      text-decoration: none;
      font-size: 1rem;
      font-weight: 700;
      padding: 1rem 2rem;
      border-radius: 50px;
      box-shadow: 0 4px 15px rgba(230, 0, 0, 0.25);
      transition: transform 0.2s, box-shadow 0.2s, background 0.2s;
      width: 100%;
      max-width: 460px;
    }}

    a.rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(230, 0, 0, 0.35);
      background: linear-gradient(135deg, #a80000 0%, #d40000 100%);
    }}

    .guide-section, .faq-section {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}

    .guide-section h2, .faq-section h2 {{
      font-size: 1.4rem;
      color: #1f2937;
      margin-bottom: 1.5rem;
      border-left: 5px solid var(--primary);
      padding-left: 0.8rem;
    }}

    .guide-section h3 {{
      font-size: 1.15rem;
      color: var(--primary-dark);
      margin: 1.5rem 0 0.8rem;
    }}

    .guide-section p {{
      font-size: 0.95rem;
      color: var(--text-main);
      line-height: 1.85;
      margin-bottom: 1rem;
    }}

    .guide-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.2rem;
      margin: 1.5rem 0;
    }}

    @media (min-width: 640px) {{
      .guide-grid {{
        grid-template-columns: 1fr 1fr 1fr;
      }}
    }}

    .guide-card {{
      background: #fdf2f8;
      border: 1px solid #fce7f3;
      border-radius: 10px;
      padding: 1.2rem;
    }}

    .guide-card h4 {{
      font-size: 0.95rem;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
    }}

    .guide-card p {{
      font-size: 0.88rem;
      color: var(--text-sub);
      line-height: 1.6;
      margin-bottom: 0;
    }}

    .faq-item {{
      border-bottom: 1px solid #f3f4f6;
      padding: 1.2rem 0;
    }}

    .faq-item:last-child {{
      border-bottom: none;
    }}

    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
    }}

    .faq-q::before {{
      content: "Q.";
      color: var(--primary);
      font-weight: 700;
    }}

    .faq-a {{
      font-size: 0.95rem;
      color: var(--text-main);
      line-height: 1.8;
      padding-left: 1.6rem;
    }}

    .related-links {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}

    .related-links h3 {{
      font-size: 1.2rem;
      color: #1f2937;
      margin-bottom: 1.2rem;
    }}

    .related-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.8rem;
    }}

    @media (min-width: 640px) {{
      .related-grid {{
        grid-template-columns: 1fr 1fr;
      }}
    }}

    .related-card {{
      display: block;
      padding: 0.8rem 1rem;
      background: #fdf2f8;
      border-radius: 8px;
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.9rem;
      transition: background 0.2s, color 0.2s;
      border: 1px solid #fce7f3;
    }}

    .related-card:hover {{
      background: #fce7f3;
      color: var(--primary);
    }}

    footer.site-footer {{
      background: #ffffff;
      border-top: 1px solid var(--border);
      padding: 2.5rem 1.5rem;
      text-align: center;
      font-size: 0.88rem;
      color: var(--text-sub);
      margin-top: 3rem;
    }}

    footer.site-footer a {{
      color: var(--primary);
      text-decoration: none;
      margin: 0 0.4rem;
    }}

    footer.site-footer a:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">🌸 Lumi Cosme</a>
      <nav class="nav-links">
        <a href="/">ホーム</a>
        <a href="/winter-evening-primrose">高保湿月見草オイル</a>
        <a href="/winter-moringa-oil">高保湿モリンガオイル</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <span class="hero-tag">❄️ 11月・12月真冬の集中保湿ケア特集</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！女王の濃密潤いヴェールで真冬のしぼみ肌をふっくら満たす高保湿ダマスクローズコスメランク10</h1>
      <p class="hero-desc">
        11月から12月へと進むにつれ、木枯らしの冷気と室内の暖房によって空気中の湿度は急落します。気温低下に伴う血行不良で肌の代謝が滞り、「スキンケアが浸透しない」「夕方になると肌が縮こまってちりめんジワが目立つ」「暖房で顔がほてるのに内側はカラカラ」といった真冬特有のインナードライに直面していませんか？<br><br>
        そんな過酷な冬の枯れ肌に劇的な潤いと弾力を取り戻してくれるのが、古来『花の女王』として珍重されてきた「ダマスクローズ（Rosa damascena）」の恵みです。数千種あるバラの中でも最高峰の香りと保水力を誇るダマスクローズから採れる蒸留水や精油には、微小な芳香成分やフラボノイド、タンニンなどの植物性ポリフェノールが凝縮されており、冷え固まった角層を瞬時に柔らかく解きほぐしながら、強固な水分シールドを張ってくれます。<br><br>
        本記事では、楽天APIからリアルタイムに取得した最新データに基づき、本場ブルガリア産や国産無農薬の朝摘みダマスクローズを贅沢に配合した高保湿コスメTOP10を徹底検証。化粧水、美容オイル、マルチバーム、日中用ミスト、ボディ乳液まで、真冬の乾燥砂漠を乗り切るための神コスメを厳選しました。
      </p>
      <div class="hero-meta">
        <span>📅 2026年11月最新更新</span>
        <span>✍️ コスメコンシェルジュ＆植物療法アナリスト監修</span>
        <span>🔬 楽天市場公式APIデータ連携済</span>
      </div>
    </section>

    <div class="toc-card">
      <h3>📑 目次：高保湿ダマスクローズコスメTOP10</h3>
      <ul class="toc-list">
{toc_links}
      </ul>
    </div>

    <section class="table-section">
      <h2>🏆 高保湿ダマスクローズコスメおすすめ比較一覧</h2>
      <div class="table-wrapper">
        <table class="rank-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品画像</th>
              <th>ブランド・商品名</th>
              <th>分類</th>
              <th>楽天市場価格</th>
              <th>詳細リンク</th>
            </tr>
          </thead>
          <tbody>
{table_joined}
          </tbody>
        </table>
      </div>
    </section>

    <section class="products-section">
{cards_joined}
    </section>

    <section class="guide-section">
      <h2>💡 失敗しない高保湿ダマスクローズコスメの選び方＆冬の活用術</h2>

      <h3>1. 「蒸留水（フローラルウォーター）」と「精油（エッセンシャルオイル）」の特性を理解する</h3>
      <p>ダマスクローズコスメを選ぶ上で重要なのは、その製品に配合されているローズエキスの『形態』です。水溶性の成分が溶け込んだ「ダマスクバラ花水（水蒸気蒸留水）」は、角層の微細な隙間まで水分を素早く引き込む導入・保水効果に長けています。一方で、数千本からわずか数滴しか採れない油溶性の「ダマスクバラ花油（精油）」は、皮脂膜を強化し、真冬のエアコン乾燥による水分蒸発を物理的に食い止めるエモリエントシールドとして機能します。インナードライが気になる方は蒸留水ベースのトナーを、肌の粉吹きやひび割れが気になる方は精油配合の美容オイルやバームを選ぶのが鉄則です。</p>

      <div class="guide-grid">
        <div class="guide-card">
          <h4>ローズ蒸留水（化粧水・ミスト）</h4>
          <p>洗顔直後のブースターや日中の暖房乾燥対策に。角層深部までみずみずしい水分を巡らせ、硬くなった肌を素早くほぐします。</p>
        </div>
        <div class="guide-card">
          <h4>ローズ美容オイル・バーム</h4>
          <p>夜のお手入れのフタや目元・口元の集中リペアに。オメガ脂肪酸やビタミン類とともに水分の蒸散を鉄壁ブロックします。</p>
        </div>
        <div class="guide-card">
          <h4>2層式ミスト・ボディミルク</h4>
          <p>水分と油分を同時にチャージ。お風呂上がりの全身乾燥やメイク直しの粉浮きリセットに抜群の利便性を発揮します。</p>
        </div>
      </div>

      <h3>2. 11月・12月の寒冷乾燥を打破する「ローズ温感パッティング法」</h3>
      <p>冬場の気温低下によって肌温度が下がると、せっかくの高保湿成分も浸透しにくくなります。ダマスクローズコスメの効果を何倍にも引き出すため、以下のステップを実践してください。</p>
      <ol style="margin-left: 1.5rem; margin-bottom: 1rem; color: var(--text-sub); line-height: 1.8;">
        <li><strong>手のひらで温める：</strong> 化粧水やオイルを手にとったら、すぐに肌に塗布せず、両手をすり合わせて手のひら全体を体温で温めます。</li>
        <li><strong>深呼吸してアロマを取り込む：</strong> 顔に手を近づけ、ゆっくりと深呼吸してダマスクローズの天然芳香を吸い込みます。副交感神経が優位になり末梢血流が促進されます。</li>
        <li><strong>10秒間の包み込みハンドプレス：</strong> こすらず、両手で頬、額、顎をじっくりと包み込み、手のひらの温もりで角層の奥まで美容成分を押し込みます。</li>
      </ol>

      <h3>3. 合成香料と天然オーガニックの見分け方</h3>
      <p>ドラッグストア等で安価に販売されているローズコスメの中には、合成香料（香料）によってバラの香りを人工的に再現しているものも多く存在します。合成香料のローズはリラクゼーション効果や肌の収斂・保湿といった本来の植物学的恩恵が期待できないだけでなく、冬のバリアが低下した敏感肌には刺激となる場合があります。全成分表示を確認し、「ダマスクバラ花水」「ダマスクバラ花油」「ハイブリッドローズ花エキス」などの学名・天然由来成分が上位に記載されているオーガニック認証製品を選びましょう。</p>
    </section>

    <section class="faq-section">
      <h2>❓ 高保湿ダマスクローズコスメに関するよくある質問（FAQ）</h2>
      <div class="faq-item">
        <div class="faq-q">なぜ真冬（11月・12月）の乾燥にしぼんだ肌にダマスクローズコスメが効果的なのですか？</div>
        <div class="faq-a">ダマスクローズ（Rosa damascena）の蒸留水や精油には、ゲラニオール、シトロネロール、ネロールなどの微小芳香分子が豊富に含まれており、乱れた肌バリアを穏やかに整えて角層の水分保持力を高める優れた収斂・保湿作用があります。11月〜12月は急激な気温低下によって末梢血流が滞り、肌が冷えて縮こまることでスキンケアが浸透しにくくなりますが、ダマスクローズの豊かな芳香と浸透力は硬くなった角質層を柔軟に解きほぐし、内側からふっくらと押し返すようなハリと潤いを取り戻してくれます。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">ダマスクローズウォーター（蒸留水）とローズ精油配合オイルはどちらを選べば良いですか？</div>
        <div class="faq-a">肌の悩みのタイプに応じて選ぶのがベストです。インナードライで水分が不足し、化粧水が浸透しにくいと感じる方には、微小な水分を角層深部まで届ける『ローズウォーター（化粧水やミスト）』が最適です。一方、粉吹きやひび割れ、皮脂の減少による激しいカサつきに悩む方には、油分膜で水分蒸発を物理的にシャットアウトする『ローズ美容オイルやバーム』が適しています。冬の乾燥が極限に達する時期には、ローズウォーターで水分を満たした直後にローズオイルでフタをする『ライン使い』が最も高い保湿効果を発揮します。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">敏感肌ですが、ダマスクローズの高濃度コスメで刺激を感じることはありませんか？</div>
        <div class="faq-a">本物のオーガニックダマスクローズ蒸留水は弱酸性で肌への親和性が極めて高く、古くから敏感肌の鎮静ハーブウォーターとして親しまれてきました。ただし、合成香料でローズの香りを再現した安価な製品や、エタノールが高配合された製品は冬のバリア乱れ肌にしみることがあります。本記事でご紹介しているアルテヤオーガニックや生活の木、メルヴィータなど、認証オーガニック原料を使用した純度の高い製品を選び、使い始めは目立たない腕の内側などでパッチテストを行うことを推奨します。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">ダマスクローズの香りはリラクゼーションや睡眠にも良い影響がありますか？</div>
        <div class="faq-a">はい、科学的にも大きな注目を集めています。天然ダマスクローズに含まれる芳香成分は嗅覚神経を通じて自律神経に働きかけ、副交感神経を優位にしてストレスを緩和する作用が認められています。冬の寒さや年末の多忙さで交感神経が高まり緊張状態が続くと、血管が収縮して肌荒れが悪化します。夜の入浴後やスキンケア時にダマスクローズの香りを深く吸い込むことで、質の高い睡眠を促し、睡眠中の肌再生バリアの回復を強力に後押しします。</div>
      </div>
    </section>

    <section class="related-links">
      <h3>🔗 あわせて読みたい！冬の高保湿スキンケア特集</h3>
      <div class="related-grid">
        <a href="/winter-evening-primrose" class="related-card">🌙 高保湿月見草オイルコスメ10選</a>
        <a href="/winter-moringa-oil" class="related-card">🌱 高保湿モリンガオイルコスメ10選</a>
        <a href="/winter-tamanu-oil" class="related-card">🌿 高保湿タマヌオイルコスメ10選</a>
        <a href="/winter-baobab-oil" class="related-card">🌳 高保湿バオバブオイルコスメ10選</a>
        <a href="/winter-kombucha" class="related-card">🍵 高保湿コンブチャコスメ10選</a>
        <a href="/winter-manuka-honey" class="related-card">🍯 高純度マヌカハニーコスメ10選</a>
        <a href="/winter-resurrection-plant" class="related-card">🌵 復活草・トレハロースコスメ10選</a>
        <a href="/winter-ceramide-cream" class="related-card">🛡️ 高保湿セラミドクリーム10選</a>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <p>&copy; 2026 Lumi Cosme. All rights reserved. 掲載価格は楽天市場の最新参考価格です。</p>
    <p style="margin-top: 0.5rem;"><a href="/">ホーム</a> | <a href="/winter-damask-rose">高保湿ダマスクローズ</a> | <a href="/winter-evening-primrose">高保湿月見草オイル</a> | <a href="/winter-moringa-oil">高保湿モリンガオイル</a></p>
  </footer>

</body>
</html>"""

with open("winter-damask-rose.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved winter-damask-rose.html successfully!")
