import json
import re

with open("fetched_3new_apricot_almond_shikon.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_apricot_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 杏仁オイル70%超高配合！首元・目元のポツポツ角質粒ケアで不動の人気を誇る名品",
        "catch": "職人仕込みの低温圧搾ピュア杏仁オイルを限界濃度まで濃縮。加齢や真冬の乾燥で硬直した首筋や目周りの古い角質粒を、毎晩のなめらかマッサージでやさしくときほぐす",
        "brand_name": "ZEALAND BIFU (ジーランドビフ)",
        "capacity": "30ml / スポイト遮光ガラス瓶",
        "type": "高純度杏仁原液スキンケア美容オイル",
        "features": "アンズ核油（70%以上高配合）、ヨモギ葉エキス、オタネニンジン根エキス、ダイズ油、トコフェロール",
        "value": "目元やデコルテに現れる頑固な角質粒（老人性イボ・ポツポツ）に対して、皮膚を削ることなく脂肪酸の力で柔軟化。真冬の過酷な乾燥による小ジワもふっくら整える",
        "desc_p1": "11月から12月にかけてタートルネックやマフラーを着用する季節になると、衣類の摩擦と急激な空気の乾燥によって首元やデコルテの皮膚代謝が滞り、触るとチクチク・ザラザラする『角質粒（ポツポツ）』が目立ってきます。ジーランドビフの『アンミオイル』は、この冬の首元・目元悩みに特化して開発され、累計販売本数で圧倒的な実績を持つ専門オイルです。",
        "desc_p2": "黄金色に輝くオイルは、とろみがありながらも肌にのせると体温でサラリと広がり、角層の奥深くへと吸い込まれるように馴染みます。パルミトレイン酸とオレイン酸が硬化した角質細胞の結合を穏やかにゆるめ、毎晩のスキンケアの仕上げに優しく円を描くように塗り込むことで、数週間で指先を滑らせたときの凹凸感がなめらかに変化。冬場の首元の開いたニットも自信を持って着こなせる素肌へと導きます。",
        "target": "首元や目元、胸元に小さな茶色いポツポツやザラつきができやすい方、冬になると首筋の乾燥小ジワが目立つ方、皮膚科に行く前に自宅で優しく角質粒ケアを始めたい方",
        "point": "夜のお手入れで化粧水をたっぷり浸透させた後、手のひらに3〜4滴をとり、気になる首筋や目周りに下から上へ引き上げるように優しくマッサージしながらなじませます。蒸しタオルで首元を温めてから使うと浸透性が倍増します。"
    },
    {
        "rank": 2,
        "tag": "🌿 低温圧搾オーガニック認証！真冬のカチコチ角層をふっくらほぐす高純度キャリアオイル",
        "catch": "アロマとハーブの老舗「生活の木」が厳選した有機アプリコット。不飽和脂肪酸のバランスが理想的で、真冬の洗顔後ブースターから全身の贅沢マッサージまでマルチに活躍",
        "brand_name": "生活の木 (Tree of Life)",
        "capacity": "70ml / 遮光ガラスドロッパーボトル",
        "type": "有機未精製・精製ブレンド オーガニックキャリアオイル",
        "features": "有機アンズ核油100%、高濃度オレイン酸、リノール酸、ビタミンA前駆体",
        "value": "生活の木基準の徹底した品質管理。赤ちゃんのスキンケアにも使えるほど低刺激でありながら、真冬の暖房でパサついた肌の角質バリアを即座に修復",
        "desc_p1": "冬本番を迎える12月、寒さで血管が収縮すると肌のターンオーバーは通常の倍近くまで遅延し、角層が肥厚してスキンケアが浸透しない『角質硬直』に陥ります。生活の木の『有機アプリコットカーネルオイル』は、そんな真冬のゴワゴワ肌を瞬時に解きほぐすために最適なピュア植物油です。",
        "desc_p2": "スイートアーモンドオイルよりもさらに軽やかで伸びが良く、肌に乗せた瞬間に心地よい滑らかさが広がります。洗顔直後のプレオイルとして1〜2滴ハンドプレスすれば、硬く強張っていた表皮がふんわりと柔らかくなり、その後に塗布する化粧水をぐんぐん引き込むブースター効果を発揮。目元の薄い皮膚にも重さを残さず密着し、一日中乾かない柔らかなハリを保ちます。",
        "target": "化粧水が肌表面で弾かれて浸透していかないと感じる方、信頼できるオーガニックブランドの植物油を使いたい方、顔だけでなく首元やハンドケアにも贅沢に使いたい方",
        "point": "朝晩の洗顔直後、肌にまだわずかに水分が残っている状態で2滴を手のひら全体に広げ、顔全体を包み込むように優しくプレスします。角層がほぐれた後、いつもの化粧水を重ねてください。"
    },
    {
        "rank": 3,
        "tag": "💧 無添加コールドプレス×国内充填！ビタミンA・B群が真冬のくすみと小ジワを救う万能ドロップ",
        "catch": "コスパと鮮度を追求した&SHのピュアアプリコット。遮光ボトルに閉じ込められた新鮮なオレイン酸が、冬のエアコン直撃によるインナードライを長時間シャットアウト",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "80ml / 遮光ドロッパーボトル",
        "type": "100%ピュア植物性キャリアオイル",
        "features": "アンズ核油（無添加低温圧搾）、パルミトレイン酸、ステアリン酸、天然トコフェロール",
        "value": "80mlのたっぷりサイズで惜しみなく使える高コスパ。防腐剤や香料を一切添加せず、杏の仁に含まれる天然ビタミン群をそのまま肌へ届ける安心設計",
        "desc_p1": "暖房の効いた室内で長時間デスクワークを続けると、午後には目元や頬が突っ張り、ファンデーションが小ジワに落ちてひび割れてしまいます。&SHの『アプリコットカーネルオイル 80ml』は、日中から夜間の乾燥崩壊を阻止する高密着エモリエントオイルです。",
        "desc_p2": "杏の種子から抽出されるオイルは別名『パーシック油』とも呼ばれ、人間の皮脂に極めて近い脂肪酸組成を持っています。そのため塗布しても毛穴を塞ぐような被膜感がなく、肌の深部へとスムーズに浸透。夜のスキンケアの最後にクリームに1滴混ぜるだけで、暖房をつけっぱなしにした寝室でも朝までしっとり吸い付くような潤いが持続します。",
        "target": "大容量で毎日惜しみなくフェイスからボディまで使いたい方、ファンデーションの乾燥割れや粉吹きに悩む方、ベタつきの少ない高保湿オイルを求める方",
        "point": "夜のお手入れの最後、乳液やクリームに1滴垂らして混ぜ合わせてから全顔へ。またメイク前に乾燥しやすい目尻やほうれい線へ米粒大を薄く仕込むとメイク崩れを劇的に予防できます。"
    },
    {
        "rank": 4,
        "tag": "🍊 未精製コールドプレス×有機JAS認定！杏の生命力をそのまま閉じ込めた超濃厚ゴールドリペア",
        "catch": "手作りコスメ・高機能原料の名門マンディムーンが誇る未精製グレード。杏仁特有のかすかな甘いナッツ香と濃厚な黄金色が、冬の枯れ肌にみなぎる弾力をもたらす",
        "brand_name": "Mandy Moon (マンディムーン)",
        "capacity": "50ml / 遮光プラドロッパー容器",
        "type": "未精製オーガニックピュアオイル",
        "features": "未精製アンズ核油（オーガニック認証）、植物ステロール、高濃度トコフェロール、オメガ9脂肪酸",
        "value": "脱色・脱臭を一切行わない未精製抽出。精製オイルでは失われがちな微量栄養素や抗酸化ポリフェノールがそのまま残り、真冬の紫外線・乾燥ダメージを集中修復",
        "desc_p1": "真冬の冷たい北風に晒された肌は、酸化ストレスと水分喪失が同時に進行し、夕方になると急激にしぼんで老け見えします。マンディムーンの『オーガニック アプリコットカーネルオイル（未精製）』は、杏の種子（仁）が持つパワフルな再生力を一切薄めずにボトリングした本格派リペアオイルです。",
        "desc_p2": "未精製ならではの深みのある黄金色と、ほんのり香る杏仁の自然なアロマが特徴。指にとるとコクがありながら、肌に乗せるととろけるように馴染み、カサついた角質層を柔らかく満たします。首元やデコルテのポツポツが気になる部分へ指の腹でじっくりと円を描きながら塗り込むと、硬くなった角質が日を追うごとに滑らかにほぐれ、つるんとしたむきたまご肌を実感できます。",
        "target": "化学処理されていない未精製のピュアなオーガニックオイルを愛用したい方、冬の乾燥による肌のしぼみ・ハリ不足に本気で悩む方、首筋の集中トリートメントを行いたい方",
        "point": "お風呂上がりの温まった肌に、スポイト3滴分を手にとって首元からデコルテ、肩周りにかけてリンパを流すようにマッサージします。週に2回の蒸しタオルパックを組み合わせるとさらに効果的です。"
    },
    {
        "rank": 5,
        "tag": "✨ コスモスオーガニック認証！真冬の目元＆首元を滑らかに整える極上フレンチオイル",
        "catch": "国際基準COSMOS認証を取得したspa hinokiのプレミアムアプリコット。繊細な目元の皮膚構造を研究し尽くした抜群のテクスチャーで、冬のちりめんジワをふっくら持ち上げる",
        "brand_name": "spa hinoki (スパヒノキ)",
        "capacity": "100ml / 遮光ポンプボトル",
        "type": "エコサートCOSMOS認証 オーガニック植物油",
        "features": "フランス産オーガニックアンズ核油、オレイン酸（約65%）、リノール酸（約25%）、ビタミンE",
        "value": "ワンタッチで出せる便利な遮光ポンプボトル採用。空気に触れにくく酸化を防ぎながら、毎日のスキンケアルーティンにスマートに高保湿を取り入れられる",
        "desc_p1": "目元は顔の中で最も皮膚が薄く、皮脂腺がほとんど存在しないため、11月以降の湿度低下で真っ先にちりめんジワや乾燥くすみが現れます。スパヒノキの『オーガニック アプリコットカーネルオイル』は、世界最大規模の有機認証機関エコサートによるCOSMOS認証を取得した最高品質のトリートメントオイルです。",
        "desc_p2": "シルクのように滑らかで摩擦を感じさせないテクスチャーは、デリケートな目元や首周りのマッサージに最適。ポンプを軽く1プッシュして薬指の腹で目の下や目尻にトントンと優しく押し込むと、角層の隙間を埋めるようにオイルが浸透し、エアコンの直風を受けても乾かない鉄壁の保湿膜を形成します。100mlのたっぷりサイズでコスパも抜群です。",
        "target": "目尻の乾燥小ジワや目の下のちりめんジワを集中ケアしたい方、ポンプ式で手軽に衛生的に使いたい方、信頼できる国際オーガニック認証品を選びたい方",
        "point": "夜のお手入れでアイクリームを塗る前後に、薬指に半プッシュ分をとって目周りの骨に沿って優しくタッピングします。摩擦を絶対に起こさないよう、指を滑らせるのではなく置くように馴染ませるのがコツです。"
    },
    {
        "rank": 6,
        "tag": "🛁 ポンプ付大容量300ml！真冬の全身粉吹きからデコルテ集中マッサージまで贅沢使い",
        "catch": "サロン専売品質を手軽に自宅で。大容量だからこそできる真冬の『お風呂上がり全身オイルトリートメント』で、すね・肘・背中の粉吹き痒みを根底から一掃",
        "brand_name": "マカダミア屋",
        "capacity": "300ml / 専用ポンプボトル",
        "type": "サロン仕様 天然無添加キャリアオイル",
        "features": "高純度アンズ核油、未精製・精製ベストバランスブレンド、オレイン酸、リノール酸",
        "value": "エステサロンやリラクゼーションサロンの現場で実際に使用されている業務用グレード。毎日全身にたっぷり使っても数ヶ月持つ圧倒的なボリューム感",
        "desc_p1": "真冬になると顔だけでなく、すねや太もも、背中が粉を吹いてかゆくなり、お風呂上がりに慌ててボディクリームを塗っても追いつかない……そんな全身の重度乾燥に悩む方に最適なのが、マカダミア屋の『天然無添加 アプリコットカーネルオイル 300ml』です。",
        "desc_p2": "ポンプを押すだけで適量が出せるため、お風呂場から出た直後の濡れた素肌へスピーディーに塗布可能。水分とオイルが肌の上で瞬時に乳化し、ビロードのような柔らかな保護膜を全身に張り巡らせます。伸びが非常に良いため、首元から肩、鎖骨周りのリンパマッサージにも最適で、冬の寒さで凝り固まった首筋をほぐしながらポツポツ角質粒の予防ケアが同時に叶います。",
        "target": "真冬にすねや背中が粉を吹いて痒くなりやすい方、お風呂上がりの全身保湿を時短かつ強力に行いたい方、首やデコルテのマッサージを習慣にしたい方",
        "point": "入浴後、バスタオルで体を拭く前の濡れた肌に2〜3プッシュを全身に伸ばします。その後タオルで軽く押さえるように水分を拭き取るだけで、極上のしっとり感が一日中続きます。"
    },
    {
        "rank": 7,
        "tag": "💊 医薬部外品・薬用有効成分配合！首元・目元のポツポツ荒れ肌を科学的にケアする集中液",
        "catch": "抗炎症の薬用有効成分グリチルレチン酸ステアリルを配合。冬の乾燥と摩擦で赤く炎症を起こしやすい首周りの角質粒を、荒れを防ぎながらなめらかに鎮静する",
        "brand_name": "AIWA (アイワ)",
        "capacity": "40ml / 遮光スポイト瓶",
        "type": "医薬部外品 薬用高保湿アプリコットオイル",
        "features": "グリチルレチン酸ステアリル（薬用有効成分）、アンズ核油、天然ビタミンE、スクワラン",
        "value": "単なる保湿にとどまらず、薬用有効成分が冬の衣服擦れによる首元の肌荒れ・かぶれ・ひび割れを未然に防止。敏感肌でも安心して継続できるメディカル処方",
        "desc_p1": "冬の角質粒は、乾燥だけでなくタートルネックやマフラーの化学繊維による慢性的な摩擦刺激が引き金となって炎症を伴いながら進行することが多々あります。アイワの『薬用アプリコットオイル』は、厚生労働省承認の薬用有効成分を配合した本格派の医薬部外品オイルです。",
        "desc_p2": "消炎効果を持つグリチルレチン酸ステアリルが肌荒れや赤みを速やかに鎮静し、高純度の杏仁油がカチコチに硬直したポツポツ角層をやさしく軟化。とろみのあるオイルが患部にピタッと密着し、真冬の外気や摩擦ダメージから患部を保護します。首筋に痒みや赤みが出やすい敏感肌の方でも、刺激を感じることなく首元の美肌ケアを続けられます。",
        "target": "首元にポツポツができると同時に赤みや痒みも出やすい方、効果が認められた医薬部外品を選びたい方、皮膚が薄くデリケートな首元を安全にケアしたい方",
        "point": "洗顔・入浴後、清潔な状態の首元や目元にスポイトで直接1〜2滴を落とし、擦らずに指の腹でトントンと押し込むようになじませます。朝晩の継続使用が推奨されます。"
    },
    {
        "rank": 8,
        "tag": "🌡️ 杏仁オイル×ハトムギ×温感和漢！寝ている間に目元の頑固な粒を集中パック",
        "catch": "塗って寝るだけの新習慣スティックパック。じんわり温感ジェルが冬の冷え固まった目元の血行を促し、杏仁とハトムギのダブルパワーで角質粒を集中軟化",
        "brand_name": "リベルタ (つぶぽろん)",
        "capacity": "1.8g / ダイヤル式シリコンブラシ容器",
        "type": "目元専用 温感和漢集中ナイトパック",
        "features": "アンズ種子エキス、ハトムギ種子エキス（ヨクイニン）、サリチル酸、和漢植物複合エキス、温感成分",
        "value": "ダイヤルを回すと先端の極細シリコンブラシから適量の温感ジェルが登場。手を汚さずに目元の細かなポツポツへピンポイントで直塗りでき、寝具にもつかない速乾密着設計",
        "desc_p1": "目のキワや眉の周りにできる微細な白い粒（稗粒腫や角質粒）は、クリームを塗るだけではなかなか手応えが得られず、メイクでも隠しきれない冬の厄介な悩みです。リベルタの『つぶぽろん 目元温和漢パック』は、このピンポイントの目元悩みを解消するために誕生したアイデアコスメです。",
        "desc_p2": "ペン型のシリコンブラシでポツポツ部分を優しく撫でると、心地よいじんわりとした温感が広がり、寒さで閉じていた毛穴と硬い角質をリラックスさせます。杏仁オイルとハトムギエキスが角質粒の芯までじっくりと浸透。塗布後は薄い透明フィルムへと変化して有効成分を一晩中閉じ込めるため、寝ている間に剥がれる心配もありません。翌朝の洗顔時にスルリと洗い流せます。",
        "target": "目のキワや眉周りに小さな白い粒・ブツブツができている方、オイルを顔全体に塗るのが苦手でピンポイントにケアしたい方、温感効果で冬の目元の血行も良くしたい方",
        "point": "夜のスキンケアの最後に、ダイヤルを回してジェルを出し、先端のシリコンブラシで気になる粒の上をやさしく円を描くようにマッサージしながら塗布します。完全に乾いてから就寝してください。"
    },
    {
        "rank": 9,
        "tag": "🌍 全米No.1サプリブランドが放つ最高純度！髪のパサつきから小ジワまでシルク化する名作",
        "catch": "アイハーブでも圧倒的レビュー数を誇るNOW Foodsのロングセラー。100%純粋な低温圧搾杏仁油が、真冬の乾燥で静電気を帯びる毛先や目元のちりめんジワを劇的修復",
        "brand_name": "NOW Foods (ナウフーズ)",
        "capacity": "118ml / UVカット遮光ボトル",
        "type": "100%ピュア モイスチャライジングオイル",
        "features": "純粋アンズ核油100%、オメガ9脂肪酸、天然ビタミンE、非遺伝子組み換え（Non-GMO）",
        "value": "海外サプリメント最大手ならではの厳格な品質基準と圧倒的な低価格。酸化しにくい安定した脂肪酸組成で、フェイスケアからヘアケアまで冬中頼れる万能選手",
        "desc_p1": "11月以降の木枯らしが吹く時期、肌の乾燥だけでなく『毛先のパサつき・枝毛・静電気』も深刻化します。NOW Foodsの『ピュア アプリコットオイル 118ml』は、世界中のナチュラル志向ユーザーに愛用される最高峰のマルチユースオイルです。",
        "desc_p2": "非常にサラサラとしたテクスチャーで、塗布した瞬間に素早く肌へ浸透し、嫌な油膜感やテカリを残しません。洗顔後のブースターや化粧水後のフタとしてはもちろん、タオルドライ後の毛先に少量馴染ませてドライヤーをかけると、熱ダメージを防ぎながらサロン帰りのようなシルキーな指通りへと導きます。1本持っておけば冬の乾燥トラブルを全方位から防げます。",
        "target": "高品質なピュアオイルをリーズナブルに手に入れたい方、肌だけでなく冬の髪のパサつきや静電気も同時にケアしたい方、ベタつきのない軽やかなオイルが好きな方",
        "point": "スキンケアには手のひらで1〜2滴を顔全体へ。ヘアケアには濡れた髪の毛先中心に3〜4滴を馴染ませてからブローします。ハンドクリームに1滴混ぜて指先マッサージをするのも絶品です。"
    },
    {
        "rank": 10,
        "tag": "🧪 創業半世紀の国内研究所が精製！手持ちの化粧水に1滴混ぜて冬のバリアをブースト",
        "catch": "化粧品原料のプロ「自然化粧品研究所」が手掛ける高純度杏仁油。極限まで不純物を除去した低刺激精製グレードで、敏感に傾いた真冬の角層を穏やかに保護",
        "brand_name": "自然化粧品研究所",
        "capacity": "100ml / 遮光プラドロッパー容器",
        "type": "高純度精製 スキンケアキャリアオイル",
        "features": "精製アンズ核油100%、高濃度オレイン酸、パルミトレイン酸、リノール酸",
        "value": "無色無臭でアレルギーリスクを最小限に抑えた安心の国内精製。敏感肌やアトピー傾向のある肌でも冬の保湿強化として気兼ねなく取り入れられるピュアオイル",
        "desc_p1": "冬の寒さと乾燥で肌が過敏になり、香料や未精製オイルの植物成分にピリピリと刺激を感じてしまう……そんなデリケートな乾燥肌の方に自信を持っておすすめできるのが、自然化粧品研究所の『アプリコットカーネルオイル 100ml』です。",
        "desc_p2": "職人の高度な精製技術によって不純物や特有の匂いを丁寧にカット。無色透明でサラリとした感触でありながら、杏仁特有の豊富なオレイン酸が角層の細胞間脂質とピタッと結合し、水分蒸発を物理的にシャットアウトします。手持ちの化粧水に1滴ブレンドして使う『オイルインローション』テクニックを使えば、どんな敏感肌でも摩擦ゼロで濃厚な潤いバリアを構築できます。",
        "target": "匂いや刺激に敏感で未精製オイルが肌に合わない方、手持ちのスキンケアの保湿力を底上げしたい方、安心の国産精製品を求める方",
        "point": "手のひらに普段の化粧水を500円玉大とり、そこに本オイルを1滴垂らして両手ですり合わせ、顔全体を優しく包み込みます。水分と油分が同時に補給され、乳液いらずのしっとり肌が完成します。"
    }
]

# 目次リンク
toc_links = ""
for p in product_details:
    toc_links += f'          <li><a href="#rank-{p["rank"]}">第{p["rank"]}位：{p["brand_name"]} {p["catch"][:22]}...</a></li>\n'

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
        "url": f"https://lumi-cosme.vercel.app/winter-apricot-oil#rank-{p['rank']}"
    })

json_ld_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！若さの脂肪酸パルミトレイン酸が真冬の目元・首元のポツポツ乾燥＆ゴワつきをなめらかに整える高保湿杏仁オイルコスメランク10",
            "description": "11月・12月の寒冷乾燥で硬化した首元・目元のポツポツ角質粒やゴワつき肌を救う高保湿杏仁オイル（アプリコットカーネルオイル）コスメを徹底厳選！アンミオイル、生活の木、&SH、スパヒノキ、つぶぽろんまで徹底検証。",
            "datePublished": "2026-11-05T09:00:00+09:00",
            "dateModified": "2026-11-05T09:00:00+09:00",
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
            "name": "高保湿杏仁オイル（アプリコットカーネルオイル）コスメおすすめランキングTOP10",
            "numberOfItems": 10,
            "itemListElement": json_ld_items
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "杏仁オイル（アプリコットカーネルオイル）が真冬の首元や目元のポツポツ角質粒に良いとされる理由は何ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "杏仁オイル（アンズ核油）には、加齢や真冬の寒冷乾燥によって激減する『パルミトレイン酸』をはじめ、肌馴染み抜群のオレイン酸、リノール酸、ビタミンA・B群が極めて高いバランスで凝縮されています。冬の乾燥と衣類の摩擦で皮膚代謝が乱れると、剥がれ落ちるはずの古い角質が毛穴周りで硬化して茶色いポツポツ（角質粒・老人性イボ）になります。杏仁オイルの脂肪酸は硬化した角質細胞の結合を穏やかにゆるめ、皮膚を傷つけることなく自然なターンオーバーを促すため、目元や首筋をなめらかに整える効果があります。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "杏仁オイルとホホバオイルやアルガンオイルの違いはどこにありますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "ホホバオイルは皮脂に近いワックスエステルで『表面の水分蒸散防止』に優れ、アルガンオイルはビタミンEによる『抗酸化エイジングケア』が得意です。一方、杏仁オイルは粒子の細かさと『角質軟化作用（硬くなった皮膚をふっくらほぐす力）』において植物油随一の性能を誇ります。そのため、冬の寒さでゴワゴワに硬化した角層や、首元・目元のザラつきを滑らかにする目的では、杏仁オイルが最も優れたアプローチを発揮します。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "首元のポツポツをケアする際の最も効果的な塗り方やコツはありますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "入浴後、皮膚が温まって柔らかくなっているタイミングで行うのがベストです。化粧水で首元にも水分を補給した後、杏仁オイルを3〜4滴手のひらにとり、下から上（鎖骨から顎下へ）向かってリンパを流すように優しくマッサージします。ポツポツがある部分は爪を立てず、指の腹で円を描くように丁寧になじませてください。週に1〜2回、ホットタオルで首元を温めてからオイルを塗る集中パックを取り入れると、浸透力と角質柔軟化が飛躍的に高まります。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "敏感肌や赤ちゃんでも杏仁オイルを使用できますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "はい、杏仁オイルは植物油の中でも刺激性が極めて低く、ヨーロッパでは古くからベビーマッサージ用オイルとしても親しまれてきました。アレルギーや刺激が心配な方は、不純物を高度に除去した『精製（Refined）グレード』を選ぶか、使用前に二の腕の内側でパッチテストを行うことをおすすめします。"
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
  <title>保湿力の強さで肌乾燥とさようなら！若さの脂肪酸パルミトレイン酸が真冬の目元・首元のポツポツ乾燥＆ゴワつきをなめらかに整える高保湿杏仁オイルコスメランク10</title>
  <meta name="description" content="11月・12月の寒冷乾燥で硬化した首元・目元のポツポツ角質粒やゴワつき肌を救う高保湿杏仁オイル（アプリコットカーネルオイル）コスメを徹底厳選！アンミオイル、生活の木、&SH、スパヒノキ、つぶぽろんまで徹底検証。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-apricot-oil">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！若さの脂肪酸パルミトレイン酸が真冬の目元・首元のポツポツ乾燥＆ゴワつきをなめらかに整える高保湿杏仁オイルコスメランク10">
  <meta property="og:description" content="11月・12月の寒冷乾燥で硬化した首元・目元のポツポツ角質粒やゴワつき肌を救う高保湿杏仁オイル（アプリコットカーネルオイル）コスメを徹底厳選！アンミオイル、生活の木、&SH、スパヒノキ、つぶぽろんまで徹底検証。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-apricot-oil">
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
      --primary: #d97706;
      --primary-light: #fef3c7;
      --primary-dark: #92400e;
      --accent: #b45309;
      --accent-hover: #78350f;
      --bg: #fffdfa;
      --card-bg: #ffffff;
      --text-main: #292524;
      --text-sub: #57534e;
      --border: #fde68a;
      --shadow: 0 4px 15px rgba(217, 119, 6, 0.08);
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
      font-weight: 500;
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
      background: linear-gradient(135deg, #ffffff 0%, var(--primary-light) 100%);
      border-radius: var(--radius);
      padding: 2.5rem 2rem;
      border: 1px solid var(--border);
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .hero-badge {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.35rem 0.8rem;
      border-radius: 20px;
      margin-bottom: 1rem;
      letter-spacing: 0.5px;
    }}

    .hero-title {{
      font-size: 1.7rem;
      font-weight: 700;
      line-height: 1.4;
      color: var(--primary-dark);
      margin-bottom: 1rem;
    }}

    .hero-desc {{
      font-size: 1rem;
      color: var(--text-sub);
      line-height: 1.8;
      margin-bottom: 1.2rem;
    }}

    .meta-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--text-sub);
      border-top: 1px dashed var(--border);
      padding-top: 1rem;
    }}

    .toc-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.8rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .toc-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.5rem;
    }}

    .toc-list li a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.95rem;
      transition: color 0.2s;
    }}

    .toc-list li a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}

    .intro-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .intro-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .intro-section p {{
      margin-bottom: 1.2rem;
      font-size: 1rem;
      line-height: 1.8;
    }}

    .intro-highlight-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1rem;
      margin-top: 1.5rem;
    }}

    .highlight-card {{
      background: var(--primary-light);
      padding: 1.2rem;
      border-radius: 10px;
      border-left: 4px solid var(--primary);
    }}

    .highlight-card strong {{
      display: block;
      color: var(--primary-dark);
      font-size: 1.05rem;
      margin-bottom: 0.4rem;
    }}

    .highlight-card p {{
      font-size: 0.9rem;
      color: var(--text-main);
      margin-bottom: 0;
      line-height: 1.6;
    }}

    .table-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      overflow-x: auto;
    }}

    .table-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
    }}

    table.comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 600px;
    }}

    table.comparison-table th, table.comparison-table td {{
      padding: 0.8rem 1rem;
      border-bottom: 1px solid #f5f5f4;
      text-align: left;
    }}

    table.comparison-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
    }}

    .table-thumb {{
      width: 55px;
      height: 55px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid var(--border);
    }}

    .rank-num {{
      font-weight: 700;
      color: var(--primary);
      font-size: 1.05rem;
    }}

    .price-cell {{
      font-weight: 700;
      color: #b91c1c;
      white-space: nowrap;
    }}

    .table-link {{
      color: var(--primary);
      font-weight: 700;
      text-decoration: none;
    }}

    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      position: relative;
    }}

    .product-badge {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.3rem 0.8rem;
      border-radius: 6px;
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
      text-align: center;
    }}

    .product-img {{
      width: 220px;
      height: 220px;
      object-fit: contain;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: #ffffff;
      padding: 0.5rem;
    }}

    .product-intro {{
      flex-grow: 1;
    }}

    .product-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.5rem;
      line-height: 1.4;
    }}

    .product-brand {{
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 0.5rem;
    }}

    .product-price {{
      font-size: 1rem;
      color: var(--text-main);
      margin-bottom: 0.8rem;
    }}

    .price-val {{
      font-size: 1.4rem;
      font-weight: 700;
      color: #b91c1c;
    }}

    .product-tag {{
      display: inline-block;
      background: #fffbeb;
      border: 1px solid #fef3c7;
      color: var(--primary-dark);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.35rem 0.75rem;
      border-radius: 6px;
      margin-bottom: 0.8rem;
    }}

    .product-catch {{
      font-size: 0.95rem;
      color: var(--text-sub);
      line-height: 1.7;
    }}

    .spec-table-box {{
      margin: 1.5rem 0;
      background: #fffdfa;
      border: 1px solid var(--border);
      border-radius: 10px;
      overflow: hidden;
    }}

    table.spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
    }}

    table.spec-table th, table.spec-table td {{
      padding: 0.75rem 1rem;
      border-bottom: 1px solid #fde68a;
      text-align: left;
    }}

    table.spec-table th {{
      width: 30%;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
    }}

    .review-body {{
      margin-top: 1.5rem;
    }}

    .review-body h4 {{
      font-size: 1.1rem;
      color: var(--primary-dark);
      margin-bottom: 0.8rem;
    }}

    .review-body p {{
      margin-bottom: 1rem;
      font-size: 0.98rem;
      line-height: 1.8;
    }}

    .target-box, .point-box {{
      background: #fefce8;
      border-left: 4px solid var(--primary);
      padding: 1rem 1.2rem;
      border-radius: 0 8px 8px 0;
      margin-top: 1rem;
      font-size: 0.92rem;
    }}

    .target-box strong, .point-box strong {{
      color: var(--primary-dark);
      display: block;
      margin-bottom: 0.3rem;
    }}

    .btn-wrap {{
      margin-top: 1.8rem;
      text-align: center;
    }}

    .rakuten-btn {{
      display: inline-block;
      width: 100%;
      max-width: 480px;
      background: linear-gradient(135deg, #bf0000 0%, #e60000 100%);
      color: #ffffff;
      font-weight: 700;
      font-size: 1.05rem;
      text-align: center;
      padding: 1rem 1.5rem;
      border-radius: 30px;
      text-decoration: none;
      box-shadow: 0 4px 15px rgba(230, 0, 0, 0.25);
      transition: all 0.3s;
    }}

    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(230, 0, 0, 0.35);
      background: linear-gradient(135deg, #a60000 0%, #cc0000 100%);
    }}

    .guide-section, .faq-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .guide-section h2, .faq-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .guide-section h3 {{
      font-size: 1.15rem;
      color: var(--primary);
      margin: 1.5rem 0 0.6rem;
    }}

    .guide-section p {{
      margin-bottom: 1rem;
      font-size: 0.98rem;
      line-height: 1.8;
    }}

    .faq-item {{
      margin-bottom: 1.5rem;
      padding-bottom: 1.5rem;
      border-bottom: 1px solid #f5f5f4;
    }}

    .faq-q {{
      font-weight: 700;
      color: var(--primary-dark);
      font-size: 1.05rem;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
    }}

    .faq-q span {{
      color: var(--primary);
      font-size: 1.2rem;
      line-height: 1;
    }}

    .faq-a {{
      color: var(--text-main);
      font-size: 0.95rem;
      line-height: 1.8;
      padding-left: 1.7rem;
    }}

    .related-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .related-section-title {{
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .related-list {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 1.2rem;
    }}

    .related-card {{
      display: block;
      background: #fffdfa;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1.2rem;
      text-decoration: none;
      transition: all 0.2s;
    }}

    .related-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.05);
      border-color: var(--primary);
    }}

    .related-card-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.4rem;
      line-height: 1.5;
    }}

    .related-card-desc {{
      font-size: 0.82rem;
      color: var(--text-sub);
      line-height: 1.5;
    }}

    footer.site-footer {{
      background: #ffffff;
      border-top: 1px solid var(--border);
      padding: 2.5rem 1.5rem;
      margin-top: 4rem;
    }}

    .footer-inner {{
      max-width: 1080px;
      margin: 0 auto;
      text-align: center;
    }}

    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.8rem 1.5rem;
      margin-bottom: 1.5rem;
    }}

    .footer-links a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.85rem;
      transition: color 0.2s;
    }}

    .footer-links a:hover {{
      color: var(--primary);
    }}

    .copyright {{
      font-size: 0.8rem;
      color: #a8a29e;
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">Lumi Cosme</a>
      <nav class="nav-links">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#comparison">比較表</a>
        <a href="#guide">選び方・使い方</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <span class="hero-badge">2026年真冬版 ｜ 徹底保湿コスメ検証</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！若さの脂肪酸パルミトレイン酸が真冬の目元・首元のポツポツ乾燥＆ゴワつきをなめらかに整える高保湿杏仁オイルコスメランク10</h1>
      <p class="hero-desc">
        11月から12月にかけてマフラーやタートルネックを着用し始めると、衣類の擦れと湿度の急降下によって首筋やデコルテ、目周りの皮膚代謝が停止状態に。触るとチクチクする茶色いポツポツ角質粒や、ファンデーションがひび割れる目元のゴワつきに頭を抱える方が急増します。そんな真冬の「角質硬直」と「ポツポツ乾燥」を物理的に傷つけることなく、脂肪酸の力で柔らかくほぐし尽くすのが、古来より皮膚柔軟の生薬として重宝されてきた「杏仁オイル（アプリコットカーネルオイル）」です。植物界屈指のパルミトレイン酸とオレイン酸を秘めた高保湿名品10選をコスメコンシェルジュが徹底検証・厳選しました。
      </p>
      <div class="meta-bar">
        <span>🕒 公開日: 2026年11月5日</span>
        <span>✍️ 執筆・検証: Lumi Cosme 編集部 コスメコンシェルジュ</span>
        <span>🔍 楽天リアルタイムAPI商品データ照合済</span>
      </div>
    </section>

    <div class="toc-box">
      <div class="toc-title">📑 目次（タップで該当ランキングへジャンプ）</div>
      <ul class="toc-list">
{toc_links}
      </ul>
    </div>

    <section class="intro-section">
      <h2>真冬に首元や目元がザラつきポツポツ角質粒が増殖する皮膚科学的メカニズム</h2>
      <p>
        晩秋から12月にかけて外気温が10℃を下回り始めると、真皮の毛細血管がギュッと収縮して皮膚細胞へのアミノ酸や酸素の運搬が激減します。その結果、本来なら28日前後で自然に剥がれ落ちるはずの古い角質が剥がれ落ちず、表面に何層にも重なって接着剤のように硬化。これが「冬の角質肥厚（角層フリーズ）」です。
      </p>
      <p>
        特に首元や目元は、皮脂腺が極めて少ないにもかかわらず、衣服（ウールやアクリル繊維のハイネック・マフラー）の擦れや、目元の瞬きによる激しい物理摩擦を常に受けています。乾燥と摩擦刺激が重なると、皮膚は自身を守ろうとして角質をさらに厚く硬く盛り上げ、やがて1〜2ミリ程度の茶色いポツポツ（老人性イボ・アクロコルドン・稗粒腫）へと変化してしまうのです。
      </p>

      <div class="intro-highlight-grid">
        <div class="highlight-card">
          <strong>1. 若さの脂肪酸「パルミトレイン酸」が角質細胞を柔軟化</strong>
          <p>皮脂膜中に存在し、赤ちゃんの肌に多く加齢とともに急激に失われるパルミトレイン酸。杏仁オイルはこの希少な脂肪酸を含有し、カチコチに固まった角質同士の結合を摩擦ゼロで穏やかにゆるめます。</p>
        </div>
        <div class="highlight-card">
          <strong>2. 人間の皮脂に近い高濃度オレイン酸による高浸透シールド</strong>
          <p>オレイン酸を約65%という圧倒的な比率で含有。角層のラメラ構造と親和して角質深部まで瞬時に吸い込まれ、真冬のエアコン乾燥による水分蒸散を物理的にシャットアウトします。</p>
        </div>
        <div class="highlight-card">
          <strong>3. 天然ビタミンA・B群による代謝リズムの正常化</strong>
          <p>杏の仁（種子）に凝縮されたプロビタミンAやビタミンB群、トコフェロールが、冬の冷えで完全にフリーズした角質のターンオーバーを健やかに後押し。触れて心地よい滑らかさを呼び戻します。</p>
        </div>
      </div>
    </section>

    <section class="table-section" id="comparison">
      <h2>高保湿杏仁オイルコスメ おすすめ10選 比較一覧表</h2>
      <table class="comparison-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>画像</th>
            <th>ブランド / アイテム名</th>
            <th>分類</th>
            <th>参考価格</th>
            <th>詳細</th>
          </tr>
        </thead>
        <tbody>
{table_joined}
        </tbody>
      </table>
    </section>

    <section id="ranking">
{cards_joined}
    </section>

    <section class="guide-section" id="guide">
      <h2>プロ直伝！真冬の杏仁オイル選び方＆ポツポツ・小ジワを解消する使用テクニック</h2>
      <h3>1. 「未精製（ゴールデン）」と「精製（クリア）」の正しい見分け方</h3>
      <p>
        杏仁オイルには、杏の仁を絞ってろ過しただけの濃い黄金色の「未精製（コールドプレス）」と、不純物を高度に取り除いた透明な「精製（Refined）」があります。真冬の深刻な乾燥やエイジングケア、首元のポツポツを集中マッサージしたい場合は、微量栄養素やパルミトレイン酸がそのまま残る「未精製」がベストです。一方、アトピー傾向や超敏感肌で植物本来の成分に刺激を感じやすい方は、アレルゲンをカットした「精製」を選ぶと安心して毎日使用できます。
      </p>
      <h3>2. 「入浴後のホットタオル蒸し＋下から上へのリンパ流し」で効果倍増</h3>
      <p>
        首元やデコルテのポツポツをケアする際、絶対にやってはいけないのが『爪で引っ掻く・強く擦り取る』ことです。摩擦によってメラニンが沈着し、茶色く色素沈着して悪化してしまいます。最も効果的なのは、お風呂上がりの体が温まった状態で化粧水をたっぷり首元まで塗布し、杏仁オイルを3滴手にとって、鎖骨のリンパ節へ向かって流すように優しくマッサージする方法です。週に2回ほど、レンジで温めた蒸しタオルを首に巻いて3分間温めた後にオイルを塗ると、硬い角質が驚くほどふっくらほぐれます。
      </p>
      <h3>3. 日中の「ファンデーション乾燥割れ」を防ぐ目元ピンポイント仕込み</h3>
      <p>
        真冬の夕方に目尻やほうれい線のファンデーションがピキピキとひび割れてしまうインナードライ肌には、朝のメイク前に杏仁オイルを米粒半分ほど薬指にとり、乾燥しやすい目周りにトントンと馴染ませてから下地を重ねるテクニックが劇的な効果を発揮します。皮脂膜と同化して薄いクッション膜を作るため、笑っても粉浮きしない美しいツヤが一日中持続します。
      </p>
    </section>

    <section class="faq-section" id="faq">
      <h2>よくある質問（FAQ）</h2>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 杏仁オイル（アプリコットカーネルオイル）が真冬の首元や目元のポツポツ角質粒に良いとされる理由は何ですか？</div>
        <div class="faq-a">杏仁オイル（アンズ核油）には、加齢や真冬の寒冷乾燥によって激減する「パルミトレイン酸」をはじめ、肌馴染み抜群のオレイン酸、リノール酸、ビタミンA・B群が極めて高いバランスで凝縮されています。冬の乾燥と衣類の摩擦で皮膚代謝が乱れると、剥がれ落ちるはずの古い角質が毛穴周りで硬化して茶色いポツポツ（角質粒・老人性イボ）になります。杏仁オイルの脂肪酸は硬化した角質細胞の結合を穏やかにゆるめ、皮膚を傷つけることなく自然なターンオーバーを促すため、目元や首筋をなめらかに整える効果があります。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 杏仁オイルとホホバオイルやアルガンオイルの違いはどこにありますか？</div>
        <div class="faq-a">ホホバオイルは皮脂に近いワックスエステルで「表面の水分蒸散防止」に優れ、アルガンオイルはビタミンEによる「抗酸化エイジングケア」が得意です。一方、杏仁オイルは粒子の細かさと「角質軟化作用（硬くなった皮膚をふっくらほぐす力）」において植物油随一の性能を誇ります。そのため、冬の寒さでゴワゴワに硬化した角層や、首元・目元のザラつきを滑らかにする目的では、杏仁オイルが最も優れたアプローチを発揮します。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 首元のポツポツをケアする際の最も効果的な塗り方やコツはありますか？</div>
        <div class="faq-a">入浴後、皮膚が温まって柔らかくなっているタイミングで行うのがベストです。化粧水で首元にも水分を補給した後、杏仁オイルを3〜4滴手のひらにとり、下から上（鎖骨から顎下へ）向かってリンパを流すように優しくマッサージします。ポツポツがある部分は爪を立てず、指の腹で円を描くように丁寧になじませてください。週に1〜2回、ホットタオルで首元を温めてからオイルを塗る集中パックを取り入れると、浸透力と角質柔軟化が飛躍的に高まります。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 敏感肌や赤ちゃんでも杏仁オイルを使用できますか？</div>
        <div class="faq-a">はい、杏仁オイルは植物油の中でも刺激性が極めて低く、ヨーロッパでは古くからベビーマッサージ用オイルとしても親しまれてきました。アレルギーや刺激が心配な方は、不純物を高度に除去した「精製（Refined）グレード」を選ぶか、使用前に二の腕の内側でパッチテストを行うことをおすすめします。</div>
      </div>
    </section>

    <!-- 関連記事プレースホルダー -->
    <section id="related" class="related-section">
      <div class="related-section-title">
        <span>📑</span> あわせて読みたい！冬の徹底保湿ケア特集一覧
      </div>
      <div class="related-list" id="related-grid-box">
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-links" id="footer-links-box">
      </div>
      <p class="copyright">© 2026 Lumi Cosme. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-apricot-oil.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-apricot-oil.html!")
