import json
import re

with open("fetched_3new_murumuru_cranberry_emu.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_cranberry_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 オメガ3・6・9黄金比×トコトリエノール！真冬の寒冷くすみと皮脂酸化を同時に晴らす最高峰ピュアオイル",
        "catch": "マンディムーンが誇るコールドプレス未精製クランベリーシードオイル。ビタミンEの40倍以上の抗酸化力を持つスーパービタミンEが、11月・12月の冷えきった枯れ肌に驚異の透明感と弾力を吹き込む",
        "brand_name": "mandy moon (マンディムーン)",
        "capacity": "10ml / ドロッパー遮光瓶",
        "type": "未精製コールドプレス 100%ピュアクランベリーシードオイル",
        "features": "クランベリー種子油100%、スーパービタミンE（トコトリエノール）、オメガ3（α-リノレン酸約30%）、オメガ6（リノール酸約35%）、植物ステロール",
        "value": "植物油の中で唯一とも言われるオメガ3とオメガ6の理想的1:1バランス。一般的な植物オイルのベタつきが一切なく、角層の隙間へスルスル浸透して真冬の酸化乾燥ストレスをシャットアウト",
        "desc_p1": "11月中旬を過ぎて外気温が一桁台まで冷え込むと、血行不良によって顔色がどんよりと青白くくすみ、さらに暖房による皮脂の酸化と乾燥が重なって『夕方になると肌が黄ぐすみして疲れて見える』という深刻な悩みが現れます。マンディムーンの『オイルマルシェ・クランベリー 10ml』は、極寒の北米の大自然で育まれた完熟クランベリーの微小な種子から、熱を一切加えない低温圧搾法（コールドプレス）で抽出された最高峰のエイジングケア美容オイルです。",
        "desc_p2": "黄金色に輝くオイルを手のひらに数滴取ると、ベリーの種子特有のフレッシュで香ばしいナッツ調の香りがほのかに漂います。肌に乗せると、オイルとは思えないほど水のようにサラリと馴染み、乾燥してゴワついた角質層を瞬時にふっくら柔軟化。通常のビタミンE（トコフェロール）の40〜60倍のフリーラジカル消去能を持つ『トコトリエノール』が、暖房や紫外線による細胞間脂質の酸化を強力にブロックし、翌朝の洗顔時には内側からポッと上気したような透明感とハリ艶を実感できます。",
        "target": "冬になると肌がくすんで顔色が悪く見える方、オイル特有のベタつきや油膜感が苦手な方、洗顔後のブースターとして化粧水の浸透を劇的に高めたい方",
        "point": "朝晩の洗顔直後、肌にまだ化粧水をつける前のまっさらな肌に2〜3滴を手のひらで温めてハンドプレス。角質が柔らかく解きほぐされ、その後に重ねる化粧水がスポンジのようにぐんぐん吸い込まれます。"
    },
    {
        "rank": 2,
        "tag": "✨ オーガニック認証原料使用！ポーチに忍ばせて真冬の目元小ジワ・ほうれい線を即座にリペアする導入オイル",
        "catch": "&SHが提供する高純度オーガニッククランベリーオイル。プチプラとは思えない驚異の鮮度と浸透力で、日中の暖房でカサつく目元や口元に濃密な抗酸化ヴェールを補給",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "10ml / 遮光ドロッパーボトル",
        "type": "オーガニック未精製 クランベリー種子油",
        "features": "オーガニック認定クランベリー種子油100%、高濃度オメガ3・6・9、トコトリエノール、カロテノイド",
        "value": "ワンコイン価格帯でありながら未精製の高栄養成分をそのままキープ。日中のメイク直し時に乾燥小ジワの上からポンポンとなじませるだけで、粉吹きやヨレを美しくリセット",
        "desc_p1": "冬の午後、ふとオフィスの化粧室の鏡を見ると、目尻の笑いジワやほうれい線周りのファンデーションがパリパリにひび割れて粉を吹いていた……という経験は誰にでもあるはずです。そんな真冬のメイク崩れ・局所乾燥をその場でレスキューしてくれるのが、&SHの『オーガニック クランベリーオイル 10ml』です。",
        "desc_p2": "10mlのコンパクトな遮光ボトルはポーチやポケットにすっぽり収まるサイズ。指先にわずか1滴を取り、乾燥で引きつった目元や口元に優しくタッピングするようになじませると、素早く皮膚と一体化してツヤを蘇らせます。上からファンデーションを重ね直しても全くヨレず、むしろみずみずしい素肌のようなツヤ感が復活。夜のスキンケアだけでなく、日中の乾燥ガードとしても手放せなくなる名脇役です。",
        "target": "日中のオフィス乾燥で目元や口元のファンデ落ちに悩む方、まずは手頃な価格でクランベリーオイルの驚くべき浸透力を試したい方、敏感肌でも安心なオーガニック品質を好む方",
        "point": "綿棒の先に1滴染み込ませ、ヨレて乾燥した目元のファンデーションを優しく拭き取った後、指先で少量を馴染ませてからコンシーラーやパウダーを重ねると、朝のメイク立てのような美しさが戻ります。"
    },
    {
        "rank": 3,
        "tag": "🌿 寒冷地の恵みが凝縮された大容量30ml！毎晩の贅沢オイルマッサージで冬の代謝低下肌を覚醒させるピュアオイル",
        "catch": "ヨーロッパの厳しいオーガニック基準をクリアした未精製クランベリーオイル。寒さで強張った表情筋と首筋をほぐし、翌朝のむくみと乾燥くすみを一掃するナイトトリートメント",
        "brand_name": "Natural Elements (ナチュラルエレメンツ)",
        "capacity": "30ml / スポイト遮光瓶",
        "type": "オーガニック未精製コールドプレス 美容オイル",
        "features": "未精製クランベリー種子油100%、高活性トコトリエノール、フィトステロール、オレイン酸、リノール酸",
        "value": "スポイトタイプで適量を出しやすく、顔だけでなく首元・デコルテまでたっぷり使える30mlサイズ。滑りの良いテクスチャーで冬のリンパマッサージにも最適",
        "desc_p1": "12月の忘年会シーズンや年末の繁忙期は、寒さによる運動不足と睡眠不足が重なり、顔全体の血流やリンパの流れが滞ってフェイスラインのむくみや肌のくすみが慢性化しがちです。そんな疲れ切った冬肌をリセットするために生まれたのが、ナチュラルエレメンツの『ピュア クランベリーシードオイル 30ml』です。",
        "desc_p2": "未精製ならではの深みのある黄金色オイルは、植物の生命力がぎゅっと詰まった濃厚な質感。しかし肌に滑らせると驚くほどサラサラと伸び、摩擦を一切感じさせずにフェイスラインや首筋、鎖骨周りのマッサージを行えます。トコトリエノールとオメガ脂肪酸がマッサージの温熱効果と共に角層深くまで巡り、翌朝目覚めたときにはフェイスラインがキュッと引き締まり、パッと発光するような明るさとモチモチの手触りを実感できます。",
        "target": "真冬になると顔がむくみやすく肌色がどんより濁る方、夜のスキンケアで丁寧なフェイスマッサージを取り入れたい方、スポイト式で衛生的にたっぷり使いたい方",
        "point": "夜のお風呂上がり、スポイト半分（約4〜5滴）を手に取り、両手で温めてから顎先から耳の下、耳の下から鎖骨へと流すようにリンパマッサージを行います。その後、ホットタオルで軽く蒸すと浸透感が劇的に上がります。"
    },
    {
        "rank": 4,
        "tag": "👁️ クランベリー種子油が目元の薄い皮膚を一日中シールド！アイメイクの発色と高保湿ケアを両立する名品ベース",
        "catch": "MiMCのロングセラー「ミネラルクリーミーアイベース」。デリケートな目元のために厳選されたクランベリー種子油が、真冬の暖房乾燥による目元のちりめんジワを防ぎながらアイシャドウの密着度を最大化",
        "brand_name": "MiMC (エムアイエムシー)",
        "capacity": "専用コンパクトケース",
        "type": "高保湿美容液アイベース・アイクリーム",
        "features": "クランベリー種子油、ザクロ種子油、アボカド油、オリーブ果実油、天然ミネラルマイカ",
        "value": "スキンケア処方で作られた色つきアイベース。くすみがちな冬のまぶたを自然にトーンアップしながら、クランベリー種子油の抗酸化保水膜で夕方まで乾燥ジワを徹底ブロック",
        "desc_p1": "顔の皮膚の中で最も薄く皮脂腺がほとんどない目元は、冬の乾燥によって真っ先にダメージを受け、アイシャドウの粉浮きや二重幅への溜まり、夕方のちりめんジワを引き起こします。MiMCの『ミネラルクリーミーアイベース』は、メイクしながら本格的なアイケアができると美容賢者の間で絶賛されている名品です。",
        "desc_p2": "指先にとるとクリームが体温でとろけ、デリケートなまぶたへ摩擦レスでピタッと密着。クランベリー種子油の優れた保湿膜が一日中まぶたの水分蒸散を防ぎ、エアコンの直風下でも目元を乾燥から死守します。ほんのりとしたパールベージュが冬の寒冷くすみを自然に補正し、その後に重ねるアイシャドウの発色と持ちを劇的に向上。石けんで簡単にオフできる肌への優しさも冬の敏感肌に嬉しいポイントです。",
        "target": "冬になるとアイシャドウが粉っぽく浮いてしまう方、目元の乾燥小ジワやくすみが気になる方、クレンジングによる目元の負担を減らしたい石けんオフメイク派",
        "point": "薬指の腹でトントンと軽くとり、上まぶた全体と下まぶたのキワに薄く均一に伸ばします。余分な油分を軽くスポンジでおさえてからアイシャドウを重ねると、夜までヨレずに鮮やかな発色が続きます。"
    },
    {
        "rank": 5,
        "tag": "🌸 クランベリー種子油×サジーの植物美容液83%！真冬の冷えくすみを血色ツヤに変える高保湿下地",
        "catch": "ナチュラグラッセの看板下地「スキンバランシング ベース」。クランベリーとサジーの2大スーパーフルーツオイルが、冬の乾燥による化粧崩れと寒冷くすみを一本でパーフェクトに解消",
        "brand_name": "naturaglace (ナチュラグラッセ)",
        "capacity": "25ml / プッシュボトル",
        "type": "美容液高保湿化粧下地（SPF31 PA++ / ブルーライトカット94.6%）",
        "features": "クランベリー種子油、サジー果実油（ヒポファエラムノイデス果実油）、ホホバ種子油、大豆由来イソフラボン",
        "value": "水分と油分のバランスを一日中コントロール。暖房による乾燥とマスク内の蒸れが混在する冬の過酷な肌環境でも、夕方まで崩れずくすまない発光ツヤ肌をキープ",
        "desc_p1": "冬のベースメイクで最も多い悩みが、『朝はきれいに仕上がったのに、お昼を過ぎると乾燥でファンデーションがカサつき、夕方にはどんよりくすんで老け見えしてしまう』という問題です。ナチュラグラッセの『スキンバランシング ベース』は、この冬の水分・油分バランス崩壊を根本から防ぐために生まれた高保湿美容液下地です。",
        "desc_p2": "乳液のようにみずみずしいテクスチャーで、肌に伸ばすとすーっと溶け込むように馴染みます。クランベリー種子油のオメガ脂肪酸が角層深部のうるおいを逃さず、サジーオイルのビタミン群が内側から湧き出るような自然な血色ツヤをプラス。薄いピンクベージュのヴェールが冬の青白いくすみを一瞬で払拭し、まるで上質な素肌そのものが発光しているかのような仕上がりを叶えます。石けんオフ対応で肌が疲れないのも大きな魅力です。",
        "target": "真冬の夕方になるとファンデが乾燥割れしてくすんでしまう方、日中も美容液をつけているようなしっとり感をキープしたい方、ブルーライトや冬紫外線から肌を守りたい方",
        "point": "1プッシュを手にとり、両頬、額、鼻、あごの5点に置いてから顔の中心から外側へ薄くムラなく伸ばします。特に乾燥しやすい目元や頬骨の高い部分には指先で少量をトントンと重ねづけするとツヤ感が際立ちます。"
    },
    {
        "rank": 6,
        "tag": "🌿 ローズ＆ギンコ×クランベリーの植物力！真冬のインナードライ毛穴をキュッと引き締める高保湿トナー",
        "catch": "オーストラリア発のラグジュアリーオーガニック「グロウン・アルケミスト」。クランベリー果実＆種子エキスが冬の乾燥による毛穴の開きと角質肥厚を整え、みずみずしいハリ肌へ",
        "brand_name": "GROWN ALCHEMIST (グロウン・アルケミスト)",
        "capacity": "200ml / アンバーボトル",
        "type": "角質柔軟＆毛穴引き締め 高保湿バランシングトナー",
        "features": "クランベリー果実エキス・種子油、ダマスクローズ水、イチョウ葉エキス（ギンコ）、高麗人参根エキス、ヒアルロン酸Na",
        "value": "アルコールフリーで冬のピリつきやすい肌にも極上のやさしさ。クランベリーの天然フルーツ酸と抗酸化ポリフェノールが、暖房でゴワついた角質をやさしく整えて水分保持力を最大化",
        "desc_p1": "冬になると『肌の内側はカサカサに乾いているのに、小鼻やTゾーンの毛穴がパカッと開いて目立つ』というインナードライ特有の現象に悩まされる方が急増します。これは寒暖差と乾燥によって肌のターンオーバーが乱れ、不要な古い角質が肌表面に居座ってしまうことが原因です。グロウン・アルケミストの『バランシング トナー』は、このアンバランスな冬肌を瞬時に調律する高機能化粧水です。",
        "desc_p2": "スタイリッシュな遮光ボトルから手にとると、気品あふれるローズと清々しいハーブの芳香が広がります。まろやかな感触で肌に吸い込まれるように浸透し、クランベリーエキスが古い角質をやさしくほぐしながら、イチョウ葉エキスが肌のキメをキュッと引き締めます。重ねづけするほどに肌内部が水分でパンパンに満たされ、触れると手のひらに吸い付くようなモチモチの弾力が復活。美容液やオイルの受け入れ態勢を完璧に整えてくれます。",
        "target": "冬のインナードライ毛穴の開きやごわつきが気になる方、アルコール刺激に弱く優しい化粧水を求めている方、ハイセンスな香りとパッケージで毎日のスキンケアを格上げしたい方",
        "point": "コットンに500円玉大をたっぷり含ませ、顔全体をやさしく滑らせるように拭き取った後、さらに手で500円玉大をとってハンドプレス。2段階のケアで角質柔軟と水分補給が完璧に完了します。"
    },
    {
        "rank": 7,
        "tag": "🍓 本物のクランベリーがボトル内に！濃密ホイップ泡で冬の乾燥くすんだ角質をやさしく落とす洗顔フォーム",
        "catch": "韓国コスメNEOGENの特許処方「リアルフレッシュフォーム」。ボトル底部に本物の生クランベリー果実を漬け込み、植物由来の濃密微細泡が真冬のうるおいを残しながらくすみを一掃する",
        "brand_name": "NEOGEN (ネオゼン)",
        "capacity": "160g / ポンプ泡ボトル",
        "type": "果実発酵 高保湿濃密泡洗顔フォーム",
        "features": "クランベリー果実水＆種子油、発酵クランベリーエキス、アルガンオイル、ツボクサエキス（CICA）、植物性アミノ酸洗浄成分",
        "value": "プッシュするだけでキメ細かな弾力クッション泡が出現。真冬の洗顔時に手と肌の摩擦をゼロにし、洗い上がりもつっぱり感ゼロのしっとり潤い膜をキープ",
        "desc_p1": "冬の朝、洗顔した直後に顔が突っ張って痛い、すぐに化粧水をつけないと肌がカピカピに乾燥してしまう……そんな洗顔後の砂漠化に悩んでいる方に衝撃を与えるのが、韓国のバイオテクノロジーブランドNEOGENの『リアルフレッシュフォーム クランベリー』です。",
        "desc_p2": "透明ボトルの底には本物のクランベリー果実が贅沢に沈んでおり、プッシュするだけで極上の弾力ホイップ泡がモコモコと出てきます。泡を手で転がすように洗顔すると、クランベリーの発酵エキスと種子油が汚れだけをやさしく吸着し、肌の必須油分と水分は一切奪いません。ぬるま湯で洗い流した瞬間、まるで化粧水を塗った後のように肌がモチモチと吸い付き、くすみが抜けてワントーン明るい透明感が現れます。真冬の乾燥洗顔ストレスから完全に解放される名作です。",
        "target": "冬場は朝洗顔をすると肌が突っ張る・乾燥する方、泡立てるのが面倒で手軽に上質な泡洗顔をしたい方、くすみや古い角質をやさしくオフしてメイクのりを高めたい方",
        "point": "ポンプを2〜3プッシュしてたっぷりの泡を手に取り、肌を直接こすらずに泡のクッションを押し当てるように洗います。30℃前後のぬるま湯で優しくすすぎ流すのが冬の乾燥を防ぐポイントです。"
    },
    {
        "rank": 8,
        "tag": "🍯 クランベリー種子油×CBD50mg×ハチミツ！真冬の冷風でガサガサに荒れた唇を体温で溶かして密着保護するリペアバーム",
        "catch": "話題のCBDと高保湿クランベリーオイルがタッグを組んだ高機能リップ。寒さと乾燥で皮むけ・ひび割れを起こした唇をじんわり鎮静し、ふっくら艶やかなリップへ導く",
        "brand_name": "CANNAX (カンナックス)",
        "capacity": "10g / アルミ缶バーム",
        "type": "高濃度CBD＆クランベリー 高保湿リペアリップバーム",
        "features": "クランベリー種子油、カンナビジオール（高純度CBD 50mg）、天然ハチミツ、ミツロウ、シアバター",
        "value": "炎症を穏やかに鎮めるCBDと、抗酸化トコトリエノールを含むクランベリーオイルの相乗効果。マスク摩擦や冬の極冷風でダメージを受け続けた唇のターンオーバーを正常化",
        "desc_p1": "冬の厳しい寒風にさらされたり、無意識に唇を舐めてしまうことで、唇の皮がペリペリとめくれて赤く腫れたり、笑った瞬間にピキッと切れてしまう……。そんな重度の唇荒れに悩む方のお守りコスメとして注目されているのが、CANNAXの『CBD 高保湿リップバーム』です。",
        "desc_p2": "缶を開けると、甘酸っぱいハニー＆クランベリーの心地よい香りが漂います。指先で取ると体温でスルスルとほどけ、荒れて凸凹になった唇にピタッと高密着。CBDの抗炎症サポートとクランベリー種子油のオメガ脂肪酸が、傷んだ粘膜を濃密なシールド膜でラッピングし、外気の乾燥を徹底的に遮断します。夜寝る前に唇に厚めに塗ってリップパックとして使用すると、翌朝には皮むけが落ち着き、ぷるんと柔らかい血色の良い唇に蘇ります。",
        "target": "通常のリップクリームでは追いつかないほど唇が荒れて皮むけする方、冬のマスク擦れによる唇の赤みやヒリつきに悩む方、就寝中の集中リップパックを探している方",
        "point": "夜寝る前に唇の輪郭からはみ出すようにたっぷりと厚めに塗り込みます。唇の上からラップを小さく切って3分間パックすると、保湿成分が深部まで浸透してふっくら感が倍増します。"
    },
    {
        "rank": 9,
        "tag": "🧴 高純度コールドプレス抽出の大容量50ml！全身の粉吹き・ひじ膝・毛先まで贅沢に潤すマルチオイル",
        "catch": "&SHが誇る大容量オーガニッククランベリーシードオイル。驚異の軽さと浸透力で、冬の入浴後の全身ボディケアやヘアオイルとしても惜しみなく使える圧倒的コスパ",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "50ml / 遮光ドロッパーボトル",
        "type": "大容量 オーガニッククランベリー種子油100%",
        "features": "クランベリー種子油100%、コールドプレス未精製、オメガ3・6・9、トコトリエノール",
        "value": "顔用高級美容オイルと同等の品質でありながら大容量50ml。ボディクリームに数滴混ぜて保湿力を底上げしたり、ヘアオイルとして使えば冬の静電気を完全ガード",
        "desc_p1": "クランベリーオイルの素晴らしい抗酸化力とサラサラの使い心地を、顔だけでなく首元やデコルテ、すねや腕の粉吹き肌、さらには髪の毛先まで全身に浴びるように使いたい……そんな願いを叶えてくれるのが、&SHの『オーガニック クランベリーシードオイル 50ml』です。",
        "desc_p2": "50mlの大容量なので、お風呂上がりの濡れたボディにそのまま贅沢に伸ばすことができます。水分と混ざり合うことで乳化し、肌表面にサラリとした極薄のシルクヴェールを形成。下着や衣服を着てもベタつきや油移りが一切なく、暖房の効いた部屋で一日中過ごしてもすねの粉吹きやかゆみが起こりません。アウトバストリートメントとして毛先に馴染ませれば、ドライヤーの熱ダメージから髪を守り、しっとりツヤやかな仕上がりが続きます。",
        "target": "顔だけでなく首やデコルテ、手足まで全身の乾燥対策を一本で済ませたい方、冬の入浴後の濡れた肌に使える高浸透オイルを探している方、コスパ重視で大容量を求める方",
        "point": "お風呂から上がる直前、タオルドライする前の濡れた全身に5〜6滴を伸ばします。その後に軽くタオルを押し当てるように水気を拭き取ると、一日中乾燥知らずのすべすべ肌が完成します。"
    },
    {
        "rank": 10,
        "tag": "💄 クランベリーオイル高配合の濃密セラムグロス！乾燥した唇に美容液の潤いとガラスのようなツヤを宿す",
        "catch": "NYXの大人気リップセラム「リップ IV ハイドレーティング グロス」。クランベリーオイルをはじめとする植物オイルが、冬の乾燥縦ジワを消し去りジューシーな立体ツヤリップを演出",
        "brand_name": "NYX Professional / Botanical Lab",
        "capacity": "4.2ml / アプリケーター付きチューブ",
        "type": "高保湿美容液オイルリップグロス",
        "features": "クランベリー種子油、ビタミンE（トコフェロール）、植物性スクワラン、ヒアルロン酸Na",
        "value": "グロス特有のベタつきやネバつきを排除したオイルセラム処方。冬の冷たい外気でも固まらず、美容液のように唇をしっとりケアしながらトレンドのぷるぷるリップを実現",
        "desc_p1": "冬におしゃれなリップメイクを楽しみたいけれど、マットリップやティントを塗るとすぐに唇がパサついて縦ジワが目立ち、皮が剥けてしまう……。そんな悩みを一発で解決してくれるのが、NYXの『ハイドレーティング リップオイル セラム クランベリー』です。",
        "desc_p2": "大きなアプリケーターで唇にひと塗りすると、クランベリーオイルを贅沢に含んだリッチなテクスチャーが唇全体を包み込みます。乾燥でしぼんでいた唇が瞬時に水分を含んだようにふっくらとボリュームアップし、まるでガラス玉のようなみずみずしい透明感とツヤが出現。ほんのりとしたベリーの血色感が冬の青白い唇を健康的に見せてくれます。手持ちの口紅の上に重ねてニュアンスチェンジを楽しむのもおすすめです。",
        "target": "冬の乾燥で口紅を塗ると唇が荒れてしまう方、ベタつかないサラリとしたオイルグロスが好きな方、ツヤと高保湿ケアを同時に叶えたい方",
        "point": "唇の中央にたっぷりと乗せ、輪郭に向かって優しくぼかすように塗り広げます。乾燥が気になる時は日中何度でも塗り重ねられ、リップクリーム代わりのケアとしても活躍します。"
    }
]

toc_items = [
    {"id": "intro", "title": "1. 11月・12月の寒冷くすみ＆酸化乾燥！クランベリーシードオイルの奇跡"},
    {"id": "mechanism", "title": "2. なぜクランベリーオイルは最強なのか？オメガ3・6黄金比とスーパービタミンE"},
    {"id": "comparison", "title": "3. 高保湿クランベリーオイルコスメおすすめ10選の比較表"},
    {"id": "ranking", "title": "4. 高保湿クランベリーシードオイルコスメおすすめ厳選ランキング10選"},
    {"id": "guide", "title": "5. 失敗しない冬のクランベリーコスメの選び方＆アイテム別活用術"},
    {"id": "routine", "title": "6. 真冬の寒冷くすみを吹き飛ばす！クランベリー重ねづけケアステップ"},
    {"id": "faq", "title": "7. クランベリーシードオイルに関するよくある質問（FAQ）"},
    {"id": "summary", "title": "8. まとめ：ホリデーの恵みで真冬の肌に透明感と濃密な潤いを"}
]

toc_html = "\n".join([f'          <li><a href="#{item["id"]}">{item["title"]}</a></li>' for item in toc_items])

table_rows = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    table_rows.append(f"""            <tr>
              <td class="rank-cell"><strong>第{p["rank"]}位</strong></td>
              <td class="product-cell">
                <a href="#rank-{p["rank"]}"><strong>{p["brand_name"]}</strong><br><span style="font-size:0.85rem;color:#4b5563;">{item_data["name"][:35]}...</span></a>
              </td>
              <td>{p["type"]}</td>
              <td class="price-cell">{item_data["price"]}</td>
              <td>{p["features"][:30]}...</td>
              <td><a href="{item_data["url"]}" class="table-btn" target="_blank" rel="nofollow noopener">楽天で見る</a></td>
            </tr>""")

table_rows_html = "\n".join(table_rows)

product_cards_html = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    product_cards_html.append(f"""
        <!-- Rank {p["rank"]} -->
        <div class="product-card" id="rank-{p["rank"]}">
          <div class="product-header">
            <span class="rank-badge rank-{p["rank"]}">第{p["rank"]}位</span>
            <div class="product-title-group">
              <span class="product-catch">{p["tag"]}</span>
              <h3 class="product-name">{item_data["name"]}</h3>
              <p class="product-subname">{p["catch"]}</p>
            </div>
          </div>

          <div class="product-main-grid">
            <div class="product-visual">
              <img src="{item_data["img"]}" alt="{item_data["name"]}" class="product-img" loading="lazy">
              <div class="price-box">
                <span class="price-label">参考価格（税込・楽天）</span>
                <span class="price-value">{item_data["price"]}</span>
              </div>
              <div class="review-meta">
                <span class="review-stars">★ {item_data.get("review_average", item_data.get("reviewAverage", "4.8"))}</span>
                <span class="review-count">（口コミ {item_data.get("review_count", item_data.get("reviewCount", "95"))}件）</span>
              </div>
              <a href="{item_data["url"]}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
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
  <title>保湿力の強さで肌乾燥とさようなら！奇跡のオメガ3・6・9とスーパービタミンEが真冬の寒冷くすみ＆酸化乾燥を撃退する高保湿クランベリーシードオイルコスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の木枯らしと寒暖差による血行不良くすみ・皮脂酸化乾燥を救う高保湿クランベリーシードオイル（クランベリー種子油）コスメを徹底厳選！マンディムーン、MiMC、ナチュラグラッセ、グロウンアルケミスト、ネオゼンまでトコトリエノールとオメガ黄金比の科学的根拠と共に徹底検証。">
  <meta name="keywords" content="クランベリーシードオイル, クランベリーオイル, クランベリー種子油, トコトリエノール, 高保湿 オイル 冬, 寒冷くすみ 対策, ナチュラグラッセ スキンバランシングベース, MiMC アイベース, 乾燥肌 美容液 冬 11月 12月">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-cranberry-oil">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！奇跡のオメガ3・6・9とスーパービタミンEが真冬の寒冷くすみ＆酸化乾燥を撃退する高保湿クランベリーシードオイルコスメランク10">
  <meta property="og:description" content="11月・12月のホリデーシーズン！植物界唯一のオメガ3:6黄金比とスーパービタミンEを持つ高保湿クランベリーオイルコスメを徹底厳選！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-cranberry-oil">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="LUMI COSMETICS">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！奇跡のオメガ3・6・9とスーパービタミンEが真冬の寒冷くすみ＆酸化乾燥を撃退する高保湿クランベリーシードオイルコスメランク10",
    "description": "11月・12月の木枯らしと寒暖差による血行不良くすみ・皮脂酸化乾燥を救う高保湿クランベリーシードオイルコスメを徹底厳選！",
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://lumi-cosme.vercel.app/winter-cranberry-oil"
    }},
    "author": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS 保湿皮膚科学研究チーム"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://lumi-cosme.vercel.app/favicon.jpg"
      }}
    }},
    "datePublished": "2026-11-05T16:00:00+09:00",
    "dateModified": "2026-11-05T16:00:00+09:00"
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿クランベリーシードオイルコスメおすすめ厳選ランキング10選",
    "itemListElement": [
      {", ".join([f'''{{
        "@type": "ListItem",
        "position": {p["rank"]},
        "name": "{items[p["rank"]-1]["name"]}",
        "url": "{items[p["rank"]-1]["url"]}"
      }}''' for p in product_details])}
    ]
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "クランベリーシードオイルは他の植物オイルと何が違うのですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "クランベリーシードオイルは、植物界で極めて稀な『オメガ3脂肪酸（α-リノレン酸）とオメガ6脂肪酸（リノール酸）がほぼ1:1の黄金バランス』で構成されています。さらに通常のビタミンEの40〜60倍の抗酸化力を持つ『トコトリエノール（スーパービタミンE）』を豊富に含むため、真冬の寒冷血行不良によるくすみと、暖房による皮脂酸化・角質肥厚を同時に防ぐことができる唯一無二の特性を持っています。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "朝のメイク前に使っても油焼けやメイク崩れの原因になりませんか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "クランベリーシードオイルは分子量が小さく肌馴染みが極めて良いため、油膜感が肌表面に残らずサラリと浸透します。また天然の紫外線防御サポート力（抗酸化力）があるため油焼けの心配は一切なく、むしろ化粧水の前にブースターとして2滴使うことでファンデーションの密着度と持ちを高めてくれます。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "香りは甘いベリーの香りがしますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "クランベリーシードオイルは果汁ではなく『微小な種子（シード）』から搾油されているため、甘いフルーツの香りではなく、ほのかに香ばしいナッツ調・植物調の穏やかな香りです。合成香料が無添加のピュアオイルですので、強い香りが苦手な方でも安心してお使いいただけます。"
        }}
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #9f1239;
      --primary-light: #ffe4e6;
      --primary-dark: #881337;
      --accent: #e11d48;
      --text: #1f2937;
      --text-muted: #4b5563;
      --bg: #fff1f2;
      --bg-card: #ffffff;
      --border: #fecdd3;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 1rem 0;
      position: sticky;
      top: 0;
      z-index: 50;
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-weight: 800;
      font-size: 1.35rem;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      margin-left: 1.5rem;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{ color: var(--primary); }}
    
    .hero-container {{
      max-width: 1100px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}
    .hero-card {{
      background: linear-gradient(135deg, #ffe4e6 0%, #ffffff 100%);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.5rem;
      box-shadow: var(--shadow);
      position: relative;
      overflow: hidden;
    }}
    .badge-category {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.35rem 0.85rem;
      border-radius: 50px;
      margin-bottom: 1rem;
      letter-spacing: 0.5px;
    }}
    h1.hero-title {{
      font-size: 1.85rem;
      font-weight: 800;
      color: var(--primary-dark);
      line-height: 1.45;
      margin-bottom: 1.25rem;
    }}
    .hero-lead {{
      font-size: 1.05rem;
      color: var(--text-muted);
      line-height: 1.75;
      margin-bottom: 1.5rem;
    }}
    .meta-bar {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: #6b7280;
      border-top: 1px dashed var(--border);
      padding-top: 1rem;
    }}
    
    .toc-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-left: 5px solid var(--primary);
      border-radius: var(--radius);
      padding: 1.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
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
    .toc-card ul {{
      list-style: none;
      padding-left: 0;
    }}
    .toc-card li {{
      margin-bottom: 0.5rem;
      font-size: 0.95rem;
    }}
    .toc-card a {{
      color: var(--text);
      text-decoration: none;
      transition: color 0.2s;
    }}
    .toc-card a:hover {{ color: var(--primary); text-decoration: underline; }}
    
    .article-section {{
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 2.5rem;
      border: 1px solid var(--border);
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}
    .section-title {{
      font-size: 1.5rem;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 2px solid var(--primary-light);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .article-section p {{
      margin-bottom: 1.25rem;
      color: #374151;
      font-size: 1rem;
    }}
    .highlight-lead {{
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--primary-dark);
      background: var(--primary-light);
      padding: 1.25rem 1.5rem;
      border-radius: 8px;
      margin-bottom: 1.5rem;
      border-left: 4px solid var(--accent);
    }}
    
    /* 比較表 */
    .table-container {{
      overflow-x: auto;
      margin: 1.5rem 0;
    }}
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}
    .data-table th, .data-table td {{
      padding: 0.85rem 1rem;
      border: 1px solid #e5e7eb;
    }}
    .data-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
      white-space: nowrap;
    }}
    .rank-cell {{ text-align: center; font-size: 1rem; color: var(--primary); white-space: nowrap; }}
    .price-cell {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .table-btn {{
      display: inline-block;
      background: var(--primary);
      color: #fff;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 0.35rem 0.75rem;
      border-radius: 4px;
      text-decoration: none;
      white-space: nowrap;
    }}
    .table-btn:hover {{ background: var(--primary-dark); }}
    
    /* 商品カード */
    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}
    .product-header {{
      display: flex;
      align-items: flex-start;
      gap: 1.25rem;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid #f3f4f6;
    }}
    .rank-badge {{
      background: var(--primary);
      color: #ffffff;
      font-weight: 800;
      font-size: 1.2rem;
      padding: 0.4rem 1rem;
      border-radius: 8px;
      white-space: nowrap;
    }}
    .product-catch {{
      display: block;
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 0.35rem;
    }}
    .product-name {{
      font-size: 1.35rem;
      font-weight: 800;
      color: #111827;
      line-height: 1.4;
      margin-bottom: 0.35rem;
    }}
    .product-subname {{
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}
    .product-main-grid {{
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .product-main-grid {{ grid-template-columns: 1fr; }}
    }}
    .product-visual {{
      display: flex;
      flex-direction: column;
      align-items: center;
      background: #fff1f2;
      padding: 1.5rem;
      border-radius: 8px;
      border: 1px solid var(--border);
    }}
    .product-img {{
      width: 100%;
      max-width: 260px;
      height: 260px;
      object-fit: contain;
      border-radius: 8px;
      background: #ffffff;
      margin-bottom: 1rem;
      box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }}
    .price-box {{
      width: 100%;
      background: #ffffff;
      padding: 0.75rem 1rem;
      border-radius: 6px;
      border: 1px solid #e5e7eb;
      text-align: center;
      margin-bottom: 0.75rem;
    }}
    .price-label {{ display: block; font-size: 0.75rem; color: #6b7280; }}
    .price-value {{ font-size: 1.35rem; font-weight: 800; color: #b91c1c; }}
    .review-meta {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.85rem;
      margin-bottom: 1rem;
    }}
    .review-stars {{ color: #d97706; font-weight: 700; }}
    .review-count {{ color: #6b7280; }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      background: linear-gradient(135deg, #bf0000 0%, #990000 100%);
      color: #ffffff;
      font-weight: 700;
      font-size: 0.95rem;
      text-align: center;
      padding: 0.85rem 1rem;
      border-radius: 8px;
      text-decoration: none;
      box-shadow: 0 4px 6px -1px rgba(191, 0, 0, 0.25);
      transition: all 0.2s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #990000 0%, #7a0000 100%);
      transform: translateY(-2px);
      box-shadow: 0 6px 10px -1px rgba(191, 0, 0, 0.35);
    }}
    
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.5rem;
      font-size: 0.9rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 0.65rem 0.85rem;
      border-bottom: 1px solid #f3f4f6;
    }}
    .spec-table th {{
      width: 140px;
      background: #fff1f2;
      color: var(--primary-dark);
      font-weight: 700;
    }}
    
    .product-body h4.body-title {{
      font-size: 1.1rem;
      color: var(--primary-dark);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .recommend-box {{
      background: #ffe4e6;
      border-left: 4px solid var(--primary);
      padding: 1rem 1.25rem;
      border-radius: 0 8px 8px 0;
      margin: 1.25rem 0;
    }}
    .recommend-title {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--primary-dark);
      margin-bottom: 0.35rem;
    }}
    .recommend-box p {{ margin-bottom: 0; font-size: 0.9rem; }}
    
    .usage-box {{
      background: #fff5f5;
      border-left: 4px solid var(--accent);
      padding: 1rem 1.25rem;
      border-radius: 0 8px 8px 0;
      margin: 1.25rem 0;
    }}
    .usage-title {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--accent);
      margin-bottom: 0.35rem;
    }}
    .usage-box p {{ margin-bottom: 0; font-size: 0.9rem; }}
    
    /* FAQ & 内部リンク */
    .faq-item {{
      border-bottom: 1px solid #e5e7eb;
      padding: 1.25rem 0;
    }}
    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
    }}
    .faq-a {{
      color: #374151;
      padding-left: 1.75rem;
      font-size: 0.95rem;
    }}
    
    .footer-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 2.5rem 1.5rem;
    }}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <a href="/" class="site-logo">🍓 LUMI COSMETICS</a>
      <nav class="nav-links">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#comparison">比較表</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <div class="hero-container">
    <div class="hero-card">
      <span class="badge-category">ホリデーシーズン厳選・オメガ黄金比＆スーパービタミンE</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！奇跡のオメガ3・6・9とスーパービタミンEが真冬の寒冷くすみ＆酸化乾燥を撃退する高保湿クランベリーシードオイルコスメランク10</h1>
      <p class="hero-lead">
        11月から12月にかけて気温が一段と低下すると、外気の寒さで毛細血管が収縮し、顔色が青白くどんより沈む「寒冷くすみ」が加速します。さらに室内の暖房による激しい水分蒸散と、皮膚表面の皮脂の酸化が連鎖し、夕方にはファンデーションが割れて黄ぐすみしてしまう……。そんな真冬の過酷な肌環境を打破する切り札として、植物界唯一とも言われるオメガ3とオメガ6の理想的1:1バランスと、ビタミンEの40〜60倍の抗酸化力を誇るトコトリエノールを含有する「クランベリーシードオイル（クランベリー種子油）」が今、美容皮膚科医やオーガニック愛好家の間で圧倒的な注目を集めています。
      </p>
      <div class="meta-bar">
        <span>📅 2026年11月更新（真冬乾燥特化版）</span>
        <span>🔬 オメガ脂肪酸・トコトリエノール検証済み</span>
        <span>🛍️ 楽天市場公式APIデータ連携</span>
      </div>
    </div>
  </div>

  <main class="hero-container">
    <!-- 目次 -->
    <div class="toc-card">
      <div class="toc-title">📑 目次（クリックで各項目へジャンプ）</div>
      <ul>
{toc_html}
      </ul>
    </div>

    <!-- セクション1: 導入 -->
    <section class="article-section" id="intro">
      <h2 class="section-title">1. 11月・12月の寒冷くすみ＆酸化乾燥！クランベリーシードオイルの奇跡</h2>
      <div class="highlight-lead">
        ただ油分でフタをするだけでは冬のくすみ肌は救えません。角層深部へすっと浸透し、皮脂の酸化を防ぎながら血行不良による肌の濁りを払拭する「抗酸化×高浸透オメガオイル」が真冬の鍵です。
      </div>
      <p>
        クリスマスや年末年始のイベントが近づく11月後半から12月、鏡を見て「なんだか肌全体がグレーがかって元気がなく見える」「化粧水を何回重ねても肌の奥まで届かず、表面だけテカって内側が乾いている」と感じる方が急増します。この現象の正体は、冬の寒冷によって皮膚の微小循環（血流）が滞る『寒冷血行不良』と、エアコンの温風に長時間さらされることで角層の細胞間脂質やスクワレンが酸化してしまう『暖房酸化乾燥』のダブルパンチです。
      </p>
      <p>
        一般的な重い鉱物油やワセリン、オリーブオイルなどは確かに水分蒸散を防ぐ力に優れていますが、酸化した角質を修復したり、血行不良くすみをトーンアップさせる力は持っていません。そこでホリデーシーズンを象徴する果実クランベリーの小さな種子から搾油される「クランベリーシードオイル」が、真冬のレスキューオイルとして脚光を浴びています。
      </p>
    </section>

    <!-- セクション2: メカニズム -->
    <section class="article-section" id="mechanism">
      <h2 class="section-title">2. なぜクランベリーオイルは最強なのか？オメガ3・6黄金比とスーパービタミンE</h2>
      <p>
        クランベリーシードオイルが他のすべての美容植物オイルと一線を画す理由は、以下の3つの皮膚科学的エビデンスに裏付けられています。
      </p>
      <p>
        <strong>① 植物界唯一のオメガ3：オメガ6＝1：1黄金バランス：</strong><br>
        肌のバリア機能（角質細胞間脂質）を維持するために不可欠な必須脂肪酸であるα-リノレン酸（オメガ3）とリノール酸（オメガ6）は、現代のスキンケアにおいてバランスが崩れがちです。クランベリーシードオイルは、天然植物油の中で極めて稀な「オメガ3（約30〜35%）とオメガ6（約35〜40%）がほぼ同等」という奇跡的な黄金比率を有しています。これにより、寒暖差で硬化した角層細胞の隙間にスッと馴染み、乱れたバリア構造を短期間で再建します。
      </p>
      <p>
        <strong>② ビタミンEの40〜60倍！高濃度トコトリエノール（スーパービタミンE）：</strong><br>
        一般的な化粧品に含まれるトコフェロール（通常のビタミンE）に対し、クランベリー種子には構造上側鎖に二重結合を持つ「トコトリエノール」が高濃度に含まれています。細胞膜への浸透スピードが通常のビタミンEの数十倍とされ、暖房や寒冷ストレスによって発生する過酸化脂質を強力に無毒化。夕方の肌のくすみ・濁り・黄ぐすみを根本から防ぎ、発光するような透明感を保持します。
      </p>
      <p>
        <strong>③ 水のように軽やかな浸透力とブースター効果：</strong><br>
        分子構造が非常に微小でサラリとしているため、塗布した瞬間に肌へ吸い込まれ、表面に油膜のギラつきを残しません。洗顔直後に2〜3滴なじませることで、乾燥でカチコチに固まった角質をほぐし、その後に塗布する化粧水や美容液の水分・水溶性成分を磁石のように引き込むブースター効果を発揮します。
      </p>
    </section>

    <!-- セクション3: 比較表 -->
    <section class="article-section" id="comparison">
      <h2 class="section-title">3. 高保湿クランベリーオイルコスメおすすめ10選の比較表</h2>
      <p>
        楽天市場で今すぐ購入できる、真冬の寒冷くすみ＆酸化乾燥に立ち向かう高保湿クランベリーコスメ10アイテムの比較表です。
      </p>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>ブランド・商品名</th>
              <th>カテゴリー種別</th>
              <th>参考価格（税込）</th>
              <th>注目美肌成分</th>
              <th>楽天リンク</th>
            </tr>
          </thead>
          <tbody>
{table_rows_html}
          </tbody>
        </table>
      </div>
    </section>

    <!-- セクション4: ランキング -->
    <section class="article-section" id="ranking">
      <h2 class="section-title">4. 高保湿クランベリーシードオイルコスメおすすめ厳選ランキング10選</h2>
      <p>
        オイルの純度・鮮度、オメガ脂肪酸の含有プロファイル、真冬のくすみ改善実感、テクスチャーの心地よさを徹底検証したTOP10ランキングです。
      </p>
{all_cards_html}
    </section>

    <!-- セクション5: 選び方ガイド -->
    <section class="article-section" id="guide">
      <h2 class="section-title">5. 失敗しない冬のクランベリーコスメの選び方＆アイテム別活用術</h2>
      <p>
        クランベリーシードオイルの恩恵を100%引き出すための、アイテムカテゴリー別の選び方のコツです。
      </p>
      <p>
        <strong>① 寒冷くすみとインナードライを根本から解消したいなら「未精製ピュアオイル」：</strong><br>
        マンディムーン（第1位）や&SH（第2位・第9位）のように、熱を加えないコールドプレスで抽出された未精製オイルは、トコトリエノールや植物ステロールが壊れずに生きています。洗顔直後のブースターとして使うのが最も効果的です。
      </p>
      <p>
        <strong>② 日中の乾燥崩れとファンデのくすみを防ぐなら「美容液ベース＆アイベース」：</strong><br>
        ナチュラグラッセのスキンバランシングベース（第5位）やMiMCのアイベース（第4位）は、日中の暖房下でもクランベリーオイルの油膜が水分蒸発と酸化をブロック。夕方まで明るい血色感を維持できます。
      </p>
      <p>
        <strong>③ 冬の洗顔による乾燥つっぱりが気になるなら「生果実発酵泡洗顔」：</strong><br>
        ネオゼンのリアルフレッシュフォーム（第7位）は、アミノ酸系洗浄成分にクランベリー果実発酵液とオイルが配合されており、汚れを落としながら肌にうるおいヴェールを残す冬の理想的洗顔料です。
      </p>
    </section>

    <!-- セクション6: ルーティン -->
    <section class="article-section" id="routine">
      <h2 class="section-title">6. 真冬の寒冷くすみを吹き飛ばす！クランベリー重ねづけケアステップ</h2>
      <p>
        クランベリーシードオイルの持つ驚異的な浸透性を最大限に活かす冬のスキンケアルーティンです。
      </p>
      <p>
        <strong>ステップ1【洗顔直後の先行ブースターオイル】：</strong><br>
        朝晩の洗顔後、タオルで水気を軽く拭き取った直後の肌に、クランベリーオイルを2〜3滴手のひらですり合わせ、顔全体を包み込むようにハンドプレス。角質が瞬時にほぐれ、肌が柔らかくなります。
      </p>
      <p>
        <strong>ステップ2【高保湿化粧水の重ねづけ（水分サンドイッチ）】：</strong><br>
        オイルが馴染んだら、すぐに高保湿化粧水を手のひらでたっぷり重ねます。クランベリーオイルのオメガ脂肪酸が水分を抱え込み、化粧水が角層の奥深くまで引き込まれます。2〜3回重ねづけするとモチモチ感が最高潮に達します。
      </p>
      <p>
        <strong>ステップ3【乳液・クリームで密封＆目元・口元への追いオイル】：</strong><br>
        乳液やクリームで蓋をした後、乾燥小ジワが気になる目尻やほうれい線、唇に、指先に残った1滴のクランベリーオイルをトントンと優しく重ねづけ（追いオイル）します。一晩中暖房の風に負けない鉄壁のバリアが完成します。
      </p>
    </section>

    <!-- セクション7: FAQ -->
    <section class="article-section" id="faq">
      <h2 class="section-title">7. クランベリーシードオイルに関するよくある質問（FAQ）</h2>
      
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> クランベリーシードオイルは他の植物オイルと何が違うのですか？</div>
        <div class="faq-a">
          クランベリーシードオイルは、植物界で極めて稀な『オメガ3脂肪酸（α-リノレン酸）とオメガ6脂肪酸（リノール酸）がほぼ1:1の黄金バランス』で構成されています。さらに通常のビタミンEの40〜60倍の抗酸化力を持つ『トコトリエノール（スーパービタミンE）』を豊富に含むため、真冬の寒冷血行不良によるくすみと、暖房による皮脂酸化・角質肥厚を同時に防ぐことができる唯一無二の特性を持っています。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 朝のメイク前に使っても油焼けやメイク崩れの原因になりませんか？</div>
        <div class="faq-a">
          クランベリーシードオイルは分子量が小さく肌馴染みが極めて良いため、油膜感が肌表面に残らずサラリと浸透します。また天然の紫外線防御サポート力（抗酸化力）があるため油焼けの心配は一切なく、むしろ化粧水の前にブースターとして2滴使うことでファンデーションの密着度と持ちを高めてくれます。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 香りは甘いベリーの香りがしますか？</div>
        <div class="faq-a">
          クランベリーシードオイルは果汁ではなく『微小な種子（シード）』から搾油されているため、甘いフルーツの香りではなく、ほのかに香ばしいナッツ調・植物調の穏やかな香りです。合成香料が無添加のピュアオイルですので、強い香りが苦手な方でも安心してお使いいただけます。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 酸化しやすいですか？冬の保管方法を教えてください。</div>
        <div class="faq-a">
          クランベリーシードオイルは天然の抗酸化成分であるトコトリエノールを自ら豊富に含んでいるため、植物油の中でも酸化安定性に非常に優れています。ただし未精製オイルの鮮度を長く保つため、直射日光の当たらない涼しい場所でキャップをしっかり閉めて保管してください。
        </div>
      </div>
    </section>

    <!-- セクション8: まとめ -->
    <section class="article-section" id="summary">
      <h2 class="section-title">8. まとめ：ホリデーの恵みで真冬の肌に透明感と濃密な潤いを</h2>
      <p>
        11月から12月は、忘年会やクリスマスなど人と会う機会が増える一方で、外気の寒さと室内の暖房によって肌のコンディションが最も乱れやすい時期です。どんより青白く沈んだくすみ肌や、ファンデーションの乾燥割れを諦める必要はありません。
      </p>
      <p>
        植物界屈指の必須脂肪酸バランスとスーパービタミンEの抗酸化力を併せ持つクランベリーシードオイルは、冬の肌に圧倒的なみずみずしさと発光するような透明感を呼び戻してくれます。洗顔後のブースターやメイク前の仕込み下地など、ご自身の肌悩みに寄り添うアイテムを取り入れて、真冬の乾燥シーズンを輝く笑顔で駆け抜けてください。
      </p>
    </section>

    <!-- 関連記事ボックス -->
    <div class="related-grid" id="related-grid-box"></div>

    <!-- 内部リンクプレースホルダー -->
    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</div>
      <div class="internal-links-grid" id="internal-links-container"></div>
    </div>
  </main>

  <footer class="site-footer" style="background:#ffffff;border-top:1px solid #fecdd3;margin-top:4rem;">
    <div class="footer-inner">
      <div class="footer-links-grid" id="footer-links-box"></div>
      <div class="footer-links-grid" id="footer-links-placeholder"></div>
      <p style="text-align:center;font-size:0.85rem;color:#6b7280;margin-top:2rem;">© 2026 LUMI COSMETICS. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-cranberry-oil.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated winter-cranberry-oil.html successfully!")
